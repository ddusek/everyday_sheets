from __future__ import print_function
from timeit import default_timer as timer
from datetime import date
from pprint import pprint
from googleapiclient.discovery import build
from creds import Creds
from fetch import Fetch
from spreadsheets import Spreadsheet

if __name__ == '__main__':
    main_start = timer()
    # Get google api credentials.
    my_creds = Creds()

    # Construct a service for interacting with sheets api.
    service = build('sheets', 'v4', credentials=my_creds.creds)

    # Fetch data from all data sources defined in json file.
    fetcher = Fetch('api_inputs.json')

    start = timer()
    data = fetcher.fetch_all()
    print(f'data fetched in {round(timer() - start, 3)}s')

    # Fill spreadsheet with fetched data.
    start = timer()
    values = []
    for post in data['reddit']:
        values.append([post['title']])
        values.append([post['reddit_url']])
        values.append([post['link_url']])
        values.append([])
    print(f'list with all values created in {round(timer() - start, 3)}s')

    # Create new spreadsheet.
    start = timer()
    sheet = Spreadsheet(service, f'everyday_sheet{date.today()}')
    print(f'new sheet created in {round(timer() - start, 3)}s')

    # Insert data into spreadsheet.
    start = timer()
    sheet.insert_data(values, 'A1:Z200', 'USER_ENTERED')
    print(f'data inserted into a sheet in {round(timer() - start, 3)}s')

    # Adjust columns size.
    sheet.set_col_size()

    print(f'elapsed time since start {round(timer() - main_start, 3)}s')
