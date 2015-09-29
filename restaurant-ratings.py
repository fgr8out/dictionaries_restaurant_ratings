# your code goes here
restaurant_scores = open("scores.txt")
restaurant_data ={}
for line in restaurant_scores:
    stripped_line = line.strip()
    split_line = stripped_line.split(":")
    restaurant_name = split_line[0]
    restaurant_rating = split_line[1]
    restaurant_data[restaurant_name] = restaurant_rating

sorted_restaurant_data = sorted(restaurant_data)
print sorted_restaurant_data
print restaurant_data
for name in sorted_restaurant_data:
    print " %s is rated at %s." % (name, restaurant_data[name])

