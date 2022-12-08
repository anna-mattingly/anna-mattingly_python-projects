# Automated Decision Making - Which movie should I watch?

# skills exercised: python - lists, random module, input()

from random import choice   

movies = [['home alone', 'holiday'],
    ['the sandlot','comedy'],
    ['the blind side', 'drama'],
    ['lion king', 'childrens']]

# what mood am I in?
print('what mood are you in?')
mood = input()

# loop through to find a matching mood
for item in movies:
    if item [1] == mood:
        print( mood + 'movie: ' + item[0])

print(choice(movies))
