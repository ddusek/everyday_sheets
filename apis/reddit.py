import praw


class Reddit():
    """Class to get data using praw.
    """
    def __init__(self, inputs):
        self.inputs = inputs
        self.results = []

    def reddit_data(self):
        reddit = praw.Reddit(client_id="XHJ8ldlctO3DUQ", client_secret="FDzafh2IKbeRCZDN5vB4Sp4Kt9c",
                             user_agent="USERAGENT")

        for r_input in self.inputs['subreddits']:
            posts = reddit.subreddit(r_input['subreddit']) \
                    .top(time_filter=r_input['time_filter'], limit=r_input['limit'])

            for post in posts:
                print(dir(post))
                self.results.append(
                    {
                        'title': post.title,
                        'link_url': post.url,
                        'reddit_url': 'https://reddit.com'+post.permalink
                    })
        for data in self.results:
            print(data)
        return self.results
