import googlemaps, populartimes

api_key = "AIzaSyAIe4GOG3T6JA5QexlfJKTSP5QSsCckg-I"
client = googlemaps.Client(key=api_key)

def get_current_coordinates():
    location = client.geolocate()['location']
    lat,lng = location['lat'], location['lng']
    return lat,lng

info = client.places("grocery store")

def best_time(place_index, day):

    place_id = info["results"][place_index]["place_id"]

    days = {"Monday": 0, "Tuesday": 1, "Wednesday": 2, "Thursday": 3, "Friday": 4, "Saturday": 5, "Sunday": 6}
    data = populartimes.get_id(api_key, place_id)["populartimes"][days[day]]["data"]

    min_val = float('Inf')
    time = 0
    for i in range(len(data)):
        if data[i] != 0 and data[i] < min_val:
            min_val = data[i]
            time = i
    return time

def get_grocery():

    print(get_current_coordinates())

    result_dict = {}

    for i in range (len(info['results'])):
        place = info['results'][i]
        result_dict[place['name']] = i

    return result_dict
    """ place_index = int(input("Please choose a place (0 - %d): " % (len(info['results'])-1) ))

        place_id = info["results"][place_index]["place_id"]
        day = str(input("which day? "))"""

print(get_grocery())