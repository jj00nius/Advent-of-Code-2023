
from collections import defaultdict

# Read lines from input file and store them in a list
lines = [x for x in open("day2/input.txt").read().strip().split("\n")]

# Function that validates games based on input lines
def checkGames(lines):
    # Initialise counters
    p1 = 0
    p2 = 0

    # Iterate through each line in the input
    for line in lines:
        # Extract game id from the current line
        gameID = int(line.split(":")[0].split(" ")[1])
        # remove game id from the line
        line = line.split(":")[1]
        # Flag determining whether the game is possible
        possible = True
        # Dictionary tracking the minimum number of counters for each colour
        minCounter = defaultdict(int)

        # Iterate through each string in the line
        for bag in line.split(";"):
            # Dictionary tracking the count of counters for each colour
            counter = defaultdict(int)
            
            # Process each colour and count from the bag
            for rev in bag.split(", "):
                rev = rev.strip()
                counter[rev.split(" ")[1]] += int(rev.split(" ")[0])
            
            # Update the minCounter dictionary with the maximum counts for each colour
            for colour, count in counter.items():
                minCounter[colour] = max(minCounter[colour], count)
            
            # Check if the counts for red, green, and blue are within limits
            if not (counter["red"] <= 12 and counter["green"] <= 13 and counter["blue"] <= 14):
                possible = False
        
        # If the game is possible, add the game ID to part 1 counter
        if possible:
            p1 += gameID

        # Calculate the product of minimum counts for red, green, and blue for part 2
        p2 += minCounter["red"] * minCounter["green"] * minCounter["blue"]

    # Return the results for both parts
    return p1, p2

# Print the result of checking games
print(checkGames(lines))