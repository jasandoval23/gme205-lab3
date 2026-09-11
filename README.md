# GmE 205 Laboratory 3

## 1. Setup

Install the required packages using the following commands:

- `python -m venv .venv`
- `.venv\Scripts\activate`
- `pip install -r requirements.txt`

### Running the Demonstration

To run the demonstration:

`python src/demo.py`

### Running the Lab 3 Runner

To run the Lab 3 runner:

`python src/run_lab3.py`

The runner produces:

- `output/lab3_report.json`
- `output/lab3_preview.png`

### Running the Tests

To run the tests:

`pytest`

All focused tests should pass.

## 2. Reflection

### 1. Refactoring: What changed in the internal representation of Point? What remained stable for code using the object?

For this lab, I changed how the Point object stores its coordinates. In Laboratory 2, longitude and latitude were stored separately. In Laboratory 3, they are now stored as a Shapely Point geometry. However, I kept the coordinate validation in the Point constructor. I also kept the `lon`, `lat`, and `to_tuple()` access so that the Point can still be used in a similar way as before.

### 2. Responsibility: Which behavior now belongs to Shapely, which belongs to SpatialObject, and which remains specific to Point or Parcel?

I learned that not all of the spatial work needs to be placed inside the Point or Parcel class. Shapely now handles the geometry and spatial operations. SpatialObject handles the common functions such as `bbox()` and `intersects()`. Point still handles things that are specific to a point, such as coordinate validation and Haversine distance. Parcel handles its own parcel ID and attributes.

### 3. Data boundary: Why should from_dict() delegate validation to the constructor?

I used `from_dict()` to create a Point from dictionary data. I think the validation should still be done by the constructor because it is already the part that checks if the coordinates are valid. This avoids writing the same validation again inside `from_dict()`.

### 4. Output boundary: Why should as_dict() return primitive / JSON-ready values rather than Shapely geometry objects?

I made `as_dict()` return simple values instead of the actual Shapely geometry. This makes the output easier to read and allows it to be saved as JSON. It also keeps the Shapely object inside the object instead of putting it directly in the output.

### 5. Inheritance: Why does intersects() belong in SpatialObject instead of being duplicated in Point and Parcel?

I placed `intersects()` in SpatialObject because both Point and Parcel have geometry and can use the same function. If I placed the method separately in both classes, I would have to repeat the same code. Using SpatialObject allows both classes to inherit the behavior.

### 6. Coordinate meaning: Why is geometry.distance() not automatically a real-world distance in meters for longitude/latitude data?

I did not replace the Haversine distance from Laboratory 2 with `geometry.distance()`. Shapely calculates distance using a Cartesian plane and the units of the input coordinates. Since the coordinates I used for Point are longitude and latitude, the result is not automatically in meters. I therefore kept the Haversine method for distance in meters. Shapely was used for the geometry, bounds, and spatial relationships, while the meaning and units of the coordinates remained part of the model.

### 7. Scale: If the system grows to millions of objects, what part of this design helps maintainability, and what performance problems would still require different techniques?

I think the use of SpatialObject would make the system easier to maintain if more types of spatial objects were added because common behavior only needs to be written once. However, having millions of objects could still cause problems with memory and processing time. Checking spatial relationships between many objects could also become slow, so additional techniques such as spatial indexing would be needed.

### Final Design Question: Can you explain why each responsibility lives where it does? If the answer is only “because the instructions said so,” the exercise is not finished.

The responsibilities were separated so that each part of the system has a clear purpose. Shapely handles the geometry and spatial operations, while SpatialObject handles behavior that is common to spatial objects. Point and Parcel keep the information and behavior that are specific to each type. This makes the code easier to understand and avoids putting everything in one class.