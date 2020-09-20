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

    def convert_data(self, data):
        """Convert all data to list.
        """
        self._convert_reddit(data[DATA_KEYS[0]], 'reddit')
        self._convert_coinpaprika(data[DATA_KEYS[1]], 'crypto')

    def insert_data(self):
        """Insert data into a spreadsheet.
        """
        cell_range = 'A1:Z200'
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
        request = {
            "requests": [
                {
                    "autoResizeDimensions": {
                        "dimensions": {
                            "dimension": "COLUMNS",
                            "startIndex": 0,
                            "endIndex": 20
                        }
                    }
                }
            ]
        }
        self.service.spreadsheets().batchUpdate(spreadsheetId=self.sheet_id, body=request).execute()
