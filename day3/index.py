import re

# Read lines from input file and store them in a list
lines = [x for x in open("input.txt").read().strip().split("\n")]

def engineSchematic(lines):
    # Initialize a variable to store the sum of part numbers
    num_coords = []
    symbol_coords = []
    # Iterate through each line in the input
    for x, line in enumerate(lines):
        nums = re.finditer(r'\d+', line)
        for num in nums:
            coords = []
            for i in range(len(num.group())):
                coords.append((x, num.start() + i))
            num_coords.append([num.group(), coords])
        symbols = re.finditer(r'[^\d+]', line)
        for symbol in symbols:
            symbol_coords.append([symbol.group(), (x, symbol.start())])
    

print(engineSchematic(lines))