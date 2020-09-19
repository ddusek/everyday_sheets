class Spreadsheet():
    def __init__(self, service, title):
        self.service = service
        self.title = title
        self.sheet_id = self._create()

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

    def insert_data(self, values, cell_range, valueInputOption):
        """Insert data into a spreadsheet.
        """
        body = {
            'values': values
        }

        spreadsheet = self.service.spreadsheets().values().update(
            range=cell_range,
            valueInputOption=valueInputOption,
            spreadsheetId=self.sheet_id,
            body=body)
        spreadsheet.execute()

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
