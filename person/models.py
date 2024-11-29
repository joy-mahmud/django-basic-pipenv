from django.db import models
from dbConnection import mydb
# Create your models here.
personCollection = mydb['person']

def printCollection():
    print(mydb.list_collection_names())
