from __future__ import print_function
from pprint import pprint
from googleapiclient.discovery import build
from creds import Creds
from fetch import Fetch

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms'
SAMPLE_RANGE_NAME = 'Class Data!A2:E'


if __name__ == '__main__':
    # Get google api credentials.
    my_creds = Creds()

    # Construct a service for interacting with sheets api.
    service = build('sheets', 'v4', credentials=my_creds.creds)

    # Fetch data from all data sources defined in json file.
    fetcher = Fetch('api_inputs.json')
    data = fetcher.fetch_all()

    # Fill spreadsheet with fetched data.
    spreadsheet_body = {
        # TODO: Add desired entries to the request body.
    }

    # Create new spreadsheet.
    # request = service.spreadsheets().create(body=spreadsheet_body)
    # response = request.execute()

    # TODO: Change code below to process the `response` dict:
    # pprint(response)
