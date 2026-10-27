# Leaflet cluster map of talk locations
#
# Run this from the _talks/ directory, which contains .md files of all your
# talks. This scrapes the location YAML field from each .md file, geolocates it
# with geopy/Nominatim, and uses the getorg library to output data, HTML, and
# Javascript for a standalone cluster map. This is functionally the same as the
# #talkmap Jupyter notebook.
import frontmatter
import glob
import getorg
from geopy import Nominatim
from geopy.exc import GeocoderTimedOut
from geopy.location import Location

# Set the default timeout, in seconds
TIMEOUT = 5

# Collect the Markdown files
g = glob.glob("_talks/*.md")

# Prepare to geolocate
geocoder = Nominatim(user_agent="academicpages.github.io")
location_dict = {}
location = ""
permalink = ""
title = ""

# Perform geolocation
for file in g:
    # Read the file
    data = frontmatter.load(file)
    data = data.to_dict()

    # Press on if the location is not present
    if 'location' not in data:
        continue

    # Prepare the description
    title = data['title'].strip()
    venue = (data.get('venue') or data.get('event') or '').strip()
    location = data['location'].strip()
    description = f"{title}<br />{venue}; {location}"

    # Geocode the location and report the status
    try:
        if data.get('latitude') is not None and data.get('longitude') is not None:
            result = Location(location, (data['latitude'], data['longitude']), {})
        else:
            result = geocoder.geocode(location, timeout=TIMEOUT)
        if result is None:
            raise ValueError(f"No coordinates found for {location}")
        location_dict[description] = result
        print(description, location_dict[description])
    except ValueError as ex:
        raise RuntimeError(f"Geocoding failed for {location}") from ex
    except GeocoderTimedOut as ex:
        raise RuntimeError(f"Geocoding timed out for {location}") from ex
    except Exception as ex:
        raise RuntimeError(f"Could not process {location}") from ex

# Save the map
m = getorg.orgmap.create_map_obj()
getorg.orgmap.output_html_cluster_map(location_dict, folder_name="talkmap", hashed_usernames=False)
