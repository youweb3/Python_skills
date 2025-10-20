print("\n=== Welcome to Movie Recommender===\n")

# Prompt the user for movie preferences
action = input("Do you like action movies? (yes/no):").lower() =="yes"
comedy = input("Do you like comedy movies? (yes/no):").lower() =="yes"
drama = input("Do you like drama movies? (yes/no):").lower() =="yes"
animation = input("Do you like animation movies? (yes/no):").lower() =="yes"

#=== Combine booleans using logical operators

#======= All genre
if action and comedy and drama and animation:
    genre = "All-Rounder"

#========combination Three genre
elif action and drama and comedy and not animation:
    genre = "Action-Comedy-Drama"
elif action and comedy and animation and not drama:
    genre = "Action-Comedy-Animation"
elif action and drama and animation and not comedy:
    genre = "Action-Drama-Animation"
elif comedy and drama and animation and not  action:
    genre = "Comedy-Drama-Animation"

#=====combination Two genre
elif action and comedy and not drama and not animation:
    genre = "Action-Comedy"
elif action and drama and not comedy and not animation:
    genre = "Action-Drama"
elif action and animation and not comedy and not drama:
    genre = "Action-Animation"
elif comedy and drama and not action and not animation:
    genre = "Comedy-Drama"
elif comedy and animation and not action and not drama:
    genre = "Comedy-Animation"
elif drama and animation and not action and not comedy:
    genre = "Drama-Animation"

#=====One genre
elif action:
    genre = "Action"
elif comedy:
    genre = "Comedy"
elif drama:
    genre = "Drama"
elif animation:
    genre = "Animation"
else:
    genre = "Unknown"

#=====Recommend movies based on the genre using conditional statements
print(f"\nYour selected genre: {genre}")
print("Recommended movies:")

if genre == 'All-Rounder':
    print("Recommended movies: 'The Avengers', 'The Incredibles', 'Forrest Gump'")
elif genre == 'Action-Comedy-Drama':
    print("Recommended movies: 'Deadpool', 'The Nice Guys', 'The Wolf of Wall Street'")
elif genre == 'Action-Comedy-Animation':
    print("Recommended movies: 'Kung Fu Panda', 'The Lego Movie', 'Big Hero 6'")
elif genre == 'Action-Drama-Animation':
    print("Recommended movies: 'Spider-Man: Into the Spider-Verse', 'Zootopia', 'Akira'")
elif genre == 'Comedy-Drama-Animation':
    print("Recommended movies: 'Inside Out', 'Soul', 'Up'")
elif genre == 'Action-Comedy':
    print("Recommended movies: 'Rush Hour', 'The Mask', 'Guardians of the Galaxy'")
elif genre == 'Action-Drama':
    print("Recommended movies: 'John Wick', 'The Dark Knight', 'Inception'")
elif genre == 'Action-Animation':
    print("Recommended movies: 'How to Train Your Dragon', 'Big Hero 6', 'Mad Max: Fury Road'")
elif genre == 'Comedy-Drama':
    print("Recommended movies: 'The Big Sick', 'Little Miss Sunshine', 'The Intouchables'")
elif genre == 'Comedy-Animation':
    print("Recommended movies: 'Shrek', 'The Lego Movie', 'Zootopia'")
elif genre == 'Drama-Animation':
    print("Recommended movies: 'Coco', 'Inside Out', 'The Green Mile'")
elif genre == 'Action':
    print("Recommended movies: 'Die Hard', 'Mad Max: Fury Road', 'John Wick'")
elif genre == 'Comedy':
    print("Recommended movies: 'The Hangover', 'Superbad', 'Step Brothers'")
elif genre == 'Drama':
    print("Recommended movies: 'The Shawshank Redemption', 'Forrest Gump', 'The Pursuit of Happyness'")
elif genre == 'Animation':
    print("Recommended movies: 'Toy Story', 'Coco', 'Frozen'")
else:
    print("Sorry, we couldn't determine your movie preferences.")
