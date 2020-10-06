from variables import NEWSAPI_SOURCES_GAMING, NEWSAPI_SOURCES_GENERAL, NEWSAPI_SOURCES_TECHNOLOGY


FIXED_PARAMS = {
    'cz': ['top-headlines', 'country', 'cz'],
    'general': ['top-headlines', 'sources', NEWSAPI_SOURCES_GENERAL],
    'technology': ['top-headlines', 'sources', NEWSAPI_SOURCES_TECHNOLOGY],
    'science': ['top-headlines', ['category', 'country'], ['science', 'us']],
    'gaming': ['top-headlines', 'sources', NEWSAPI_SOURCES_GAMING],
}
