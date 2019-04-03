# -*- coding: utf-8 -*-

from pymongo import MongoClient
client = MongoClient("mongodb://127.0.0.1:1111, 127.0.0.1:2222, 127.0.0.1:3333", replicaset='test')
print(client.test.testdb.find_one())
