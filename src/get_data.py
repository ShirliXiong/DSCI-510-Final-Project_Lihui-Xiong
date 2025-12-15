# %%
import requests
import pandas as pd
url = "https://data.cityofnewyork.us/resource/usep-8jbt.json"

params = {
    "$select": "borough, neighborhood, building_class_category, "
               "land_square_feet, gross_square_feet, sale_price, sale_date",
    "$where": "sale_price > 100000 AND "
              "gross_square_feet IS NOT NULL AND "
              "land_square_feet IS NOT NULL",
    "$limit": 1000
}

resp = requests.get(url, params=params)
df = pd.DataFrame(resp.json())
df
df.to_csv("/Users/lihuixiong/Desktop/DSCI510/FINAL/raw_data.csv", index=False)


