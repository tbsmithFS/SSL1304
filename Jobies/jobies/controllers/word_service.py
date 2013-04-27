#!/usr/bin/python

import json
import urllib2
from models.DBConnector import DBConnector


class SearchService():

    def __init__(self):
        dbcon = DBConnector()
        self.cnx = dbcon.get_connection()
        self.cursor = self.cnx.cursor()

    def search(self, fn):

        sql = ("SELECT firstname, lastname, city, state, "
               + "zip, phone FROM million WHERE firstname "
               + "LIKE '{}' LIMIT 10").format(fn)

        self.cursor.execute(sql)
        
        allDefs = []
        
        for firstname, lastname, city, state, zip, phone in self.cursor:
            
            allDefs.append({
                 'firstname': firstname,
                 'lastname': lastname,
                 'city': city,
                 'state': state,
                 'zip': zip,
                 'phone': phone})
        
        print json.dumps(allDefs)    

        self.cursor.close()
        self.cnx.close()
