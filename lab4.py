#python-revision-01.py
x = 5
y = 3
x = y

print (x)

x = 5
y = 3
y = x

print (y)

x = 10 
y = x 
x = 20

print(y)

x = 10
y = x
x = 20
y = x 
print(y)

x = "5"
y = 3
print (x * y)

x = 7
y = 2 
print("X/y")

x = 7
y = 2 
print(x/y)

x = 12 
y = 5
print(x//y)

x = 7
y = 2
print(x%y)

x = 2
y = "3"
print(str(x)+y)

x = "2"
y = "3"
print(x+y)

x = 10
if x > 5:
    print("big")
else:
    print("small")

x = 100
if x > 5:
        print("big")
else:
        print("small")

x = -10
if x > 5:
    print("big")
else:
    print("small")

x = 3
if x == 5:
    print("five")
elif x <= 5:
     print("less")
else:
     print("more")

x = 3
if x == 5:
    print("five")
elif x <= 5:
        print("less")
else:
        print("more")

x = 5
if x == 5:
    print("five")
elif x <= 5:
    print("less")
else:
    print("more")

x = 10
y = 2
if x > 20:
     print("A")
elif y>5:
         print("B")
elif x > 0:
         print("C")
else:
         print("D")

x = 10
y = 20
if x > 20:
    print("A")
elif y > 5:
    print("B")
elif x > 0:
    print("C")
else:
    print("D")

x = -5
y = -3
if x > 20:
    print("A")
elif y > 5:
    print("B")
elif x > 0:
    print("C")
else:
    print("D")

names = ["Laura", "Yasmin"]
for each_name in names:
    print(each_name)


names = ["Laura", "Yasmin"]
# Add your code here
new_name = input("Enter a name to add to the list: ")

# add the new name to the list
names.append(new_name)

# print all names
for each_name in names:
    print(each_name)

#battle-of-dices-not-rigged
import random

print("🎲 Welcome to Battle of Dices! 🎲")
print("Each player rolls a D20. First to 3 wins is the champion!")

# Track score
player1_wins = 0
player2_wins = 0
round_number = 1

# Lists to store all rolls
player1_rolls = []
player2_rolls = []

# Play game until someone reaches 3 wins
while player1_wins < 3 and player2_wins < 3:
    print(f"\n--- Round {round_number} ---")

    input("Press ENTER to roll the dice for Player 1...")
    player1_roll = random.randint(1, 20)
    print("Player 1 rolled:", player1_roll)

    input("Press ENTER to roll the dice for Player 2...")
    player2_roll = random.randint(1, 20)
    print("Player 2 rolled:", player2_roll)

    # Store rolls
    player1_rolls.append(player1_roll)
    player2_rolls.append(player2_roll)

    # Determine round winner
    if player1_roll > player2_roll:
        print("Player 1 wins this round!")
        player1_wins += 1
    elif player2_roll > player1_roll:
        print("Player 2 wins this round!")
        player2_wins += 1
    else:
        print("⚔️ It's a tie! ⚔️")

    print(f"Score -> Player 1: {player1_wins} | Player 2: {player2_wins}")
    round_number += 1

# Declare overall winner
if player1_wins == 3:
    print("\n Player 1 is the ultimate Battle of Dices Champion!")
else:
    print("\n Player 2 dominates and wins the Battle of Dices!")

print(f"It took {round_number - 1} rounds to finish the game!")

# Print game summary table
print("\n Game Summary")
print("-" * 50)
print(f"{'Round':<8}{'Player 1 (D20)':<18}{'Player 2 (D20)':<18}")
print("-" * 50)
for i in range(len(player1_rolls)):
    print(f"{i+1:<8}{player1_rolls[i]:<18}{player2_rolls[i]:<18}")
print("-" * 50)

# Save summary to a file
filename = input("\nEnter a filename to save the summary (e.g. summary.txt): ")
with open(filename, "w") as f:
    f.write("Battle of Dices – Game Summary\n")
    f.write("-" * 50 + "\n")
    f.write(f"{'Round':<8}{'Player 1 (D20)':<18}{'Player 2 (D20)':<18}\n")
    f.write("-" * 50 + "\n")
    for i in range(len(player1_rolls)):
        f.write(f"{i+1:<8}{player1_rolls[i]:<18}{player2_rolls[i]:<18}\n")
    f.write("-" * 50 + "\n")

print(f"\n Summary saved to {filename}")

#battle-of-dices-bad-not-rigged