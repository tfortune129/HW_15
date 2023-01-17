import requests, json
url = 'https://pokeapi.co/api/v2/pokemon/5',
'https://pokeapi.co/api/v2/pokemon/17',
'https://pokeapi.co/api/v2/pokemon/61',
'https://pokeapi.co/api/v2/pokemon/1',
'https://pokeapi.co/api/v2/pokemon/35'
       
response = requests.get(url)
# print (response)
# print (response.ok)
# if response.ok:
#     data = response.json()
#     drivers = data['forms']
#     my_list = []
#     for info in drivers:
#         char = info['name']
#         my_list.append(f'{char}')
#     print (my_list)