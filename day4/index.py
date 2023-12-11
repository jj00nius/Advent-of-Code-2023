# Import dependencies
from collections import defaultdict

# Open and read file and split content into lines
lines = open("day4/input.txt").read().strip().split("\n")

# Function that checks for winning cards
def checkCards(lines):
    # Initialize variables
    p1 = 0 # Tracks winning cards
    line_counts = defaultdict(int) # Keep track of counts associated with line numbers

    # Loop through each line in the file
    for i, line in enumerate(lines):
        # Increment the count for the current line number to determine the card number
        line_counts[i] += 1

        # Split the winning numbers and my numbers by identifying the '|' character
        first_txt, rest_txt = line.split('|')

        # Split the first part of the line into the ID and card numbers by identifying the ':' character
        card = first_txt.split(':')

        # Convert card and rest values into lists of integers
        w_nums = [int(x) for x in card.split()] # Determine winning numbers
        card_nums = [int(x) for x in rest_txt.split()] # Determine card numbers

        # Compare winning numbers to my numbers by calculating the number of common elements between te two lists
        value = len(set(w_nums) & set(card_nums))

        # Update p1 based on the calculated value
        if value > 0:
            p1 += 2 ** (value - 1)
        
        # Update the count for lines in the range [i + 1, i + 1 + value]
        for j in range(value):
            line_counts[i + 1 + j] += line_counts[i]
    
    # P2: determine the sum of values in the defaultdict num
    p2 = sum(line_counts.values())

    # Return the result for p1 and p2
    return p1, p2

# Call the function and print results
print(checkCards(lines))
