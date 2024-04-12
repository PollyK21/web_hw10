from pymongo import MongoClient

client = None


def get_mongodb():
    global client
    if client is None:
        client = MongoClient(
            "mongodb+srv://polkulish:polly@polly.mvw6oqq.mongodb.net/")
    db = client.test
    return db
