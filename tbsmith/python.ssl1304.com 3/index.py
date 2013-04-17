#!/usr/bin/python

from models.DBConnector import DBConnector

print "Content-type: text/html\n\n"

result = DBConnector().get_random_user()

print result
