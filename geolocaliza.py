from geopy.geocoders import Nominatim

def get_location_name(latitude, longitude):
    try:
        geolocator = Nominatim(user_agent="myGeocoder")
        location = geolocator.reverse((latitude, longitude))
        return location.address
    except Exception as e:
        return str(e)

latitude = -19.8362634  # Latitude desejada
longitude = 34.8608645  # Longitude desejada

location_name = get_location_name(latitude, longitude)

if location_name:
    print("Nome da localização:", location_name)
else:
    print("Não foi possível obter o nome da localização.")
