# Geo Coding - Mapping an address to a Coordinates
# Reverse Geo Coding - Cordinates to address

# Nominatim is one of the Geocoders available
# There's a bug with Nominatim and so using GoogleV3
from geopy.geocoders import Nominatim
from geopy.geocoders import GoogleV3
nom = GoogleV3(scheme = "http")
from pandas import read_csv
import traceback

try :
    # nom=Nominatim(user_agent='my-app')
    nom = GoogleV3(scheme="http")

    n=nom.geocode('Some Non Existent Address')
    print("Non Existent Address returned:", n)

    n=nom.geocode('3995 23rd St, San Francisco, CA 94114')
    print(n)
    print(type(n))
    print(n.latitude, " - " , n.longitude, " - ", n.altitude)


    df=read_csv('../assets/sample.csv')
    df["Location"]=df["Address"]+","+df["City"]+","+df["State"]
    # df["Location"]
    df["GeoCode"]=df["Location"].apply(nom.geocode)
    df["Latitude"]=df["GeoCode"].apply(lambda x : x.latitude if x != None else "NA")
    df["Lngitude"]=df["GeoCode"].apply(lambda x : x.longitude if x != None else "NA")
    print(df)
except Exception as e:
    print('Encountered an Exception : ' + traceback.print_exc(e))

