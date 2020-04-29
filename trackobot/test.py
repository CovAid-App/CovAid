import trackobot
from datetime import datetime

user_coords = trackobot.get_user_coordinates()

query = input("Where do you want to go? ")

# take the first ten results
results = trackobot.maps_search(query)[:10]
distances_info = trackobot.get_distances_info([user_coords for each in results], [trackobot.get_place_coordinates(place) for place in results])

for place_index in range(len(results)):
    print(trackobot.get_distance(distances_info, place_index))

'''

for i in range (len(results)):
    place = results[i]
    location = place['geometry']['location']
    lat,lng = location['lat'], location['lng']
    # TODO check if the method allows multiple distance calculations per api call
    # hide distance for now to prevent overdoing api calls
    # distance = trackobot.get_distance(user_coords, (lat,lng))

    print("%-2d - %s (%s)"%(i,place['name'], "dist"))

place_index = int(input("Please choose a place (0 - %d): " % (len(results)-1) ))
selected_place = results[place_index]
place_id = selected_place['place_id']



popular_times_info = trackobot.get_popular_times_info(place_id)

# 0: Monday, up to 6: Sunday
weekday_index = datetime.today().weekday()

print(trackobot.popular_times_on_weekday(popular_times_info, weekday_index))
'''