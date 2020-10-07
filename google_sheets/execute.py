from __future__ import print_function
from timeit import default_timer as timer
from datetime import datetime
from googleapiclient.discovery import build
from fetch import Fetch
from variables import CONSOLE_COLOR, CONSOLE_ENDC, CONSOLE_COLOR_START_DONE
from .spreadsheets import Spreadsheet
from .creds import Creds


def execute():
    """Run script every X minutes.
    """
    # Get google api credentials.
    my_creds = Creds()

    # Construct a service for interacting with sheets api.
    service = build('sheets', 'v4', credentials=my_creds.creds)

    print(CONSOLE_COLOR_START_DONE + f'{datetime.now()} running script' + CONSOLE_ENDC)
    main_start = timer()

    # Create new spreadsheet.
    start = timer()
    print('creating spreadsheet...')
    sheet = Spreadsheet(service, f'everyday_sheet{datetime.now()}')
    print(CONSOLE_COLOR + f'new sheet created in {round(timer() - start, 3)}s' + CONSOLE_ENDC)

    # Fetch data from all data sources defined in json file.
    fetcher = Fetch('reddit_inputs.json')
    start = timer()
    print('fetching data...')
    data = fetcher.fetch_all()
    print(CONSOLE_COLOR + f'data fetched in {round(timer() - start, 3)}s' + CONSOLE_ENDC)

    # Convert data into format needed for spreadsheet.
    sheet.convert_data(data)

    # Insert data into spreadsheet.
    start = timer()
    print('inserting data into spreadsheet...')
    sheet.insert_data()
    print(CONSOLE_COLOR + f'data inserted into a sheet in {round(timer() - start, 3)}s' + CONSOLE_ENDC)

    # Adjust columns size.
    sheet.set_col_size()

    print(CONSOLE_COLOR + f'elapsed time since start {round(timer() - main_start, 3)}s' + CONSOLE_ENDC)

    print('added ', datetime.now())
    print(CONSOLE_COLOR_START_DONE + f'{datetime.now()} script finished' + CONSOLE_ENDC)

    return f'https://docs.google.com/spreadsheets/d/{sheet.sheet_id}/edit#gid=0'
