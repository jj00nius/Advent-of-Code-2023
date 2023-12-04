""" TODO: 
- Model Part 2 to follow the same structure as Part 1
"""

import re

# Read lines from the input file and store them in a list
input = [line for line in open("day1/input.txt")]

values = []
with open("day1/input.txt") as file:
    for line in file:
        values.append(line.rstrip())

# Dict of for part two, mapping words to numerical representations
replaceNum = {
    "one": "o1e",
    "two": "t2o",
    "three": "t3e",
    "four": "f4r",
    "five": "f5e",
    "six": "s6x",
    "seven": "s7n",
    "eight": "e8t",
    "nine": "n9e"
}

# Function to replace words with numbers
def replaceWords(line):
    sum = 0
    # Iterate through the lines in the values list
    for line in values:
        # Replace words in line based on replaceNum dctionary
        for key, value in replaceNum.items():
            line = line.replace(key, value)
        # Find digits in modified line
        digitsOnly = re.sub("\D", "", line)
        # Add digits to the total sum
        sum += int(digitsOnly[0] + digitsOnly[-1])
    return sum

# Function which extracts a number from a string if it consists of digits
def get_num(string):
    if string.isdigit():
        return int(string)

# Function to process a line and return a result
def process(regex_str, line):
    # Find all occurrences of the regex in the line
    digits = re.findall(regex_str, line)
    
    # Extract the first and last numbers from the matched digits
    result = get_num(digits[0]) * 10 + get_num(digits[-1])
    
    # Return the calculated result
    return result

# Function to calculate the sum of processed lines
def part1():
    sum = 0
    for line in input:
        # Process each line and add the result to the sum
        sum += process("[0-9]", line)
    
    # Return the final sum
    return sum

# Print final result for part 1
print(part1())

# Print final result for part 2
print(replaceWords(input))
