import googlemaps, populartimes

api_key = "AIzaSyAIe4GOG3T6JA5QexlfJKTSP5QSsCckg-I"
client = googlemaps.Client(key=api_key)
print(client.geolocate()['location'])

"""def get_current_coordinates():
    location = client.geolocate()['location']
    lat,lng = location['lat'], location['lng']
    return lat,lng"""

def get_info(lat, lng):

    info = client.places("grocery store", (lat, lng))
    return info

def best_time(info, place_index, day):

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


def get_grocery(lat, lng):

    info = get_info(lat, lng)

    result_dict = {}

    for i in range (len(info['results'])):
        place = info['results'][i]
        result_dict[place['name']] = i

    return result_dict, info