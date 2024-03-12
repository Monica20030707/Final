import random

# List of words from http://www.free-teacher-worksheets.com/

# The orginal word list has been modified into 10 different categories, and will be called
# based in their categories.

animals = [
    "aardvark", "alligator", "ant", "antelope", "ape", "armadillo", "baboon", "badger", "bat", "bear",
    "beaver", "bee", "bison", "buffalo", "butterfly", "camel", "cat", "cheetah", "chimpanzee", "cobra",
    "cougar", "coyote", "crocodile", "deer", "dolphin", "eagle", "elephant", "falcon", "flamingo", "fox"
]

fruits = [
    "apple", "apricot", "banana", "blackberry", "blueberry", "cantaloupe", "cherry", "coconut", "cranberry", "date",
    "dragonfruit", "fig", "grape", "guava", "kiwi", "lemon", "lime", "mango", "orange", "papaya",
    "passionfruit", "peach", "pear", "pineapple", "plum", "pomegranate", "raspberry", "strawberry", "watermelon", "yuzu"
]

colors = [
    "amber", "amethyst", "azure", "beige", "black", "blue", "bronze", "brown", "burgundy", "caramel",
    "cerulean", "charcoal", "chartreuse", "chocolate", "cinnamon", "cobalt", "coral", "crimson", "cyan", "emerald",
    "fuchsia", "gold", "indigo", "ivory", "jade", "lavender", "magenta", "maroon", "olive", "orange"
]

countries = [
    "argentina", "australia", "brazil", "canada", "china", "egypt", "france", "germany", "india", "italy",
    "japan", "mexico", "netherlands", "russia", "spain", "sweden", "thailand", "turkey", "united kingdom", "united states"
]

sports = [
    "baseball", "basketball", "boxing", "cricket", "football", "golf", "hockey", "rugby", "soccer", "tennis",
    "badminton", "cycling", "swimming", "volleyball", "wrestling", "skiing", "snowboarding", "surfing", "running", "hiking"
]

occupations = [
    "actor", "artist", "chef", "doctor", "engineer", "firefighter", "lawyer", "nurse", "pilot", "teacher",
    "dentist", "musician", "scientist", "athlete", "journalist", "architect", "photographer", "veterinarian", "mechanic", "politician"
]

vehicles = [
    "car", "truck", "bus", "motorcycle", "bicycle", "train", "boat", "airplane", "helicopter", "scooter",
    "ambulance", "taxi", "submarine", "tractor", "spaceship", "tank", "yacht", "jet", "hovercraft", "ferry"
]

planets = [
    "mercury", "venus", "earth", "mars", "jupiter", "saturn", "uranus", "neptune", "pluto", "ceres",
    "eris", "haumea", "makemake", "sedna", "quaoar", "charon", "callisto", "titan", "europa", "ganymede"
]

movies = [
    "avatar", "titanic", "avengers", "jurassic park", "star wars", "harry potter", "frozen", "inception", "jaws", "tangled",
    "the lion king", "forrest gump", "batman", "finding nemo", "toy story", "shrek", "gladiator", "interstellar", "the godfather", "the matrix"
]

foods = [
    "pizza", "hamburger", "sushi", "pasta", "taco", "burrito", "steak", "salad", "soup", "sandwich",
    "pancake", "waffle", "sushi", "lasagna", "curry", "spaghetti", "fried chicken", "ramen", "donut", "bagel"
]

# Saving all lists into one dictonary, named categories, with numbers as key, which will point at the lists
# as values.
categories = {
    "1": animals,
    "2": fruits,
    "3": colors,
    "4": countries,
    "5": sports,
    "6": occupations,
    "7": vehicles,
    "8": planets,
    "9": movies,
    "10": foods
}

# Get random word from the specified categories
def get_random_word_from_category(category):
    word = random.choice(categories[category])
    return word
