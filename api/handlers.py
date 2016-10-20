from bottle.ext.neck import WSResponse
import bottle


def news_api():
    """Retrieve latest news API endpoint.
    """
    feed_size = bottle.request.query.smart_filters().get('size') or 5

    news = [
        {'icon': 'https://placeholdit.imgix.net/~text?txtsize=33&txt=news%20icon&w=100&h=100',
         'body': 'Sed ut perspiciatis omnis natus error sit voluptatem accusantium done.',
         'title': 'A lonely flower',
         'uid': _ + 1}
        for _ in range(0, feed_size)
    ]

    return WSResponse.ok(news)


def search_api():
    """Search API endpoint.
    """

    search_term = bottle.request.query.smart_filters().get('term')

    return WSResponse.ok({'keyword': search_term})