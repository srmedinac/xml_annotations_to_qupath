## XML to Qupath

Simple script that helps you batch convert XML annotations to Qupath compatible Geojson annotations. modify the `annotations_dir` and `output_dir` variables with your desired paths. Since Geojson checks if the polygons are closed for it to be a valid annotation, we check if starting and end point are the same, if not we close it by adding the initial point to the end. which is a hack but works
