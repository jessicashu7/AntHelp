



def get_info(category, db):

    # if place_type == "food":
    doc_ref = db.collection(category)
    docs = doc_ref.get()
    return docs
        # for doc in docs:
        #     doc_dict = doc.to_dict()
        #     for v in doc_dict['Adjectives']:
        #         print(v)
            # print(doc.to_dict())

# def get_collection_size(docs):
#     total = 0
#     for doc in docs:
#         total+= 1
#     return total;
def search_by_adjective(adj, docs):
    result = []
    for doc in docs:
        doc_dict = doc.to_dict()
        if adj.lower() in doc_dict['Adjectives']:
            result.append((doc.id, doc_dict))
    if len(result)==0:
        return None
    return result


def search_by_location(loc, docs):
    result = []
    for doc in docs:
        doc_dict = doc.to_dict()
        if loc.lower() in doc_dict['Locations']:
            result.append((doc.id, doc_dict))
    if len(result)==0:
        return None
    return result

        # for v in doc_dict['Adjectives']:
        #     if adj.lower()  v:
        #         print(doc.id)


# print(search_by_adjective('good', get_info('food')))
# print("================")
# print(search_by_location('student center', get_info('food')))
