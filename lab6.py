#cooler-multiplayer-battle-of-dices
import random

print("Welcome to Battle of Dices - Cooler Multiplayer Edition!")
print("Each player rolls a D20 and a D6. Highest sum wins the round!")
print("First player to 3 wins becomes the Champion!\n")

# ----- Game Setup -----
winning_score = 3
player_names = []
player_wins = []
player_rolls_history = []

# Dice functions (all in one file)
def rollD6():
    return random.randint(1, 6)

def rollD20():
    return random.randint(1, 20)

# Number of players
number_of_players = int(input("How many players? "))

# Get player names
for i in range(number_of_players):
    name = input(f"What is the name of player {i+1}? ")
    player_names.append(name)
    player_wins.append(0)               # initialize wins
    player_rolls_history.append([])     # initialize history

# ----- Game Loop -----
rounds = 0
gameover = False

while not gameover:
    rounds += 1   # round increments correctly
    print(f"\n--- Round {rounds} ---")
    input("Press ENTER to roll the dice...")

    # Rolls for each player
    current_rolls = []
    for i in range(number_of_players):
        total_roll = rollD20() + rollD6()
        current_rolls.append(total_roll)
        player_rolls_history[i].append(total_roll)
        print(f"{player_names[i]} rolled a total of: {total_roll}")

    # Determine highest roll
    max_roll = max(current_rolls)
    winners = []
    for j in range(number_of_players):
        if current_rolls[j] == max_roll:
            winners.append(player_names[j])
            player_wins[j] += 1

    # Show round result
    if len(winners) == 1:
        print(f" {winners[0]} wins this round! ")
    else:
        print(f" It's a tie! Winners: {winners}")

    # Show scoreboard
    print("\n Scoreboard:")
    for i in range(number_of_players):
        print(f"  {player_names[i]}: {player_wins[i]} wins")

    # Check for champion
    for z in range(number_of_players):
        if player_wins[z] >= winning_score:
            print(f"\n🏆 {player_names[z]} is the ultimate Battle of Dices Champion! 🏆")
            print(f"It took {rounds} rounds to win the game.")
            gameover = True
            break

# ----- Save Results -----
filename = input("\nEnter the filename to save the results: ")
with open(filename, 'w') as file:
    for round_number in range(rounds):
        file.write(f"Round {round_number+1}: ")
        rolls_str = ""
        for i in range(number_of_players):
            rolls_str += f"{player_names[i]} rolled {player_rolls_history[i][round_number]}"
            if i < number_of_players - 1:
                rolls_str += ", "
        file.write(rolls_str + "\n")

print(f"\n Results saved to '{filename}'")

#multiplayer-battle-of-dices