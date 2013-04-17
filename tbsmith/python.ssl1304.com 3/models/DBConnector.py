#!/usr/bin/python

import MySQLdb


class DBConnector():

    def get_connection(self):
        self.db = MySQLdb.connect(host="127.0.0.1",
                                  port=3306,
                                  user="root",
                                  passwd="root",
                                  db="fakeUsers")

    def execute_statement(self, stmnt=''):
        self.get_connection()
        cursor = self.db.cursor()
        cursor.execute(stmnt)
        return cursor.fetchall()

    def get_random_user(self):
        result = self.execute_statement("SELECT * from address \
                                         ORDER BY rand() LIMIT 1")
        return result
