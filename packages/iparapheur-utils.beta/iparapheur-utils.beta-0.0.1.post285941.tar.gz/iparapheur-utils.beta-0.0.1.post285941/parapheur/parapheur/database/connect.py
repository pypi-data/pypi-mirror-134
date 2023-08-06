# coding=utf-8
# module Database
from urlparse import urlparse
import pymysql.cursors


def connect(varconf):
    mysqldburl = varconf.get("Parapheur", "db.url")
    urlparsed = urlparse(mysqldburl[5:])
    mysqlserver = urlparsed.hostname
    mysqlport = 3306
    mysqluser = "null"
    mysqlpwd = "null"
    mysqlbase = "null"
    if urlparsed.port is not None:
        mysqlport = urlparsed.port
        mysqluser = varconf.get("Parapheur", "db.username")
        mysqlpwd = varconf.get("Parapheur", "db.password")
        mysqlbase = varconf.get("Parapheur", "db.name")
    cnx = pymysql.connect(user=mysqluser, password=mysqlpwd, host=mysqlserver, port=mysqlport, database=mysqlbase)
    return cnx
