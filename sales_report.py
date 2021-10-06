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

    salesperson = entries[0]
    melons = int(entries[2])

    if salesperson in salespeople:
        position = salespeople.index(salesperson)

        melons_sold[position] += melons
    else:
        salespeople.append(salesperson)
        melons_sold.append(melons)


for i in range(len(salespeople)):
    print(f'{salespeople[i]} sold {melons_sold[i]} melons')
