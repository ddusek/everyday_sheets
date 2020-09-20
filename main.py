from __future__ import print_function
from timeit import default_timer as timer
from datetime import date
from googleapiclient.discovery import build
from creds import Creds
from fetch import Fetch
from spreadsheets import Spreadsheet
from variables import CONSOLE_COLOR, CONSOLE_ENDC


if __name__ == '__main__':
    main_start = timer()
    # Get google api credentials.
    my_creds = Creds()

    # Construct a service for interacting with sheets api.
    service = build('sheets', 'v4', credentials=my_creds.creds)

    # Create new spreadsheet.
    start = timer()
    print(CONSOLE_COLOR + 'creating spreadsheet...')
    sheet = Spreadsheet(service, f'everyday_sheet{date.today()}')
    print(f'new sheet created in {round(timer() - start, 3)}s')

    # Fetch data from all data sources defined in json file.
    fetcher = Fetch('reddit_inputs.json')
    start = timer()
    print('fetching data...')
    data = fetcher.fetch_all()
    print(f'data fetched in {round(timer() - start, 3)}s')

    # Convert data into format needed for spreadsheet.
    sheet.convert_data(data)

    # Insert data into spreadsheet.
    start = timer()
    print('inserting data into spreadsheet...')
    sheet.insert_data()
    print(f'data inserted into a sheet in {round(timer() - start, 3)}s')

    # Adjust columns size.
    sheet.set_col_size()

    print('done')
    print(f'elapsed time since start {round(timer() - main_start, 3)}s' + CONSOLE_ENDC)
