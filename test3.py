import requests

API_KEY = 'k6AF02uec6xQEzvhF-XB_wdqffYPoVNOjApiS2NK6jY'
latitude = 12.916517
longitude = 79.132500

# Set up API endpoint and parameters
url = f"https://discover.search.hereapi.com/v1/discover?apiKey={API_KEY}&at={latitude},{longitude}&q=veterinary clinic"

# Send the HTTP GET request
response = requests.get(url)

# Parse the JSON response
data = response.json()

# Check if results were found
if 'items' in data:
    # Get the number of police stations
    num_police_stations = len(data['items'])

    # Print the number of police stations
    print("Number of Police Stations:", num_police_stations)
    for i in range(len(data['items'])):
        print(data['items'][i]['position'])
else:
    print("No police stations found nearby.")
