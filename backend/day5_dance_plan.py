# Dance move database

dance_moves = {
    "hip-hop": {
        "beginner": [
            "Step Touch",
            "Two Step"
        ],
        "intermediate": [
            "Running Man",
            "Side Slide",
            "Body Bounce"
        ],
        "advanced": [
            "Body Wave",
            "Spin",
            "Fast Footwork"
        ]
    },

    "salsa": {
        "beginner": [
            "Basic Step",
            "Side Basic"
        ],
        "intermediate": [
            "Right Turn",
            "Cross Body Lead"
        ],
        "advanced": [
            "Double Turn",
            "Advanced Combination"
        ]
    },

    "classical": {
        "beginner": [
            "Basic Posture",
            "Hand Gesture"
        ],
        "intermediate": [
            "Side Step",
            "Turn"
        ],
        "advanced": [
            "Complex Turn",
            "Advanced Expression"
        ]
    },

    "freestyle": {
        "beginner": [
            "Step Touch",
            "Side Slide"
        ],
        "intermediate": [
            "Body Wave",
            "Spin"
        ],
        "advanced": [
            "Fast Combination",
            "Floor Move"
        ]
    }
}


# Get moves based on style and difficulty

def get_moves(style, difficulty):
    return dance_moves[style][difficulty]


# Generate dance plan

def generate_dance_plan(config):

    style = config["style"]
    difficulty = config["difficulty"]
    energy = config["energy"]

    moves = get_moves(style, difficulty)

    if energy == "low":
        move_count = 1

    elif energy == "medium":
        move_count = 2

    else:
        move_count = len(moves)

    selected_moves = moves[:move_count]

    plan = {
        "song": config["song"],
        "style": style,
        "energy": energy,
        "difficulty": difficulty,
        "duration": config["duration"],
        "moves": selected_moves
    }

    return plan


# Sample user configuration

config = {
    "song": "Blinding Lights",
    "style": "hip-hop",
    "energy": "high",
    "difficulty": "beginner",
    "duration": 15
}


# Generate dance plan

dance_plan = generate_dance_plan(config)


# Display dance plan

print("\n--- Dance Plan ---")

print("Song:", dance_plan["song"])
print("Style:", dance_plan["style"])
print("Energy:", dance_plan["energy"])
print("Difficulty:", dance_plan["difficulty"])
print("Duration:", dance_plan["duration"], "seconds")

print("\nMoves:")

for move in dance_plan["moves"]:
    print("-", move)