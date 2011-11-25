from pymymailru import *
from flask import requst, session, g

def auth(f):
    from functools import wraps

    @wraps(f)
    def mailru_auth(*a, **kw):

		g.token = request.args['session_key']

		session['auth'] = {
			"user_id": request.args['vid'],
			"token": g.token,
		}

        return f(*a, **kw)

    return fb_auth