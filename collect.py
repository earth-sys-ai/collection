import geojson

# handles json input
# sent a feature array
def handle(raw):
    data = geojson.loads(raw)

    # scrape uid
    uid = data["uid"]
    data.pop("uid")

    # create feature collection
    fs = geojson.FeatureCollection([data["features"]])

    # add from file
    try:
        with open(uid + '.json', 'r') as in_file:
            fs_store = geojson.loads(in_file.read())
            fs = geojson.FeatureCollection(fs["features"] + fs_store["features"])
            fs["features"] = fs["features"][0]
    except:
        print()

    # write collection
    with open(uid + '.json', 'w') as out_file:
        geojson.dump(fs, out_file) 


# store polygons
# store image of polygon location
# assign and sort data by uid