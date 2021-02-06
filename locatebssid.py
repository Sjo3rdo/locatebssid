import urllib.request
import json
import webbrowser

___author___ = 'D4rkC00d3r'

bssid = input('Enter a BSSID: ')  # Mac address of AP you want to locate
api_uri = 'https://api.mylnikov.org/geolocation/wifi?v=1.1&data=open&bssid='  # Api endpoint for database.
map_url = 'https://www.openstreetmap.org/search?query={}%2C%20{}#map=17/{}/{}&layers=D'
# Example of a MAC address; 00:0C:42:1F:65:E9 this can be used for testing.


def mappin(lat, lon):
    while True:
        confirm = input('Show on map? (Y)es or (N)o: ')
        if 'Y' in confirm:
            webbrowser.open(map_url.format(lat, lon, lat, lon))
            return
        else:
            break


def results():
    if 'desc' in data:
        print(data['desc'])
    else:
        print('Device has last been seen at:')
        print('Lat: {0}'.format(data['data']['lat']))
        print('Lon: {0}'.format(data['data']['lon']))
        print('Meter accuracy: {0}'.format(data['data']['range']))
        lat = data['data']['lat']
        lon = data['data']['lon']
        mappin(lat, lon)


# used to write the results of the api call to a .json file.
with urllib.request.urlopen(api_uri + bssid) as url:
    data = json.loads(url.read().decode())
    json_str = json.dumps(data)
    with open('locatebssid.json', 'w') as f:
        json.dump(data, f, indent=4)
        results()
