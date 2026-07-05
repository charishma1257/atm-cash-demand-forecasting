import pandas as pd
import folium

# Load ATM locations
locations = pd.read_csv("../data/atm_locations.csv")

# Load optimized route
with open("../data/optimized_route.txt", "r") as f:
    route = [line.strip() for line in f.readlines()]

# Create map
m = folium.Map(
    location=[
        locations["latitude"].mean(),
        locations["longitude"].mean()
    ],
    zoom_start=7
)

route_coords = []

# Add markers in route order
for i, atm in enumerate(route):

    row = locations[locations["atmId"] == atm].iloc[0]

    route_coords.append([row["latitude"], row["longitude"]])

    folium.Marker(
        [row["latitude"], row["longitude"]],
        popup=f"Stop {i+1}<br>{atm}",
        tooltip=f"{i+1}. {row['atmName']}",
        icon=folium.Icon(color="blue")
    ).add_to(m)

# Draw route
folium.PolyLine(
    route_coords,
    color="red",
    weight=4,
    opacity=0.8
).add_to(m)

# Save map
m.save("../atm_map.html")

print("ATM Route Map created successfully!")