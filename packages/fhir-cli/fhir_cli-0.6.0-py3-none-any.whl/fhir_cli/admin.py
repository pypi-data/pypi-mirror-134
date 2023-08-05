import getpass
import glob
import re
from typing import Iterator
from uuid import NAMESPACE_URL, uuid5

import requests
from psycopg2 import connect, sql

from fhir_cli import (
    CONNECT_CONFIG_TEMPLATE,
    CONNECT_URL,
    DBT_META_TABLE,
    DBT_SCHEMA,
    FHIR_DBT_SCHEMA,
    FUNCTIONS_DIR_NAME,
    INIT_DB_TEMPLATE,
    JINJA_ENV,
    POSTGRES_DB,
    POSTGRES_HOST,
    POSTGRES_PASSWORD,
    POSTGRES_PORT,
    POSTGRES_SERVER_NAME,
    POSTGRES_USER,
    log,
)


def get_user_defined_functions() -> Iterator[str]:
    for file_path in glob.iglob(f"{FUNCTIONS_DIR_NAME}/**/*.sql", recursive=True):
        with open(file_path, "r") as f:
            yield f.read()


def is_jdbc_url(url: str) -> bool:
    return False if re.match(r"^jdbc:\w+://.+:\d+/\w+$", url) is None else True


class Admin:
    """The admin command is used by an administrator to initialize a new project"""

    @staticmethod
    def createdb(database: str):
        """Create a new db for the project

        Args:
            database (str): a name for the new database
        """

        conn = connect(
            host=POSTGRES_HOST,
            dbname=POSTGRES_DB,
            port=POSTGRES_PORT,
            user=POSTGRES_USER,
            password=POSTGRES_PASSWORD,
        )
        conn.autocommit = True

        stmt = sql.SQL("CREATE DATABASE {database}").format(database=sql.Identifier(database))

        with conn.cursor() as curs:
            curs.execute(stmt)

        conn.close()

    @staticmethod
    def initdb(database: str, url: str, user: str = None, password: str = None):
        """Initialize the new db for the project

        Args:
            database (str): the database to initialize
            url (str): the source database JDBC url (formatted
            as jdbc:database_type//host:port/dbname) used to generate the project id
            user (:obj:`str`, optional): a username of choice.
            password (:obj:`str`, optional): a password of choice. If not specified,
            the command will prompt for a password
        """

        if not is_jdbc_url(url):
            log.error(f"URL {url} is not in a valid JDBC format")
            return

        while not password:
            password = getpass.getpass()

        conn = connect(
            host=POSTGRES_HOST,
            dbname=database,
            port=POSTGRES_PORT,
            user=POSTGRES_USER,
            password=POSTGRES_PASSWORD,
        )
        conn.autocommit = True

        user_stmt = sql.SQL("CREATE USER {role} WITH PASSWORD %s").format(role=sql.Identifier(user))

        project_id = uuid5(NAMESPACE_URL, url)
        initdb_stmt = JINJA_ENV.get_template(INIT_DB_TEMPLATE).render(
            database=database,
            dbt_schema=DBT_SCHEMA,
            dbt_meta_table=DBT_META_TABLE,
            project_id=project_id,
            role=user,
            project_url=url,
        )

        with conn.cursor() as curs:
            curs.execute(user_stmt, (password,))
            curs.execute(initdb_stmt)
            set_search_path_stmt = sql.SQL("SET search_path TO {dbt_schema}").format(
                dbt_schema=sql.Identifier(DBT_SCHEMA)
            )
            curs.execute(set_search_path_stmt)
            for func_definition in get_user_defined_functions():
                curs.execute(func_definition)

        conn.close()

    @staticmethod
    def connect(database: str):
        """Add a Kafka Connect connector

        Args:
            database (str): the database to connect
        """
        connector = JINJA_ENV.get_template(CONNECT_CONFIG_TEMPLATE).render(
            project_db=database,
            postgres_server_name=POSTGRES_SERVER_NAME,
            postgres_port=POSTGRES_PORT,
            postgres_user=POSTGRES_USER,
            postgres_password=POSTGRES_PASSWORD,
            schemas=",".join([FHIR_DBT_SCHEMA]),
        )
        r = requests.post(
            f"{CONNECT_URL}/connectors/",
            data=connector,
            headers={"Content-Type": "application/json"},
        )
        r.raise_for_status()

    @staticmethod
    def dblink(
        target: str, source: str, type: str, host: str, port: int, user: str, password: str = None
    ):
        """Create a foreign server linking the source database to the project database

        This command uses a foreign data wrapper to create a connection to another database
        thanks to the provided credentials.

        Args:
            target (str): the target database
            source (str): the source database
            type (str): the source database type (can be either `oracle` or `postgres`)
            host (str): the source server host
            port (int): the source server port
            user (str): a source database user
            password (:obj:`str`, optional): the user password. If not specified,
            the command will prompt for a password
        """

        while not password:
            password = getpass.getpass()

        conn = connect(
            host=POSTGRES_HOST,
            dbname=target,
            port=POSTGRES_PORT,
            user=POSTGRES_USER,
            password=POSTGRES_PASSWORD,
        )
        conn.autocommit = True

        stmt = JINJA_ENV.get_template(f"{type}_fdw.sql.j2").render(
            source_db=source,
            source_host=host,
            source_port=port,
            source_user=user,
            source_password=password,
        )
        with conn.cursor() as curs:
            curs.execute(stmt)

        conn.close()
