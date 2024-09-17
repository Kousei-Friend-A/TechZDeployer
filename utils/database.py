from pymongo import MongoClient

db = MongoClient(
    "mongodb+srv://friendakouseimanu:asdfg@cluster0.1trpq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
).TechZDeployer.users


def inc_user(user, name, link):
    db.update_one(
        {"user": user},
        {"$inc": {"count": 1}, "$push": {"repos": [name, link]}},
        upsert=True,
    )


def repo_count(user):
    user = db.find_one({"user": user})
    if not user:
        return 0
    return user.get("count", 0)
