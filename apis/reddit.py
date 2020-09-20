import praw
from variables import REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET


class Reddit():
    """Class to get data using praw.
    """
    def __init__(self, inputs):
        self.inputs = inputs
        self.user_agent = 'USERAGENT'

    def get_data(self):
        """Get data from api and return it in dictionary.
        """
        reddit = praw.Reddit(client_id=REDDIT_CLIENT_ID, client_secret=REDDIT_CLIENT_SECRET,
                             user_agent=self.user_agent)
        results = []
        for r_input in self.inputs['subreddits']:
            posts = reddit.subreddit(r_input['subreddit']) \
                    .top(time_filter=r_input['time_filter'], limit=r_input['limit'])

            for post in posts:
                results.append({
                        'title': post.title,
                        'link_url': post.url,
                        'reddit_url': 'https://reddit.com'+post.permalink
                    })
        return results
