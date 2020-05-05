import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("TOKEN")

name = "Strava Labs"
print(name)

athlete = 12532
print(athlete)

import time
import json
from swaggerpy.client import SwaggerClient
from swagger_client.rest import ApiException
from pprint import pprint

swagger_client.configuration.access_token = token

# create an instance of the API class
api_instance = swagger_client.SegmentsApi()
bounds = [54.595417, 25.176989, 54.660222, 25.262004]
activityType = "riding"

try:
    # Explore segments
    api_response = api_instance.exploreSegments(bounds, activityType=activityType)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SegmentsApi->exploreSegments: %s\n" % e)
