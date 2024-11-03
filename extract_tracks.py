import json

# Load the JSON file from the defined path
with open('/Users/lolacopaev/Desktop/data_proj/response_sample.json', 'r') as file:
    data = json.load(file)

# Iterate through the items and print track and its details
for idx, item in enumerate(data.get('items', []), start=1):
    track_name = item.get('name', 'Unknown Track')
    artist_name = ', '.join([artist['name'] for artist in item.get('artists', [])]) or 'Unknown Artist'
    duration_ms = item.get('duration_ms', 'Unknown Duration')

    print(f"Track {idx}: {track_name}, Artist: {artist_name}, Duration (ms): {duration_ms}")

