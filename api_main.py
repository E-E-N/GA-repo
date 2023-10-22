#module to send HTTP requests
import requests

#Class with the Attributes; A part of steps to retrieve data from API requests url
class APIhandler:
    def __init__(self, location='a', count=1, geocoding_api_url='https://geocoding-api.open-meteo.com/v1/search', 
                language='en', format='json'):
        self.geocoding_api_url = geocoding_api_url
        self.location = location
        self.language = language
        self.count = count
        self.format = format
        
    # Send an API request to retrieve geocoding data.
    def make_api_request(self, location, count):
        #Build the API url using the provided/default values
        api_url = f"{self.geocoding_api_url}?name={location}&count={count}&language={self.language}&format={self.format}"
        # Send HTTP Get Request constructed API URL.
        response = requests.get(api_url)
        return response

# Extracts Data from the API url and Organize the Data
    def Geocoding_data(self, *args):
        # Determine the 'location' and 'count' values from arguments or class
        location = args[0] if args else self.location 
        count = args[1] if len(args) > 1 else self.count 
        response = self.make_api_request(location, count)

        if response is None:
            return {"error": "Request from API URL Failed"}
        try:
            json_data = response.json()
        except ValueError as E:
            print(f"JSON Error: {E}")
            return{"Error - INVALID JSON Response"}

        extracted_data = []
        for result in json_data.get('results', []):
            data = {
                'location': result.get('name'),
                'latitude': result.get('latitude'),
                'population': result.get('population'),
                'longitude': result.get('longitude'),
                'timezone': result.get('timezone'),
                'elevation': result.get('elevation'),
                'country_code': result.get('country_code'),
                'format': self.format
                }
            extracted_data.append(data)
        

        formatted_data = {
            'geocoding_results': extracted_data,
            'total_results': len(extracted_data),               
            }
        return formatted_data
        

          