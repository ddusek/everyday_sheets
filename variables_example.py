CONSOLE_COLOR = '\033[92m'
CONSOLE_ENDC = '\033[0m'
CONSOLE_COLOR_ERROR = '\033[91m'
CONSOLE_COLOR_START_DONE = '\033[92m'

# https://www.reddit.com/dev/api
REDDIT_CLIENT_ID = 'REDDIT_CLIENT_ID'
REDDIT_CLIENT_SECRET = 'REDDIT_CLIENT_SECRET'

TELEGRAM_BOT_TOKEN = 'TOKEN'

# https://newsapi.org
NEWSAPI_KEY = 'NEWSAPI_KEY'


DATA_KEYS = ['reddit', 'news_cz', 'news_general', 'news_technology', 'news_science', 'news_gaming', 'crypto']

NEWSAPI_IGNORED_SOURCES = ['Sport.cz', 'Nova.cz']

NEWSAPI_SOURCES_GENERAL = ','.join(['abc-news',
                                    'breitbart-news',
                                    'fox-news',
                                    'time'])

NEWSAPI_SOURCES_TECHNOLOGY = ','.join(['techcrunch',
                                       'techradar',
                                       'crypto-coins-news'])

NEWSAPI_SOURCES_GAMING = ','.join(['polygon',
                                   'ign'])

EMOJI_SLEEP = u'\U0001F634'
EMOJI_SCREAM = u'\U0001F631'
