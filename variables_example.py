CONSOLE_COLOR = '\033[92m'
CONSOLE_ENDC = '\033[0m'

DATA_KEYS = ['reddit', 'news_cz', 'news_general', 'news_technology', 'news_science', 'news_gaming', 'crypto']

# https://newsapi.org
NEWSAPI_KEY = 'NEWSAPI_KEY'
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

# https://www.reddit.com/dev/api
REDDIT_CLIENT_ID = 'REDDIT_CLIENT_ID'
REDDIT_CLIENT_SECRET = 'REDDIT_CLIENT_SECRET'
