friends_graph = {}
friends_graph['you'] = ['alice', 'bob', 'claire']
friends_graph['alice'] = ['peggy']
friends_graph['bob'] = ['anuj', 'peggy']
friends_graph['claire'] = ['jonny', 'thom']
friends_graph['anuj'] = []
friends_graph['jonny'] = []
friends_graph['peggy'] = []
friends_graph['thom'] = []

from collections import deque

def searchMangoSeller(name):
  if not name.lower() in friends_graph:
    return False
  search_queue = deque()
  search_queue += friends_graph[name.lower()]
  searched = []
  while search_queue:
    person = search_queue.popleft()
#    print(person)
    if not person in searched:
      if isMangoSeller(person):
        print(person + ' is a mango seller!')
        return True
      else:
        search_queue += friends_graph[person]
        searched.append(person)
  return False

def isMangoSeller(name):
  return name[-1].lower() == 'm'
