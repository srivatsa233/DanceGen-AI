# Day 3 - User Input and Validation for DanceGen AI

song = input("Enter song name: ").strip()

allowed_styles = ["hip-hop", "classical", "salsa", "freestyle"]

while True:
    dance_style = input(
        "Enter dance style (Hip-hop/Salsa/Classical/Freestyle): "
    ).strip().lower()

    if dance_style in allowed_styles:
        break

    print("Invalid dance style. Please try again.")


allowed_energy = ["low", "medium", "high"]

while True:
    energy = input(
        "Enter energy (Low/Medium/High): "
    ).strip().lower()

    if energy in allowed_energy:
        break

    print("Invalid energy level. Please try again.")


allowed_difficulties = [
    "beginner",
    "intermediate",
    "advanced"
]

while True:
    difficulty = input(
        "Enter difficulty level (Beginner/Intermediate/Advanced): "
    ).strip().lower()

    if difficulty in allowed_difficulties:
        break

    print("Invalid difficulty level. Please try again.")


allowed_durations = [15, 30, 60]

while True:
    duration = int(
        input("Enter duration (15/30/60 seconds): ")
    )

    if duration in allowed_durations:
        break

    print("Invalid duration. Please try again.")


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