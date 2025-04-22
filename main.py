import random

NUM_ROUNDS = 5

def main():
    print("🎲 Welcome to the High-Low Game!")
    print('--------------------------------')

    your_score = 0

    for i in range(NUM_ROUNDS):
        print(f"🔁 Round {i + 1} of {NUM_ROUNDS}")
        print("----------------------------")

        computer_num = random.randint(1, 100)
        your_num = random.randint(1, 100)
        print("Your number is:", your_num)

        choice = input("Do you think your number is HIGHER or LOWER than the computer's? ").strip().lower()

        while choice not in ("higher", "lower"):
            choice = input("❗ Please enter either 'higher' or 'lower': ").strip().lower()

        higher_and_correct = choice == "higher" and your_num > computer_num
        lower_and_correct = choice == "lower" and your_num < computer_num

        if higher_and_correct or lower_and_correct:
            print(f"✅ You were right! The computer's number was {computer_num}.")
            your_score += 1
        else:
            print(f"❌ Incorrect. The computer's number was {computer_num}.")

        print(f"⭐ Current Score: {your_score}/{i + 1}")
        print()

    print("🎯 Game Over!")
    print(f"🏁 Final Score: {your_score}/{NUM_ROUNDS} ({(your_score / NUM_ROUNDS) * 100:.0f}%)")

    if your_score == NUM_ROUNDS:
        print("🎉 Wow! You played perfectly!")
    elif your_score > NUM_ROUNDS // 2:
        print("👍 Good job, you played really well!")
    else:
        print("🙁 Better luck next time!")

if __name__ == "__main__":
    main()
