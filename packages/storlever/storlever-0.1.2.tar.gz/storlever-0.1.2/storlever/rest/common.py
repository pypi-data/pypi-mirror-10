"""
storlever.common
~~~~~~~~~~~~~~~~

This module implements some common API for REST.

:copyright: (c) 2014 by OpenSight (www.opensight.cn).
:license: AGPLv3, see LICENSE for more details.

"""
import sys
import traceback

import pyramid.exceptions
from pyramid.view import view_config
from pyramid.response import Response
from pyramid.events import subscriber, NewResponse
from pyramid.renderers import render_to_response

from storlever.lib.schema import SchemaError as ValidationFailure
from storlever.lib.exception import StorLeverError

class _rest_view(view_config):
    def __init__(self, **settings):
        method = self.__class__.__name__.split('_')[0].upper()
        super(_rest_view, self).__init__(request_method=method,
                                         **settings)


class get_view(_rest_view):
    pass


class post_view(_rest_view):
    pass


class put_view(_rest_view):
    pass


class delete_view(_rest_view):
    pass


@view_config(context=ValidationFailure)
def failed_validation(exc, request):
    response = request.response
    response.status_int = 400
    type, dummy, tb = sys.exc_info()
    tb_list = traceback.format_list(traceback.extract_tb(tb)[-5:])
    return {'info': str(exc), 'exception': str(type), 'traceback': tb_list}


@view_config(context=StorLeverError)
def storlever_error_view(exc, request):
    response = request.response
    response.status_int = exc.http_status_code
    type, dummy, tb = sys.exc_info()
    tb_list = traceback.format_list(traceback.extract_tb(tb)[-5:])
    return {'info': str(exc), 'exception': str(type), 'traceback': tb_list}


@view_config(context=Exception)
def error_view(exc, request):
    response = request.response
    response.status_int = 500
    type, dummy, tb = sys.exc_info()
    tb_list = traceback.format_list(traceback.extract_tb(tb)[-5:])
    return {'info': str(exc), 'exception': str(type), 'traceback': tb_list}


@view_config(context=pyramid.exceptions.NotFound)
def not_found_view(exc, request):
    response = request.response
    response.status_int = exc.status_code
    type, dummy, tb = sys.exc_info()
    if not request.path.startswith('/storlever/api/'):
        return render_to_response('storlever:templates/404.pt', {},
                              request=request)
    else:
        return {'info': 'Resource {0} not found or method {1} not supported'.format(request.path, request.method),
                'exception': str(type),
                'traceback': []}


@subscriber(NewResponse)
def add_response_header(event):
    """
    add all custom header here
    """
    response = event.response
    response.headers['X-Powered-By'] = 'OpenSight (www.opensight.cn)'
    response.headers['Access-Control-Allow-Origin'] = '*'

def get_params_from_request(request, schema=None):
    """Get input parameter dict from request

    If the request content type is json, get the params dict from json body,
    otherwise, from GET/POST params.
    If shema is not None, check the input params dict against the schema.

    return the params dict.


    :param request: request object
    :param schema:  the schema for the input params

    """
    params = dict(request.params)
    if "json" in request.content_type:
        params.update(request.json_body)
    if schema is not None:
        params = schema.validate(params)

    return params

