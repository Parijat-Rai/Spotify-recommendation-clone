from pprint import pprint
import json
import pandas as pd

# Import json
data_path = "../data/First_1000.json"
raw_json = json.loads(open(data_path).read())

# Transform Data
playlists = raw_json["playlists"]
df = pd.json_normalize(playlists, record_path='tracks', meta=['name'])

# Output
df.to_csv("../data/raw_data.csv")