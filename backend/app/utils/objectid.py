def str_id(doc):
    if doc:
        doc["_id"] = str(doc["_id"])
    return doc