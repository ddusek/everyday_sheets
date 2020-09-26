import json
from variables import DATA_KEYS


class Spreadsheet():
    def __init__(self, service, title):
        self.service = service
        self.title = title
        self.sheet_id = self._create()
        self.data = {}

    def _create(self):
        """Create a spreadsheet and return its ID.
        """
        spreadsheet_body = {
            'properties': {
                'title': self.title
            },
        }
        spreadsheet = self.service.spreadsheets().create(body=spreadsheet_body)
        response = spreadsheet.execute()
        return response.get('spreadsheetId')

    def _convert_reddit(self, values, key):
        """Convert Reddit data to list.
        """
        self.data[key] = []
        self.data[key].append([key])
        for value in values:
            self.data[key].append([value['title']])
            self.data[key].append([value['reddit_url']])
            self.data[key].append([value['link_url']])
            self.data[key].append([value['rating']])
            self.data[key].append([])

    def _convert_coinpaprika(self, values, key):
        """Convert Coinpaprika data to list.
        """
        self.data[key] = []
        self.data[key].append([key])
        for value in values:
            self.data[key].append([value['coin']])
            self.data[key].append([value['price']])
            self.data[key].append([])

    def _convert_newsapi(self, values, key):
        """Convert newsapi data to list.
        """
        self.data[key] = []
        self.data[key].append([key])
        for value in values:
            self.data[key].append([value['title']])
            self.data[key].append([value['url']])
            self.data[key].append([value['time_published']])
            self.data[key].append([])

    def convert_data(self, data):
        """Convert all data to list.
        """
        self._convert_reddit(data[DATA_KEYS[0]], DATA_KEYS[0])
        self._convert_newsapi(data[DATA_KEYS[1]], DATA_KEYS[1])
        self._convert_newsapi(data[DATA_KEYS[2]], DATA_KEYS[2])
        self._convert_newsapi(data[DATA_KEYS[3]], DATA_KEYS[3])
        self._convert_newsapi(data[DATA_KEYS[4]], DATA_KEYS[4])
        self._convert_newsapi(data[DATA_KEYS[5]], DATA_KEYS[5])
        self._convert_coinpaprika(data[DATA_KEYS[6]], DATA_KEYS[6])

    def insert_data(self):
        """Insert data into a spreadsheet.
        """
        cell_range = 'A1:Z1000'
        value_input_option = 'USER_ENTERED'
        for source in DATA_KEYS:
            body = {
                'values': self.data[source]
            }

            spreadsheet = self.service.spreadsheets().values().update(
                range=cell_range,
                valueInputOption=value_input_option,
                spreadsheetId=self.sheet_id,
                body=body)
            spreadsheet.execute()
            cell_range = chr(ord(cell_range[0])+2) + cell_range[1:]

    def set_col_size(self):
        """Set columns size to fit content.
        """
        request = json.loads(open('sheets_request.json', 'r').read())
        self.service.spreadsheets().batchUpdate(spreadsheetId=self.sheet_id, body=request).execute()
