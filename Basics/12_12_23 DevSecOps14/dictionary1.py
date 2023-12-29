
actor = {
    'name': 'kevin hart',
    'id': 443221,
    'movies': ['fatherhood', 'whats now'],
}

# print(actor)
# print(type(actor))
# print(actor['name'])
# print(actor.get('salary'))
#
# actor['name'] = 'kevin <3'
# print(actor)
# actor['salary'] = 18000
# print(actor)
# print(actor)
# del actor['id'] # delete the key and the value
# print(actor)
#
# name = actor.pop('name')
# print(actor)
# print(name)
# print(actor)
# actor.clear()
# print(actor) # delete all the pairs

# x = actor.popitem()
# print(x)

# for k in actor: # iterate over the keys
#     print(k)
#
# for k in actor:
#     print(f'the value of the key{k} is {actor[k]}')



# print(actor) #dict
# print(actor.values()) # tuple values
# print(actor.keys()) # keys tuple
# print(actor.items()) # tuple list

# for v in actor.values():
#     if v is int and v > 20:
#         print(v)

for k,v in actor.items(): # iterate over akk the key and values of json 
        print(k,v)