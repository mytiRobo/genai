#Scope

# enemies = 1

# def increase_enemies():
#     enemies = 2
#     print(f'enemies inside funcrion: {enemies}')

# increase_enemies()
# print(f'enemies outside function: {enemies}')

#Local Scope

# def drink_potion():
#     potion_strength = 2
#     print(potion_strength)

# drink_potion()
# print(potion_strength)

#Global Scope

# player_health = 10

# def drink_potion():
#     potion_strength = 2
#     print(potion_strength)

# drink_potion()

#There is no block scope

# game_level = 3
# enemies = ['skeleton', 'zombie', 'alien']

# if game_level < 5:
#     new_enemy = enemies[0]

# print(new_enemy)


#Modifying global scope

enemies = 1

def increase_enemies():
    # global enemies
    # enemies += 1
    print(f'enemies inside funcrion: {enemies}')
    return enemies + 100

enemies = increase_enemies()
print(f'enemies outside function: {enemies}')
