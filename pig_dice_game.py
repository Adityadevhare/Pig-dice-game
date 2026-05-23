import random

# Constants
MIN_ROLL = 1
MAX_ROLL = 6
TARGET_SCORE = 50
MIN_PLAYERS = 2
MAX_PLAYERS = 4

def roll():
    """Roll a single die."""
    return random.randint(MIN_ROLL, MAX_ROLL)

def get_player_count():
    """Validate and return number of players."""
    while True:
        try:
            players = int(input(f"Enter number of players ({MIN_PLAYERS}-{MAX_PLAYERS}): "))
            if MIN_PLAYERS <= players <= MAX_PLAYERS:
                return players
            print(f"Must be between {MIN_PLAYERS}-{MAX_PLAYERS}.")
        except ValueError:
            print("Invalid input. Enter a number.")

def player_turn(player_num, total_score):
    """Execute single player's turn. Returns score gained this turn."""
    print(f"\n--- Player {player_num} Turn ---")
    print(f"Total score: {total_score}")
    
    turn_score = 0
    while True:
        if input("Roll? (y/n): ").lower() != "y":
            break
        
        value = roll()
        print(f"Rolled: {value}")
        
        if value == MIN_ROLL:
            print("💥 Rolled a 1! Turn lost!")
            turn_score = 0
            break
        
        turn_score += value
        print(f"Turn score: {turn_score}")
    
    return turn_score

def play_game():
    """Main game loop."""
    players = get_player_count()
    player_scores = [0] * players
    
    while max(player_scores) < TARGET_SCORE:
        for idx in range(players):
            turn_gain = player_turn(idx + 1, player_scores[idx])
            player_scores[idx] += turn_gain
            print(f"New total: {player_scores[idx]}\n")
    
    # Announce winner
    winner_idx = player_scores.index(max(player_scores))
    print(f"\n🎉 Player {winner_idx + 1} wins with {player_scores[winner_idx]} points!")

if __name__ == "__main__":
    play_game()