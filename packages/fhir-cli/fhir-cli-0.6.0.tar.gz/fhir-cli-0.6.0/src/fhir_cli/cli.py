from typing import Iterator, Tuple

import fire
from psycopg2 import ProgrammingError, connect, sql
from psycopg2.extras import RealDictCursor
from requests import HTTPError

from fhir_cli import (
    DBT_SCHEMA,
    FHIR_COLUMN_NAME,
    POSTGRES_DB,
    POSTGRES_HOST,
    POSTGRES_PASSWORD,
    POSTGRES_PORT,
    POSTGRES_USER,
    log,
)
from fhir_cli.admin import Admin
from fhir_cli.dbt import Dbt
from fhir_cli.fhir_resource import FhirResource, FhirValidationError
from fhir_cli.utils.compact import dict_compact
from fhir_cli.utils.number_print import number_print

CURSOR_ITERSIZE = 20


def get_resources_from_model(
    cursor, model: str, offset: int = 0, limit: int = 100
) -> Iterator[Tuple[int, dict]]:
    """get_resources_from_model looks for a fhir model file and retrieves the Fhir resources

    This function uses a named cursor fetching at most CURSOR_ITERSIZE rows
    at each network roundtrip during iteration on the cursor
    https://www.psycopg.org/docs/cursor.html#cursor.itersize

    Args:
        cursor: a database connection cursor
        model (str): a Fhir model name
        offset (:obj:`int`, optional): an offset for the executed query. Defaults to 0.
        limit (:obj:`int`, optional): a limit for the executed query. Defaults to 100.
    """
    select_fhir_stmt = sql.SQL(
        "SELECT id, {fhir_column_name} FROM {fhir_model} ORDER BY id LIMIT %s OFFSET %s"
    ).format(
        fhir_column_name=sql.Identifier(FHIR_COLUMN_NAME),
        fhir_model=sql.Identifier(model),
    )
    cursor.execute(select_fhir_stmt, (limit, offset))
    for row in cursor:
        yield row["id"], dict_compact(row[FHIR_COLUMN_NAME])


class Cli:
    """a cli to manage your DbtOnFhir project"""

    def __init__(self):
        self.dbt = Dbt()
        self.admin = Admin()

    @staticmethod
    def link(source: str, target: str = None):
        """Create a foreign schema from a schema of the source database

        This command uses a foreign data wrapper to access data
        stored in an external server. The module opens a connection and extracts
        a database schema. Subsequently a user can import the data to the local
        database by creating a table or a materialized view selecting from a
        foreign table of a given schema.

        Args:
            source (str): the source schema
            target (:obj:`str`, optional): the target schema. If not specified,
            the target schema will take the name of the source schema.
        """

        if not target:
            target = source

        conn = connect(
            host=POSTGRES_HOST,
            dbname=POSTGRES_DB,
            port=POSTGRES_PORT,
            user=POSTGRES_USER,
            password=POSTGRES_PASSWORD,
        )

        schema_stmt = sql.SQL("CREATE SCHEMA {target_schema}").format(
            target_schema=sql.Identifier(target)
        )
        import_stmt = sql.SQL(
            "IMPORT FOREIGN SCHEMA {source_schema} FROM SERVER source_server INTO {target_schema}"
        ).format(
            source_schema=sql.Identifier(source),
            target_schema=sql.Identifier(target),
        )
        with conn.cursor() as curs:
            curs.execute(schema_stmt)
            curs.execute(import_stmt)
            conn.commit()

        conn.close()

    @staticmethod
    def validate(model: str, offset: int = 0, limit: int = 100):
        """Extract a fhir model row and validates the Fhir resource
        against a Fhir server

        Args:
            model (str): should be a valid DBT Fhir model name such as `observation_heartrate`
            offset (:obj:`int`, optional): set an offset to the query. Defaults to 0.
            limit (:obj:`int`, optional): a limit for the executed query. Defaults to 100.
        """
        conn = connect(
            host=POSTGRES_HOST,
            dbname=POSTGRES_DB,
            port=POSTGRES_PORT,
            user=POSTGRES_USER,
            password=POSTGRES_PASSWORD,
            cursor_factory=RealDictCursor,
            options=f"-c search_path={DBT_SCHEMA}",
        )
        cursor = conn.cursor(name="curname")
        cursor.itersize = CURSOR_ITERSIZE
        try:
            for _id, resource in get_resources_from_model(cursor, model, offset, limit):
                fhir = FhirResource(resource)
                number_print(repr(fhir))
                try:
                    fhir.validate()
                    log.info(f"\U0001F525 resource (id={_id}) is valid")
                except FhirValidationError as e:
                    log.error(e)
                input("Press [Return] for the next result or [Ctrl+c] to quit")
        except ProgrammingError as e:
            conn.rollback()
            log.error(e)
        except HTTPError as e:
            log.error(e.response.json())
        except KeyboardInterrupt:
            pass
        finally:
            cursor.close()
            conn.close()


def run():
    cli = Cli()
    fire.Fire(cli)


if __name__ == "__main__":
    run()
