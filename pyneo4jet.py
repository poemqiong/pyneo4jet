#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File: pyneo4jet.py
Author: huxuan - i(at)huxuan.org
Created: 2012-11-25
Last modified: 2012-11-25
Description:
    Main interface for pyneo4jet

Copyrgiht (c) 2012 by huxuan. All rights reserved.
License GPLv3
"""
import sys

import gevent.monkey
gevent.monkey.patch_all()
from bottle import run, get, post, request, template

try:
    from config import *
except ImportError:
    print '[Error] config.py is NEEDED! Refer to config-sample.py'
    sys.exit(1)

@get('/')
def login_or_timeline_get():
    """
    Check whether user has login
    show the timeline if is
    show login otherwise
    """
    return 'GET /'

@post('/')
def login_post():
    """
    Check whether post the corresponding username and password
    """
    return 'POST /'

@get('/register/')
def register_get():
    """
    Show the form for register

    Note:
        Currently INVITATION_CODE is NEEDED!
    """
    return 'GET /register/'

@post('/register/')
def register_post():
    """
    Add a new account

    Note:
        Need to check whether username, avatar and INVITATION_CODE is valid
        avatar could be optional but should have default value
    """
    return 'POST /register/'

@get('/profile/')
def profile_get():
    """
    Show form of profile with subbmit button which can change it.
    """
    return 'GET /profile/'

@post('/profile/')
def profile_post():
    """
    Update profile and redirect to get page
    """
    return 'POST /profile/'

@get('/tweet/')
@get('/tweet/<index:int>')
def tweet_get(index=0):
    """
    Show an empty form for tweet
    """
    return 'GET /tweet/%d' % index

@post('/tweet/')
def tweet_post():
    """
    Add a new tweet
    """
    return 'POST /tweet/'

@get('/user/<username>')
def user_get(username):
    """
    Show user's profile and tweets as well as follow link or followed status.
    """
    return 'GET /user/%s' % username

@get('/user/<username>/friends/')
@get('/user/<username>/friends/<index:int>')
def user_firends_get(username, index=0):
    """
    Show list for user's friends
    """
    return 'GET /user/%s/friends/%d' % (username, index, )

def main():
    """Parse the args and run the server"""
    if len(sys.argv) == 2 and sys.argv[1].isdigit():
        port = sys.argv[1]
    else:
        port = 8888
    run(server='gevent', host='0.0.0.0', port=port, quiet=True, fast=True)

if __name__ == '__main__':
    main()