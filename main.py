from __future__ import print_function
import time
import sys
from timeit import default_timer as timer
from datetime import date, datetime
from googleapiclient.discovery import build
from creds import Creds
from fetch import Fetch
from spreadsheets import Spreadsheet
from variables import CONSOLE_COLOR, CONSOLE_ENDC, CONSOLE_COLOR_START_DONE, CONSOLE_COLOR_ERROR


def execute(minutes):
    """Run script every X minutes.
    """
    while True:
        execute_start = time.time()
        print(CONSOLE_COLOR_START_DONE + f'{datetime.now()} running script' + CONSOLE_ENDC)

        main_start = timer()
        # Get google api credentials.
        my_creds = Creds()

        # Construct a service for interacting with sheets api.
        service = build('sheets', 'v4', credentials=my_creds.creds)

        # Create new spreadsheet.
        start = timer()
        print('creating spreadsheet...')
        sheet = Spreadsheet(service, f'everyday_sheet{date.today()}')
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
        print(f'script will run again in {minutes} minutes.')

        time.sleep((float(minutes)*60) - ((time.time() - execute_start) % (float(minutes)*60)))


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(CONSOLE_COLOR_ERROR + 'you must enter a parameter (int - minutes)' + CONSOLE_ENDC)
        sys.exit()
    param = int(sys.argv[1])
    try:
        execute(param)
    except ValueError:
        print('wrong parameter, you must enter int number (number of minutes to sleep)')
