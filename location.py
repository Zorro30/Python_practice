from geopy.geocoders import Nominatim

geolocator = Nominatim()

lc = "Oregon Coast"

place = geolocator.geocode(lc)
print (place.raw)