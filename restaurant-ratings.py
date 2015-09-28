# your code goes here
restaurant_scores = open("scores.txt")
restaurant_data ={}
for line in restaurant_scores:
    stripped_line = line.strip()
    split_line = stripped_line.split(":")
#    restaurant_name = split_line[0]
    restaurant_data(split_line[0]) = split_line[1]

print resta