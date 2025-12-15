# %%
numeric_cols = ["sale_price", "land_square_feet", "gross_square_feet"]
for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

df["sale_date"] = pd.to_datetime(df["sale_date"], errors="coerce")


df = df.dropna(subset=["sale_price"])

# %%
df.isna().sum()

# %%

value_counts = df["borough"].value_counts()


for cat, count in value_counts.items():
    print(f"{cat}: {count}")

# %%

value_counts = df["building_class_category"].value_counts()


for cat, count in value_counts.items():
    print(f"{cat}: {count}")

# %%
def building_class_8cat(cat):
    if cat is None:
        return "Other"
    c = str(cat).upper()
    

    if c.startswith("01"):
        return "OneFamily"
    elif c.startswith("02"):
        return "TwoFamily"
    elif c.startswith("03"):
        return "ThreeFamily"
    

    elif c.startswith("07"):
        return "WalkupApt"
    elif c.startswith("08"):
        return "ElevatorApt"
    
   
    elif c.startswith("21") or c.startswith("22") or c.startswith("29") or c.startswith("30") \
         or c.startswith("27") or c.startswith("33") or c.startswith("35") or c.startswith("32") \
         or c.startswith("26"):
        return "Commercial"
    
   
    elif c.startswith("05") or c.startswith("31") or c.startswith("06"):
        return "VacantLand"
    
    else:
        return "Other"

df["building_class_8"] = df["building_class_category"].apply(building_class_8cat)
print(df["building_class_8"].value_counts())


# %%
df = df.drop(columns=["land_square_feet","neighborhood"], errors="ignore")
df = df[df["gross_square_feet"] != 0]
df
df.to_csv("/Users/lihuixiong/Desktop/DSCI510/FINAL/processed_data.csv", index=False)


