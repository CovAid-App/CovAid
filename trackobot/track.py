import googlemaps, populartimes 

api_key = "AIzaSyAIe4GOG3T6JA5QexlfJKTSP5QSsCckg-I"
client = googlemaps.Client(key=api_key)

def get_current_coordinates():
    location = client.geolocate()['location']
    lat,lng = location['lat'], location['lng']
    return lat,lng

info = client.places("grocery store")

print(get_current_coordinates())

print(info['results'][0].keys())

for i in range (len(info['results'])):
    place = info['results'][i]
    print("%-2d -"%i, place['name'])

place_index = int(input("Please choose a place (0 - %d): " % (len(info['results'])-1) ))