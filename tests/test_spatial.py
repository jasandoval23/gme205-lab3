from spatial import Point, Parcel
from shapely.geometry import Polygon


def test_valid_point():
    p = Point("A", 121.0, 14.6)
    assert p.lon == 121.0
    assert p.lat == 14.6


def test_invalid_longitude():
    try:
        Point("A", 999, 14.6)
        assert False
    except ValueError:
        assert True


def test_from_dict():
    data = {
        "id": "B",
        "lon": 121.05,
        "lat": 14.65,
        "name": "Sample Place",
        "tag": "POI"
    }

    p = Point.from_dict(data)

    assert p.id == "B"
    assert p.lon == 121.05
    assert p.lat == 14.65


def test_invalid_from_dict():
    data = {
        "id": "C",
        "lon": 999,
        "lat": 14.65
    }

    try:
        Point.from_dict(data)
        assert False
    except ValueError:
        assert True


def test_point_bbox():
    p = Point("A", 121.0, 14.6)
    assert p.bbox() == (121.0, 14.6, 121.0, 14.6)


def test_parcel_bbox():
    geom = Polygon([
        (0, 0),
        (10, 0),
        (10, 5),
        (0, 5)
    ])

    parcel = Parcel(101, geom, {})

    assert parcel.bbox() == (0.0, 0.0, 10.0, 5.0)


def test_intersects():
    geom = Polygon([
        (0, 0),
        (10, 0),
        (10, 5),
        (0, 5)
    ])

    parcel = Parcel(101, geom, {})

    inside = Point("IN", 2, 2)
    outside = Point("OUT", 12, 2)

    assert inside.intersects(parcel) is True
    assert outside.intersects(parcel) is False


def test_as_dict():
    p = Point("A", 121.0, 14.6, name="Gate", tag="POI")

    data = p.as_dict()

    assert data["id"] == "A"
    assert data["geometry"] == [121.0, 14.6]
    assert data["bbox"] == [121.0, 14.6, 121.0, 14.6]