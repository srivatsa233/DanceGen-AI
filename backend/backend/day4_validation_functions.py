# Day 4 - Validation Functions for DanceGen AI


def get_song():
    song = input("Enter song name: ").strip()

    while song == "":
        print("Song name cannot be empty.")
        song = input("Enter song name: ").strip()

    return song


def get_choice(prompt, allowed_values):
    while True:
        value = input(prompt).strip().lower()

        if value in allowed_values:
            return value

        print("Invalid choice. Please try again.")


def get_duration():
    allowed_durations = [15, 30, 60]

    while True:
        try:
            duration = int(
                input("Enter duration (15/30/60 seconds): ")
            )

            if duration in allowed_durations:
                return duration

            print("Invalid duration. Choose 15, 30, or 60.")

        except ValueError:
            print("Please enter a number.")


allowed_styles = [
    "hip-hop",
    "classical",
    "salsa",
    "freestyle"
]

allowed_energy = [
    "low",
    "medium",
    "high"
]

allowed_difficulties = [
    "beginner",
    "intermediate",
    "advanced"
]


song = get_song()

dance_style = get_choice(
    "Enter dance style (Hip-hop/Salsa/Classical/Freestyle): ",
    allowed_styles
)

energy = get_choice(
    "Enter energy (Low/Medium/High): ",
    allowed_energy
)

difficulty = get_choice(
    "Enter difficulty (Beginner/Intermediate/Advanced): ",
    allowed_difficulties
)

duration = get_duration()


configuration = {
    "song": song,
    "style": dance_style,
    "energy": energy,
    "difficulty": difficulty,
    "duration": duration
}


print("\nYour Configuration")
print("------------------")

print("Song:", song)
print("Dance Style:", dance_style)
print("Energy:", energy)
print("Difficulty:", difficulty)
print("Duration:", duration, "seconds")

print("\nConfiguration Dictionary:")
print(configuration)