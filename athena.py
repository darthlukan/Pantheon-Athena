#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# Filename: athena-twit.py
# Author: Brian Tomlinson
# Contact: darthlukan@gmail.com
# Description: Twitter client for Athena using the python-twitter module.
# License: GPLv2
# Source: https://github.com/darthlukan/Pantheon-Athena.git

import os
import sys
import twitter

class Twitter():

    def __init__(self):

        self.oauth_token = ''
        self.oauth_token_secret = ''
        self.consumer_key = ''
        self.consumer_secret = ''

        self.api = twitter.Api(self.oauth_token, self.oauth_token_secret,
                               self.consumer_key, self.consumer_secret)

    def authorize(self):
        'TODO'

    def send_updates(self):
        '''Sends multiple status updates if longer than 140 characters.'''
        status = raw_input('Enter your status: ')
        self.api.PostUpdates(status)

    def send_dm(self):
        user = raw_input('Who would you like to send a Direct Message to?: ')
        msg = raw_input('Enter your message to %s: ' % (user))
        self.api.PostDirectMessage(user, msg)

    def get_pub_timeline(self):
        statuses = self.api.GetPublicTimeline()
        for s in statuses:
            print s.user.name, '(' + s.user.screen_name + ')', s.text