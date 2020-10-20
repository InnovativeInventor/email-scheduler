import pymongo
import config
import datetime
import mongoset

# client = pymongo.MongoClient(host=config.DB)
# table = client["serverless"]["notifications"]

client = mongoset.connect(config.DB, "serverless")
table = client["notifications"]

email_document = {
    "email": {
        "address": "maxfan8@gmail.com",
        "subject": "TEST",
        "msg": "This is a test.",
    },
    "sent": False,
    "time": datetime.datetime.now(),
}

if table.insert(email_document):
    print("Inserted")
