#!/usr/bin/python

import mysql.connector


class DBConnector():

    def get_connection(self):
        cnx = mysql.connector.connect(host="127.0.0.1",
                                           port=8889,
                                           user="root",
                                           passwd="root",
                                           db="JobiesDB")
        return cnx
