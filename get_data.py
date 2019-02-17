def get_info(category, db):
    doc_ref = db.collection(category)
    docs_for_size = doc_ref.get()
    if check_category(category, db, docs_for_size) == 0:
        return []

    doc_ref2 = db.collection(category)
    docs_for_return = doc_ref2.get()
    return docs_for_return


def check_category(category, db, docs):
    total = 0
    for doc in docs:
        total += 1
    return total

def get_items_in_cat(docs):
    items = []
    for doc in docs:
        items.append((doc.id, doc_dict))
    return items


def search_by_adjective(adj, docs):
    result = []
    for doc in docs:
        doc_dict = doc.to_dict()
        if adj.lower() in doc_dict['Adjectives']:
            result.append((doc.id, doc_dict))
    return result


def search_by_location(loc, docs):
    result = []
    for doc in docs:
        doc_dict = doc.to_dict()
        if loc.lower() in doc_dict['Locations']:
            result.append((doc.id, doc_dict))
    return result
