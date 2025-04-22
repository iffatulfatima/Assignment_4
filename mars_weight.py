# Prompts the user for a weight on Earth and a planet,
# then prints the equivalent weight on that planet.

# Gravitational constants
MERCURY_GRAVITY = 0.376
VENUS_GRAVITY = 0.889
MARS_GRAVITY = 0.378
JUPITER_GRAVITY = 2.36
SATURN_GRAVITY = 1.081
URANUS_GRAVITY = 0.815
NEPTUNE_GRAVITY = 1.14

def main():
    # Step 1: Get user weight on Earth
    earth_weight = float(input("Enter a weight on Earth: "))

    # Step 2: Get user planet
    planet = input("Enter a planet (e.g., Mars, Venus, Jupiter...): ")

    # Step 3: Select gravity constant
    if planet == "Mercury":
        gravity_constant = MERCURY_GRAVITY
    elif planet == "Venus":
        gravity_constant = VENUS_GRAVITY
    elif planet == "Mars":
        gravity_constant = MARS_GRAVITY
    elif planet == "Jupiter":
        gravity_constant = JUPITER_GRAVITY
    elif planet == "Saturn":
        gravity_constant = SATURN_GRAVITY
    elif planet == "Uranus":
        gravity_constant = URANUS_GRAVITY
    else:
        gravity_constant = NEPTUNE_GRAVITY  # Default case

    # Step 4: Calculate planetary weight
    planetary_weight = earth_weight * gravity_constant
    rounded_planetary_weight = round(planetary_weight, 2)

    # Step 5: Show result
    print("The equivalent weight on " + planet + ": " + str(rounded_planetary_weight))

# Run the program
if __name__ == '__main__':
    main()
