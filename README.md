# everyday_data
Telegram bot to get data from some APIs, save them into google sheets and send url of the sheets to the user.
## setup
File variables.py is needed to be created, where should be saved your api keys to run this script.  
You can copy example file variables_example.py, add api keys and change stuff as you want.  
  
File sheets_request.json contains request to google sheets api to change how data should be displayed in spreadsheets (row length, cell styles, etc)

## run flask
$ export FLASK_APP=api.py
$ flask run