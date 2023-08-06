
def __doc_sqlite3():
    import sqlite3

    LIGHTDB = sqlite3.connect('dasifo_default_storage.db')
    cur = LIGHTDB.cursor()

    # Create table
    cur.execute('''CREATE TABLE storages
                   (db_name text, host text, port text, username text, password text)''')

    # This is the qmark style:
    cur.execute("insert into lang values (?, ?)", ("C", 1972))

    # The qmark style used with executemany():
    lang_list = [
        ("Fortran", 1957),
        ("Python", 1991),
        ("Go", 2009),
    ]
    cur.executemany("insert into lang values (?, ?)", lang_list)

    # And this is the named style:
    cur.execute("select * from lang where first_appeared=:year", {"year": 1972})
    print(cur.fetchall())

    # Save (commit) the changes
    LIGHTDB.commit()

    # We can also close the connection if we are done with it.
    # Just be sure any changes have been committed or they will be lost.
    LIGHTDB.close()

import os
from .sql_db import _create_mysql
def create_connection(dbname=None, have=None):
    """  """
    DATABASES = ('mysql', 'postgresql', 'mongodb')
    DBKEYS = ('dbname', 'host', 'port', 'username', 'password')
    try:
        db_type = input(f"Enter one of these supported DBs ({DATABASES}): ")
        for k in DBKEYS:
            os.environ[db_type+'_'+k] = input(f"Enter {k}: ")

        if db_type == 'mysql':
            _create_mysql()


    except:
        pass


def find(con, table, id=None, one=False):
    pass
    sql = """  """
    cursor = con.cursor()
    cursor.execute(sql)
    return cursor.fetchall()


def update(con, table, id=None, have=None, by=None):
    pass


def insert(con, table, col_values=None):
    pass
