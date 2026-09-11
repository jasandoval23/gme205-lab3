import json
from pathlib import Path

import matplotlib.pyplot as plt
from shapely.geometry import Polygon

from spatial import Point, Parcel


def main():
    # Create output folder
    output_dir = Path("output")
    output_dir.mkdir(exist_ok=True)

    # Create Point
    point = Point("A", 121.0, 14.6, name="Gate", tag="POI")

    # Create Parcel
    attributes = {
        "area": 50.0,
        "zone": "Residential",
        "is_active": True
    }

    geom = Polygon([
        (0, 0),
        (10, 0),
        (10, 5),
        (0, 5)
    ])

    parcel = Parcel(101, geom, attributes)

    # Create inside and outside points
    inside = Point("IN", 2, 2)
    outside = Point("OUT", 12, 2)

    # Build report
    report = {
        "point": point.as_dict(),
        "parcel": parcel.as_dict(),
        "relationships": {
            "inside_intersects_parcel": inside.intersects(parcel),
            "outside_intersects_parcel": outside.intersects(parcel)
        }
    }

    # Write JSON report
    with open(output_dir / "lab3_report.json", "w", encoding="utf-8") as file:
        json.dump(report, file, indent=2)

    # Create preview
    x, y = parcel.geometry.exterior.xy

    plt.figure()
    plt.plot(x, y, label="Parcel")

    plt.scatter(
        inside.lon,
        inside.lat,
        label="Inside"
    )

    plt.scatter(
        outside.lon,
        outside.lat,
        label="Outside"
    )

    plt.text(inside.lon, inside.lat, " IN")
    plt.text(outside.lon, outside.lat, " OUT")

    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Lab 3 Spatial Object Preview")
    plt.legend()
    plt.savefig(output_dir / "lab3_preview.png")
    plt.close()


if __name__ == "__main__":
    main()