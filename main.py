# Step 1: Welcome message
print("\n✨ Welcome to the Fairy Tale Mad Libs Game! ✨")
print("Fill in the blanks and create your magical story!")
print("=" * 60)

# Step 2: User input
hero_name = input("Enter a hero's name: ")
magical_place = input("Enter a magical place: ")
object_name = input("Enter a magical object: ")
adjective = input("Enter an adjective: ")
creature = input("Enter a magical creature (e.g., dragon, unicorn): ")
power = input("Enter a superpower: ")
villain_name = input("Enter a villain's name: ")

# Step 3: Story template
story = f"""
In a faraway land called {magical_place}, there lived a brave soul named {hero_name}.
One day, {hero_name} found a mysterious {object_name} that glowed with a {adjective} light.
Suddenly, a wild {creature} appeared and warned {hero_name} of danger.

With the power of {power}, {hero_name} set out on a quest to defeat the evil {villain_name}.
After an epic battle, peace was restored in {magical_place}, and {hero_name} became a legend forever.

The end 🌟
"""

# Step 4: Print the final story
print("\n📖 Here is your magical Mad Libs story:")
print("-" * 60)
print(story)
