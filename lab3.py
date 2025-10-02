#lab-battle-of-dices
import random

print("🎲 Welcome to Battle of Dices! 🎲")

# Variables to keep track of the score:
player1_wins = 0
player2_wins = 0

# Round 1
input("\nPress ENTER to roll the dice...")

player1_roll = random.randint(1, 6)

print("Player 1 rolled: ", player1_roll)

player2_roll = random.randint(1, 6)

print("Player 2 rolled: ", player2_roll)

input("\nPress ENTER to continue...")

# So far so good right? But how to check who got the highest roll?

if player1_roll > player2_roll:
    player1_wins += 1
    print("Player 1 wins this round!")
    print("Because ", player1_roll," is greater than ", player2_roll)
elif player1_roll == player2_roll:
    print("Amaaazzinng! This round has a tie!")
else:
    player2_wins = player2_wins + 1
    print("Player 2 wins this round!")
    print("Because ", player2_roll," is greater than ", player1_roll)


# We can print the game score:
print("The game score is Player1 ", player1_wins, " vs. ", player2_wins, " Player 2.")

# Now we need to check if either player won.
if player1_wins == 3:
    print("Player 1 is the newest Battle of Dices Champion! ")
elif player2_wins == 3:
    print("Player 2 is the newest Battle of Dices Champion! ")
else:
    print("This heated Battle of Dices is still going on! Who will win in the end? ")


#battle-ofdices-cooler
from dice import rollD6, rollD20

print("# Welcome to Battle of Dices – Cooler Edition! #")
print("Each player rolls a D20 and a D6. Highest sum wins the round!")

player1_wins = 0
player2_wins = 0
round_number = 1

while player1_wins < 3 and player2_wins < 3:
    print(f"\n--- Round {round_number} ---")
    input("Press ENTER to roll the dice...")

    # Roll two dice per player
    player1_roll = rollD20() + rollD6()
    player2_roll = rollD20() + rollD6()

    print(f"Player 1 rolled a total of: {player1_roll}")
    print(f"Player 2 rolled a total of: {player2_roll}")

    if player1_roll > player2_roll:
     print("# Player 1 wins this round! #")
     player1_wins += 1

     elif player2_roll > player1_roll:
          print("# Player 2 wins this round! #")
          player2_wins += 1
     else:
          print("⚔️ It's a tie! ⚔️")

     print(f"Score -> Player 1: {player1_wins} | Player 2: {player2_wins}")
     round_number += 1

# Declare the winner
if player1_wins == 3:
   print(f"\n## Player 1 is the ultimate Battle of Dices Champion! ##")
   print(f"It took {round_number - 1} rounds to win the game.")
else:
   print(f"\n## Player 2 dominates and wins the Battle of Dices! ##")
   print(f"It took {round_number - 1} rounds to win the game.")


#battle-of-dices-bad
import random

print("🎲 Welcome to Battle of Dices! 🎲")
print("Each player rolls a D20. First to 3 wins is the champion!")

# Variables to keep track of the score
player1_wins = 0
player2_wins = 0
round_number = 1

# Keep playing rounds until someone reaches 3 wins
while player1_wins < 3 and player2_wins < 3:
    print(f"\n--- Round {round_number} ---")
    input("Press ENTER to roll the dice...")

    # Roll dice for both players
    player1_roll = random.randint(1, 20)
    player2_roll = random.randint(1, 20)

    print("Player 1 rolled:", player1_roll)
    print("Player 2 rolled:", player2_roll)

    # Determine winner of the round
    if player1_roll > player2_roll:
        print("Player 1 wins this round!")
        player1_wins += 1
    elif player2_roll > player1_roll:
        print("Player 2 wins this round!")
        player2_wins += 1
    else:
        print("⚔️ It's a tie! ⚔️")

    # Print current score
    print(f"Score -> Player 1: {player1_wins} | Player 2: {player2_wins}")

    round_number += 1

# Declare overall winner
if player1_wins == 3:
    print("\n Player 1 is the ultimate Battle of Dices Champion!")
    print(f"it took {round_number - 1} rounds to win the game.")
else:
    print("\n Player 2 dominates and wins the Battle of Dices!")
    print(f"it took {round_number - 1} rounds to win the game.")
    
#battle-of-dices-better
import random

print("🎲 Welcome to Battle of Dices! 🎲")
print("Each player rolls a D20. First to 3 wins is the champion!")

# Variables to keep track of the score
player1_wins = 0
player2_wins = 0
round_number = 1

# Keep playing rounds until someone reaches 3 wins
while player1_wins < 3 and player2_wins < 3:
    print(f"\n--- Round {round_number} ---")
    input("Press ENTER to roll the dice...")

    # Roll dice for both players
    player1_roll = random.randint(1, 20)
    player2_roll = random.randint(1, 20)

    print("Player 1 rolled:", player1_roll)
    print("Player 2 rolled:", player2_roll)

    # Determine winner of the round
    if player1_roll > player2_roll:
        print("Player 1 wins this round!")
        player1_wins += 1
    elif player2_roll > player1_roll:
        print("Player 2 wins this round!")
        player2_wins += 1
    else:
        print("⚔️ It's a tie! ⚔️")

    # Print current score
    print(f"Score -> Player 1: {player1_wins} | Player 2: {player2_wins}")

    round_number += 1

# Declare overall winner
if player1_wins == 3:
    print("\n Player 1 is the ultimate Battle of Dices Champion!")
    print(f"it took {round_number - 1} rounds for player 1 to win the game!")
else:
    print("\n Player 2 dominates and wins the Battle of Dices!")
    print(f"It took {round_number - 1} rounds for player 2 to win the game!")