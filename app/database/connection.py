"""Manejo de conexiones a PostgreSQL con pooling."""

import os
import psycopg2
from psycopg2 import pool as pg_pool
from psycopg2.extras import RealDictCursor
from contextlib import contextmanager
from typing import Optional, Generator
from app.logger import get_logger
from app.exceptions import DatabaseError

logger = get_logger("database")

_MIN_CONN = int(os.environ.get("DB_MIN_CONN", "1"))
_MAX_CONN = int(os.environ.get("DB_MAX_CONN", "10"))

_connection_pool: Optional[pg_pool.ThreadedConnectionPool] = None


def get_database_url() -> str:
    url = os.environ.get("DATABASE_URL")
    if not url:
        raise DatabaseError(
            "DATABASE_URL no definida. "
            "Define DATABASE_URL en .env o como variable de entorno."
        )
    return url


def init_pool():
    global _connection_pool
    if _connection_pool is not None:
        return
    url = get_database_url()
    try:
        _connection_pool = pg_pool.ThreadedConnectionPool(
            _MIN_CONN, _MAX_CONN, url
        )
        logger.info(
            "Pool de conexiones inicializado "
            f"(min={_MIN_CONN}, max={_MAX_CONN})"
        )
    except psycopg2.Error as e:
        logger.error(f"Error al inicializar pool: {e}")
        raise DatabaseError(f"No se pudo conectar a la base de datos: {e}")


def close_pool():
    global _connection_pool
    if _connection_pool:
        _connection_pool.closeall()
        _connection_pool = None
        logger.info("Pool de conexiones cerrado")


@contextmanager
def get_connection() -> Generator:
    conn = None
    try:
        if _connection_pool is None:
            init_pool()
        conn = _connection_pool.getconn()
        if conn.closed:
            _connection_pool.putconn(conn, close=True)
            conn = _connection_pool.getconn()
        with conn.cursor() as cur:
            cur.execute("SET search_path TO public")
        yield conn
        conn.commit()
    except psycopg2.Error as e:
        if conn:
            try:
                conn.rollback()
            except Exception:
                pass
        logger.error(f"Error de base de datos: {e}")
        raise DatabaseError(f"Error de base de datos: {e}")
    finally:
        if conn and _connection_pool:
            try:
                _connection_pool.putconn(conn)
            except Exception:
                try:
                    conn.close()
                except Exception:
                    pass


@contextmanager
def get_cursor():
    with get_connection() as conn:
        cur = conn.cursor(cursor_factory=RealDictCursor)
        try:
            yield cur
        finally:
            cur.close()


def fetch_one(query: str, params: tuple = ()) -> Optional[dict]:
    with get_cursor() as cur:
        cur.execute(query, params)
        row = cur.fetchone()
        return dict(row) if row else None


def fetch_all(query: str, params: tuple = ()) -> list:
    with get_cursor() as cur:
        cur.execute(query, params)
        rows = cur.fetchall()
        return [dict(r) for r in rows]


def execute(query: str, params: tuple = ()) -> int:
    with get_connection() as conn:
        cur = conn.cursor()
        try:
            cur.execute(query, params)
            return cur.rowcount
        finally:
            cur.close()


def execute_returning(query: str, params: tuple = ()) -> Optional[dict]:
    with get_cursor() as conn:
        conn.execute(query, params)
        row = conn.fetchone()
        return dict(row) if row else None
