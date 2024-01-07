import os
import glob
import json
from pathlib import Path
import xml.etree.ElementTree as ET


def convert_xml_to_geojson(xml_file_path):
    """
    Converts an XML annotation file to GeoJSON format.
    """
    tree = ET.parse(xml_file_path)
    root = tree.getroot()
    geojson = {"type": "FeatureCollection", "features": []}

    for annotation in root.findall(".//Annotation"):
        for region in annotation.findall(".//Region"):
            vertices = region.findall(".//Vertex")
            geojson_points = [
                [float(vertex.get("X")), float(vertex.get("Y"))] for vertex in vertices
            ]

            # Ensure the polygon is closed by repeating the first point at the end if necessary
            if geojson_points[0] != geojson_points[-1]:
                geojson_points.append(geojson_points[0])

            feature = {
                "type": "Feature",
                "geometry": {"type": "Polygon", "coordinates": [geojson_points]},
                "properties": {"name": "Region {}".format(region.get("Id"))},
            }
            geojson["features"].append(feature)

    return json.dumps(geojson, indent=4)


annotations_dir = "/path/to/all/your/annotations"
output_dir = "/output/path/"


for xml_file_path in glob.glob(os.path.join(annotations_dir, "*.xml")):
    converted_geojson = convert_xml_to_geojson(xml_file_path)
    output_file_path = os.path.join(output_dir, Path(xml_file_path).stem + ".geojson")

    with open(output_file_path, "w") as file:
        file.write(converted_geojson)

    print("Converted file saved at:", output_file_path)


#########IF SINGLE FILE##########
# xml_file_path = "path/to/file.xml"  # Replace with the actual path to your XML file
# converted_geojson = convert_aperio_to_geojson(xml_file_path)

# output_dir = "/output/path/"  # Replace with your desired output directory
# output_file_path = os.path.join(output_dir, Path(xml_file_path).stem + ".geojson")

# with open(output_file_path, "w") as file:
#     file.write(converted_geojson)

# print("Converted file saved at:", output_file_path)
#################################
