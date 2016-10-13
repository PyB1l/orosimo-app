# -*- coding: utf-8 -*-
"""`app.api` package.

Contains the Application API/AJAX services.
"""

__all__ = ('api', )

import bottle
from bottle.ext.neck import StripPathMiddleware, WSResponse
from bottle.ext.smart_filters import SmartFiltersPlugin

api = StripPathMiddleware(bottle.Bottle())
api.install(SmartFiltersPlugin())


@api.get('/news')
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


@api.get('/search')
def search_api():
    """Search API endpoint.
    """

    search_term = bottle.request.query.smart_filters().get('term')

    return WSResponse.ok({'keyword': search_term})