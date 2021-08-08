from collections import deque


def seller_search(graph):
    queue_search = deque()
    queue_search += graph['you']
    checked = []
    while queue_search:
        seller = queue_search.popleft()
        if seller not in checked:
            if seller_person(seller):
                print(seller, ' is a seller')
                return True
            else:
                queue_search += graph[seller]
                checked.append(seller)
    return False


def seller_person(seller_name):
    return len(seller_name) == 4


graph = {"you": ["alice", "bob", "claire"], "bob": ["anuj", "peggy"], "alice": ["peggy"], "claire": ["thom", "jonny"],
         "anuj": [], "peggy": [], "thom": [], "jonny": []}
seller_search(graph)
