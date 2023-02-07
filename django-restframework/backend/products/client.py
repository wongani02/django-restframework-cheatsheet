from algoliasearch_django import algolia_engine

def get_client():
    return algolia_engine.client

def get_index(index_name='pablo_Product'):
    client = get_client()
    index = client.init_index(index_name)
    return index


'''without tag search'''
# def perform_serach(query, **kwargs):
#     index = get_index()
#     results=index.search(query)
#     return results

'''with tag search functionality'''
def perform_serach(query, **kwargs):
    index = get_index()
    params = {}
    tags = ''
    if tags in kwargs:
        tags = kwargs.pop('tags') or []
        if len(tags)!=0:
            params['tagFilters'] = tags
    results=index.search(query, params)
    return results