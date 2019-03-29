# -*- coding: utf-8 -*-

from pymongo import MongoClient
client = MongoClient("mongodb://127.0.0.1:27017, 127.0.0.1:27018, 127.0.0.1:27019", replicaset='repset')
print(client.test.testdb.find_one())
