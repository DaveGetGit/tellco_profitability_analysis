import os
import psycopg2
from psycopg2 import pool
from dotenv import load_dotenv

load_dotenv()


class PostgresConnectionPool:
    """
This class handles a pool of PostgreSQL database connections via the psycopg2 library.
Rather than repeatedly opening and closing a database connection when required, 
this class establishes a pool of up to 10 connections. A connection object can be 
accessed from this pool and manually released when no longer needed.
    """

    def __init__(self):
        self.host = os.getenv('DB_HOST')
        self.user = os.getenv('DB_USER')
        self.password = os.getenv('DB_PASSWORD')
        self.database = os.getenv('DB_NAME')
        self.pool = None

    def create_pool(self):
        """
        Creates a connection pool if it doesn't exist and returns it.
        """
        if self.pool is None:
            connection_string = f"host={self.host} user={
                self.user} password={self.password} dbname={self.database}"
            self.pool = psycopg2.pool.SimpleConnectionPool(
                1, 10, connection_string)
        return self.pool

    def get_connection(self):
        """
        Retrieves a connection from the pool.
        """
        return self.create_pool().getconn()

    def release_connection(self, connection):
        """
        Releases a connection back to the pool.
        """
        if connection:
            self.create_pool().putconn(conn=connection)


postgres_pool = PostgresConnectionPool()
