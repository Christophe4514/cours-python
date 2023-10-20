from tinydb import TinyDB, Query, where

db = TinyDB('data_02.json', indent=4)

users = db.table("Users") # table user
roles = db.table("Roles") # table role

users.insert_multiple([
    {"name": "Patrick", "salary": 2500},
    {"name": "Paul", "salary": 3500},
    {"name": "Dani", "salary": 1500},
                       ])

roles.insert_multiple([
    {"name":"Pythonista"},
    {"name":"Javaista"},
    {"name":"JavaScripista"}
])