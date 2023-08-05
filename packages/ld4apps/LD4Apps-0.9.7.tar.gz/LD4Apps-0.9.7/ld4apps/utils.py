import os
import Cookie, cryptography
import uuid
import requests, urlparse
import json
from base_constants import ADMIN_USER
from rdf_json import RDF_JSON_Encoder
import url_policy as url_policy_module

import logging
logger = logging.getLogger(__name__)
class LimitLogging():
    def __init__(self, lvl):
        self.level=lvl
    def __enter__(self):
        logging.disable(self.level)
    def __exit__(self, a, b, c):
        logging.disable(logging.NOTSET)
LIMIT_LOGGING_LEVEL_INFO = LimitLogging(logging.INFO)

SYSTEM_HOST = os.environ.get('SYSTEM_HOST') if 'SYSTEM_HOST' in os.environ else None

def get_jwt(environ):
    session_key = None
    if ('HTTP_COOKIE' in environ):
        cookie = Cookie.SimpleCookie()
        cookie.load(environ['HTTP_COOKIE'])
        if 'SSSESSIONID' in cookie:
            session_key = cookie['SSSESSIONID'].value
    elif ('HTTP_AUTHORIZATION' in environ and environ['HTTP_AUTHORIZATION'].lower().startswith('bearer ')):
        # user credentials from another domain were passed by the client
        session_key = environ['HTTP_AUTHORIZATION'][len('bearer '):]
    elif ('GUEST_AUTHORIZATION' in environ):
        session_key = environ['GUEST_AUTHORIZATION']
    return session_key

def get_claims(environ):
    session_key = get_jwt(environ)
    if session_key:
        return cryptography.decode_jwt(session_key) 
    else:
        return None       

def get_or_create_claims(environ):
    jwt = get_jwt(environ)
    if jwt:
        claims = cryptography.decode_jwt(jwt) 
        if not claims: # expired claims?
            claims = cryptography.decode_jwt(jwt, verify_expiration=False)
            if claims: # we have a verified set of claims, but they have expired
                del claims['acc']
                del claims['exp']
                environ['GUEST_AUTHORIZATION'] = cryptography.encode_jwt(claims)
    else:
        claims = None
    if not claims:
        claims = create_anonymous_user_claims(environ)
        environ['GUEST_AUTHORIZATION'] = cryptography.encode_jwt(claims)
    return claims

def create_anonymous_user_claims(environ):
    host = get_request_host(environ)
    anonymous_user = 'http://%s/unknown_user/%s' % (host, uuid.uuid4())
    return {'user': anonymous_user} 

def get_request_host(environ): # TODO: remove this and make callers use get_request_host function in lda-clientlib
    return url_policy_module.get_request_host(environ)

def get_request_url(environ):
        host = get_request_host(environ)
        if environ['QUERY_STRING']:
            request_url = 'http://%s%s?%s' %(host, environ['PATH_INFO'], environ['QUERY_STRING'])
        else:
            request_url = 'http://%s%s' %(host, environ['PATH_INFO'])
        return request_url

def set_resource_host_header(request_url, headers):
    if SYSTEM_HOST is not None:
        parts = list(urlparse.urlparse(request_url))
        if not parts[0]:
            parts[0] = 'http'
        if parts[1]:
            headers['CE-Resource-Host'] = parts[1]
        parts[1] = SYSTEM_HOST
        return urlparse.urlunparse(tuple(parts))
    else:
        return request_url

def intra_system_get(request_url, headers=None):
    if not headers: headers = dict()
    actual_url = set_resource_host_header(str(request_url), headers)
    logger.debug('intra_system_get request_url: %s actual_url: %s headers: %s', request_url, actual_url, headers)
    return requests.get(actual_url, headers=headers)

CONTENT_RDF_JSON_HEADER = {
    'Content-type' : 'application/rdf+json+ce',
    'Cookie' : 'SSSESSIONID=%s' % cryptography.encode_jwt({'user': ADMIN_USER}),
    'ce-post-reason' : 'ce-create'
    }

def intra_system_post(request_url, data, headers=None):
    if not headers: headers = CONTENT_RDF_JSON_HEADER.copy()
    actual_url = set_resource_host_header(request_url, headers)
    logger.debug('intra_system_post request_url: %s actual_url: %s headers: %s data: %s', request_url, actual_url, headers, data)
    return requests.post(actual_url, headers=headers, data=json.dumps(data, cls=RDF_JSON_Encoder), verify=False)
    return None
