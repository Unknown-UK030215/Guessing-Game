import socket
import json

# Host: Changeable, check IPConfig in the Command Line Interface
host = "192.168.68.107"
port = 7777

# Function: Play Game
def play_game():
    s = socket.socket()
    s.connect((host, port))

    # Receive: Banner name
    data = s.recv(1024)
    print("\n== Guessing Game (Enhanced) ==\n")

    # Print: Banner name
    print(data.decode().strip())

    # loop: While (Endless unless close)
    while True:
        # Get: User input
        user_input = input("Input: ").strip()
        s.sendall(user_input.encode())

        # Add: Spacing (after the input)
        print()

        # Reply: Receive
        reply = s.recv(1024).decode().strip()

        # Conditional: Reply's
        if "Correct" in reply:
            print(reply)
            leaderboard_data = s.recv(1024).decode()  # Receive leaderboard data from server

            # Handle empty or unexpected data
            if not leaderboard_data:
                print("Error: Empty or unexpected leaderboard data received.")
                break
            
            try:
                leaderboard = json.loads(leaderboard_data)
                if isinstance(leaderboard, list):  # Ensure it's a list before printing
                    print_leaderboard(leaderboard)
                else:
                    print("Error: Unexpected leaderboard data format.")
            except json.JSONDecodeError:
                pass  # Silently handle JSON decode error
            break

        # Handle invalid input
        elif "Invalid" in reply:
            print(reply)
            continue

        print(reply)
        continue

    # Close: Program
    s.close()

# Function: Print Leaderboard
def print_leaderboard(leaderboard):
    print("\n== Leaderboard ==\n")
    for rank, player in enumerate(leaderboard, start=1):
        print(f"Rank {rank}:")
        print(f"Name: {player['name']}")
        print(f"Score: {player['score']}")
        print(f"Tries: {player['tries']}")
        print(f"Difficulty: {player['difficulty']}\n")

# Loop: While (Endless unless close)
while True:
    play_game() # If Yes and If No Break
    repeat = input("\nDo you want to play again? (yes/no): ").strip().lower()
    if repeat != "yes":
        break
