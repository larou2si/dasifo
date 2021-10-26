"""
Description:
   make connections with most of sql DB servers:
   - MySQL
   - PostgreSQL
"""
from mysql.connector import connect, Error
import psycopg2
from postgis.psycopg import register
# from postgis import LineString, Point, Polygon, MultiPoint, MultiPolygon, MultiLineString, Geometry


try:
    MYSQLDBCON = connect(
        host="localhost",
        user=input("Enter username: "),
        password=("Enter password: "),
        database="")
except Error as e:
    print(e)
    MYSQLDBCON = None


try:
    POSTGRESQLDBCON = psycopg2.connect(
        host=__host,
        database=__database,
        user=__user,
        port=__port)
    try:
        register(POSTGRESQLDB)
    except:
        # todo: create postgis and postgis_topology extensions for postgresql !
        print("there is no postgis extension in your postgresql server!")

    # cursor = POSTGRESQLDB.cursor()
except:
    POSTGRESQLDBCON = None