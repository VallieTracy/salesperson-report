"""Generate sales report showing total melons each salesperson sold."""

# Creating global variables
# Empty lists which will store names of salespeople and another list which will store # of melons sold
# Might want to make a dictionary instead of two separate lists where person is key and value is melons sold
salespeople = []
melons_sold = []

# Opening the file and storing it in a variable called 'f'
f = open('sales-report.txt')

# Loop thru every line in the file 'f'
for line in f:
    # Strip each line of white space
    line = line.rstrip()
    # Split the line at '|' character and store it in a new variable 'entries'
    entries = line.split('|')

    # Definig the salespeople as entries at index 0 and placing them in a variable called salesperson
    # Similar for melons, and changing data type to integer
    salesperson = entries[0]
    melons = int(entries[2])

    # If the salesperson is already in salespeople list created above:
    if salesperson in salespeople:
        # Locating the index of salesperson within salespeople list created above and storing in variable called 'position'
        position = salespeople.index(salesperson)
        # Using position, finding the corresponding position in melons_sold list and adding melons value to it
        melons_sold[position] += melons
    
    # Otherwise, add the salesperson to salespeople list created above and similarly for melons_sold
    else:
        salespeople.append(salesperson)
        melons_sold.append(melons)


for i in range(len(salespeople)):
    print(f'{salespeople[i]} sold {melons_sold[i]} melons')
