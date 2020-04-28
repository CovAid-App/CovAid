import googlemaps, populartimes 

api_key = "AIzaSyAIe4GOG3T6JA5QexlfJKTSP5QSsCckg-I"
client = googlemaps.Client(key=api_key)

def get_user_coordinates():
    location = client.geolocate()['location']
    lat,lng = location['lat'], location['lng']
    return lat,lng

def get_distance(coords1, coords2):
    '''
    Returns the distance between two points in km, as a string.
    '''

    dist_info = client.distance_matrix(coords1, coords2, "driving")
    return dist_info['rows'][0]['elements'][0]['distance']['text']

info = client.places("grocery store")
results = info['results']

user_coords = get_user_coordinates()

print(results[0].keys())

for i in range (len(results)):
    place = results[i]
    location = place['geometry']['location']
    lat,lng = location['lat'], location['lng']
    distance = get_distance(user_coords, (lat,lng))



    print("%-2d - %s (%s)"%(i,place['name'],distance))

place_index = int(input("Please choose a place (0 - %d): " % (len(results)-1) ))
selected_place = results[place_index]
place_id = selected_place['place_id']

popular_times = populartimes.get_id(api_key, place_id)

print(popular_times['populartimes'])