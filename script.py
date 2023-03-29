# Import libraries
import json
import csv
from roboflow import Roboflow

# Define AI Model
model = Roboflow(api_key="kqDNXws4fknIuWd56ZOo").workspace().project("cansat-4").version(1).model
model.confidence = 40
model.overlap = 30

# Load image info
inputFile = open('images\info.json', 'r')
images = json.load(inputFile)
inputFile.close()

# Create the file with the output data
outputFile = open('data\data.csv', 'w', newline='')
writer = csv.writer(outputFile)
data = []

# Function to deploy model
def getPredictions(image):
    result = model.predict(f'images\{image["name"]}.jpg')
    result.save(f'data\{image["name"]}.jpg')
    return result.json()

# Function to calculate the image dimensions in degrees.
def getDimensions(image):
    height = abs(image['location'][0][0] - image['location'][1][0]) * 2
    width = abs(image['location'][0][1] - image['location'][1][1]) * 2
    return (height, width)

# Function to match prediction coordinates to GPS coordinates in decimal degrees
def getCoordinates(image, prediction, height, width):
    latitude = image['location'][1][0] + height - (prediction['y'] / image['height'] * height)
    longitude = image['location'][1][1] - width + (prediction['x'] / image['width'] * width)
    return (round(latitude, 6), round(longitude, 6))

# Loop for every image
for image in images:
    predictions = getPredictions(image)['predictions']
    print(image['name'])
    
    (height, width) = getDimensions(image)
    for prediction in predictions:
        coordinates = getCoordinates(image, prediction, height, width)
        data.append(coordinates)

# Output data
writer.writerow(('latitude', 'longitude'))
writer.writerows(data)
outputFile.close()