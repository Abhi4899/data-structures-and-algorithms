#breath first search


from collections import deque

#checks if a person is mango seller if
#letter 'm' is present in their name
def person_is_seller(name):
    if 'm' in name:
        return True
    else:
        return False

#implementation of Breath First Search Algorithm
def search(name):
    search_queue = deque()
    search_queue += graph[name]
    searched=[] #this list keeps track of people whome you have searched before
    
    while search_queue: #while the queue isn't empty
        person = search_queue.popleft() #grabs the first person off the queue
        if person not in searched: #only search this person if you haven't already searched them
            if person_is_seller(person):
                print(person,'is mango seller')
                return True
            else:
                search_queue+=graph[person] #add all their friends to the search queue
                searched.append(person) #mark this person as searched
    return False



graph={}
graph['anuj']=[]
graph['bob']=['anuj','peggy']
graph['peggy']=[]
graph['you']=['bob','alice','claire']
graph['claire']=['tom','jonny']
graph['jonny']=[]
graph['tom']=['claire']
graph['alice']=['peggy']

if not search('you'): print('No mango seller found')

