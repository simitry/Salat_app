import requests
import json

# important -----------------------
date = "26-01-2025"
endpoint = "timings"

latitude = "31.628674"      # lat and lon of Marrakech
longitude = "-7.992047"

params = {
    "latitude": latitude,
    "longitude": longitude
}
#----------------------------------

response = requests.get(f"https://api.aladhan.com/v1/{endpoint}/{date}", params)

data = response.json()

# with open("salat.json", "w") as file:
#     json.dump(response.json(), file, indent=4)

# print("Data written to salat.json")

salat = data.get("data" , {})
timing = salat.get("timings",{})

# print(timing["Fajr"])

