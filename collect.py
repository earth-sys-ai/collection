import geojson

# handles json input
def handle(raw):
    data = geojson.loads(raw)
    print(data)