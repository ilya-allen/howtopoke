import pokepy
client = pokepy.V2Client().get_pokemon('mew')
print(client[0].weight)


# https://github.com/PokeAPI/pokepy 
# USEFUL LINK TO UNDERSTANDING THE API



