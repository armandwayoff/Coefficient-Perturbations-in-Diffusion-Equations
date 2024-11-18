data = """

"""

# Extracting the second column
lines = data.strip().split('\n')
first_column = [float(line.split(' : ')[0]) for line in lines]
second_column = [float(line.split(' : ')[1]) for line in lines]

print(second_column)