from pymymailru import *
from flask import request, session, g, current_app as app, abort

import logging
def auth(f):
    from functools import wraps

    @wraps(f)
    def mailru_auth(*a, **kw):
        logging.info("req: %r" % request.args)

        g.token = request.args['session_key']

        secret = app.config['SOCIAL_API']['secret']
        sig = calc_signature(request.args, secret)
        if sig != request.args['sig']:
            logging.warning("request with tampered sig")
            abort(400)
            return

        session['auth'] = {
                "user_id": request.args['vid'],
                "token": g.token,
        }

        return f(*a, **kw)

    return mailru_auth
