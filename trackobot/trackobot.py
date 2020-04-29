import googlemaps, populartimes

api_key = "AIzaSyAIe4GOG3T6JA5QexlfJKTSP5QSsCckg-I"
client = googlemaps.Client(key=api_key)

def get_user_coordinates():
    location = client.geolocate()['location']
    lat,lng = location['lat'], location['lng']
    return lat,lng

def get_place_coordinates(place):
    return place['geometry']['location']

def get_distances_info(origins, destinations):
    '''

    '''
    dist_info = client.distance_matrix(origins, destinations, "driving")
    
    return dist_info

def get_distance(distances_info, index):
    return distances_info['rows'][index]['elements'][0]['distance']['text']

def get_popular_times_info(place_id):
    '''
    Returns JSON of popular times for the given place.
    '''
    return populartimes.get_id(api_key, place_id)['populartimes']

def popular_times_on_weekday(popular_times_info, weekday_index):
    '''
    Returns the popular times of a place for a certain weekday.
    '''
    return popular_times_info[weekday_index]['data']

def get_best_time_to_visit(popular_times_on_weekday):
    '''
    Gets the hour of minimum popularity for the given weekday.
    '''
    return min(pop for pop in popular_times_on_weekday if pop > 0)

def maps_search(query):
    '''
    Searches for nearby places given a query.
    '''
    info = client.places(query)
    return info['results']