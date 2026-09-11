from spatial import Point,Parcel

p = Point("A", 121.0, 14.6, name="Gate", tag="POI")

print(p.id)
print(p.lon, p.lat)
print(p.to_tuple())
print(p.geometry.geom_type)

# # Test 1: Valid dictionary
# data = {
#     "id": "B",
#     "lon": 121.05,
#     "lat": 14.65,
#     "name": "Sample Place",
#     "tag": "POI"
# }

# p = Point.from_dict(data)

# print("Valid record:")
# print(p.id)
# print(p.lon, p.lat)
# print(p.name)
# print(p.tag)


# # Test 2: Invalid dictionary
# bad_data = {
#     "id": "C",
#     "lon": 999,
#     "lat": 14.65,
#     "name": "Invalid Place",
#     "tag": "POI"
# }

# print("\nInvalid record:")
# p_bad = Point.from_dict(bad_data)

# Test 3: as_dict()
# print("\nObject as dictionary:")

# p = Point("A", 121.0, 14.6, name="Gate", tag="POI")

# print(p.as_dict())

# # D.3 Test inherited bbox()
# p = Point("A", 121.0, 14.6)

# print("\nPoint bbox:")
# print(p.bbox())

# E2
from shapely.geometry import Polygon
geom = Polygon([
    (0, 0),
    (10, 0),
    (10, 5),
    (0, 5)
])

attributes = {
    "area": 50.0,
    "zone": "Residential",
    "is_active": True
}
parcel = Parcel(101, geom, attributes)
print(parcel.bbox())

print("\nParcel as dictionary:")
print(parcel.as_dict())

inside = Point("IN", 2, 2)
outside = Point("OUT", 12, 2)

print(inside.intersects(parcel))   # True
print(outside.intersects(parcel))  # False