# -----------------------------------
# Day 2 - Python Basics for DanceGen AI
# -----------------------------------


# 1. VARIABLES
# Variables store information.

song = "Blinding Lights"
dance_style = "Hip-hop"
energy = "High"
difficulty = "Beginner"
duration = 15

print("Song:", song)
print("Dance Style:", dance_style)
print("Energy:", energy)
print("Difficulty:", difficulty)
print("Duration:", duration)


# -----------------------------------
# 2. LISTS
# A list stores multiple values.
# -----------------------------------

dance_styles = [
    "Hip-hop",
    "Salsa",
    "Classical",
    "Freestyle"
]

print("\nAvailable Dance Styles:")

for style in dance_styles:
    print("-", style)


# -----------------------------------
# 3. DICTIONARY
# Stores information using key-value pairs.
# -----------------------------------

configuration = {
    "song": "Blinding Lights",
    "dance_style": "Hip-hop",
    "energy": "High",
    "difficulty": "Beginner",
    "duration": 15
}

print("\nConfiguration:")
print(configuration)

print("\nSelected dance style:")
print(configuration["dance_style"])


# -----------------------------------
# 4. IF / ELSE
# Allows the program to make decisions.
# -----------------------------------

difficulty = "Beginner"

if difficulty == "Beginner":
    print("\nUse simple dance movements")
else:
    print("\nMore complex movements are allowed")


# -----------------------------------
# 5. MULTIPLE CONDITIONS
# -----------------------------------

energy = "High"
difficulty = "Beginner"

if energy == "High" and difficulty == "Beginner":
    print("Use simple movements with high energy")


# -----------------------------------
# 6. LOOPS
# Loops repeat something for each item.
# -----------------------------------

dance_moves = [
    "Step Touch",
    "Two Step",
    "Running Man",
    "Side Slide"
]

print("\nDance Moves:")

for move in dance_moves:
    print("-", move)


# -----------------------------------
# 7. FUNCTIONS
# Functions let us reuse code.
# -----------------------------------

def describe_dance(style, energy, difficulty):
    print("\nDance Description")
    print("-----------------")
    print("Dance style:", style)
    print("Energy:", energy)
    print("Difficulty:", difficulty)


describe_dance("Hip-hop", "High", "Beginner")


# -----------------------------------
# 8. SIMPLE DANCE PLAN GENERATOR
# -----------------------------------

def generate_dance_plan(style, energy, difficulty, duration):

    if difficulty == "Beginner":
        moves = [
            "Step Touch",
            "Two Step",
            "Running Man",
            "Side Slide"
        ]

    else:
        moves = [
            "Advanced Footwork",
            "Spin",
            "Body Isolation",
            "Fast Combination"
        ]

    print("\nDance Configuration")
    print("-------------------")
    print("Style:", style)
    print("Energy:", energy)
    print("Difficulty:", difficulty)
    print("Duration:", duration, "seconds")

    print("\nSuggested Moves")

    for move in moves:
        print("-", move)


generate_dance_plan(
    "Hip-hop",
    "High",
    "Beginner",
    15
)