# -*- coding: utf-8 -*-
"""`app.api` package.

Contains the Application API/AJAX services.
"""

__all__ = ('api', )

import bottle
import json
from bottle.ext.neck import StripPathMiddleware, WSResponse
from bottle.ext.smart_filters import SmartFiltersPlugin
from app.services import ServiceError, mail_service
from app.models import admin_backend, ModelError


api = StripPathMiddleware(bottle.Bottle())
api.install(SmartFiltersPlugin())


@api.get('/news')
def news_api():
    """Retrieve latest news API endpoint.
    """
    try:
        news = admin_backend('get_latest')

        for post in news:
            post['body'] = ' '.join(post['body'].split(' ')[:10]) + ' ...'

    except ModelError as error:
        return WSResponse.service_unavailable(errors=error.args[0])

    return WSResponse.ok(news)


@api.get('/search')
def search_api():
    """Search API endpoint.
    """

    search_term = bottle.request.query.smart_filters().get('term')

    return WSResponse.ok({'keyword': search_term})


@api.post('/register')
def register_api():
    """Online registration API endpoint.
    """

    try:
        register_data = bottle.request.json
        mail_service('info@oroshmo.gr', register_data)

    except ServiceError as error:
        return WSResponse.service_unavailable(errors=error.args[0])

    except json.JSONDecodeError:
        return WSResponse.bad_request(errors=['Invalid json POST data!'])

    return WSResponse.ok(data={'status': 'send'})
