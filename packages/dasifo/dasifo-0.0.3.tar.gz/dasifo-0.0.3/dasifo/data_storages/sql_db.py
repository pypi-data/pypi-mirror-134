"""
Description:
   make connections with most of sql DB servers:
   - MySQL
   - PostgreSQL
"""
import os
import subprocess

from mysql.connector import connect, Error
import psycopg2
from postgis.psycopg import register
# from postgis import LineString, Point, Polygon, MultiPoint, MultiPolygon, MultiLineString, Geometry


def _start_server(server_name=None):
    if server_name == 'mysql':
        bashCmd = ["ls", "."]
        process = subprocess.Popen(bashCmd, stdout=subprocess.PIPE)
        output, error = process.communicate()
    else:
        print("Not supported server")
def _create_mysql():
    try:
        # global
        MYSQLDBCON = connect(
            host=os.environ.get('mysql_host'),  # locaolhost
            port=os.environ.get('mysql_port'),  # 3306
            user=os.environ.get('mysql_username'),  #
            password=os.environ.get('mysql_password'),  # ''
            #database=os.environ.get('mysql_dbname')
        )

        # we have to check if the DBname if created or we recreate it
    except Error as e:
        print(e)
        MYSQLDBCON = None

def _create_postgresql():
    try:
        # global
        POSTGRESQLDBCON = psycopg2.connect(
                host=os.environ.get('postgresql_host'),  # locaolhost
                port=os.environ.get('postgresql_port'),  # 5432
                user=os.environ.get('postgresql_username'),  #
                password=os.environ.get('postgresql_password'),  # ''
                #database=os.environ.get('postgresql_dbname')
        )

        # we have to check if the DBname if created or we recreate it
        try:
            register(POSTGRESQLDBCON)
        except:
            # todo: create postgis and postgis_topology extensions for postgresql !
            print("there is no postgis extension in your postgresql server!")

        # cursor = POSTGRESQLDB.cursor()
    except:
        POSTGRESQLDBCON = None