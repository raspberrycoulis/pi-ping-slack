#!/usr/bin/python

# This Python script will ping a website and return the relevant HTTP status code.
# It will then send a message to Slack (via webhook) telling you either:
#
# "Google is up and running"
# "Google is offline!"
#
# More on HTTP status codes found here: https://en.wikipedia.org/wiki/List_of_HTTP_status_codes
#
# Feel free to improve as I made this quickly and I'm not a coding ninja!
#
# By: Wesley Archer (aka. Raspberry Coulis)
# Web: https://www.raspberrycoulis.co.uk
# Twitter: https://twitter.com/raspberrycoulis
# Email: wesley@raspberrycoulis.co.uk

import requests
import urllib2
import time

# Replace the URL with the website you want to test
website = "https://www.google.co.uk/"

# Replace the sitename to match the site you want to test - this will be included in the Slack message
sitename = "Google"

# The time (in seconds) between checks. Default is 1800 seconds (30 minutes)
wait = 1800

# Replace with your incoming webhook URL generated in Slack
webhook = 'YOUR_SLACK_INCOMING_WEBHOOK'


def ping():
  while True:
    response = requests.get(website)
    dataup = '{"text":"'+sitename+' is up and running"}'
    datadown = '{"text":"'+sitename+' is offline!"}'
    requp = urllib2.Request(webhook, dataup, {'Content-Type': 'application/json'})
    reqdown = urllib2.Request(webhook, datadown, {'Content-Type': 'application/json'})

    if int(response.status_code) == 200: # OK
      f = urllib2.urlopen(requp)
      f.close()

    elif int(response.status_code) == 400: # Bad request
      f = urllib2.urlopen(reqdown)
      f.close()        

    elif int(response.status_code) == 401: # Unauthorised
      f = urllib2.urlopen(reqdown)
      f.close()

    elif int(response.status_code) == 403: # Forbidden
      f = urllib2.urlopen(reqdown)
      f.close()

    elif int(response.status_code) == 404: # Not found
      f = urllib2.urlopen(reqdown)
      f.close()

    elif int(response.status_code) == 444: # nginx: No response
      f = urllib2.urlopen(reqdown)
      f.close()
                                
    elif int(response.status_code) == 500: # Internal server error
      f = urllib2.urlopen(reqdown)
      f.close()

    elif int(response.status_code) == 502: # Bad gatway
      f = urllib2.urlopen(reqdown)
      f.close()        

    elif int(response.status_code) == 503: # Service unavailable
      f = urllib2.urlopen(reqdown)
      f.close()

    elif int(response.status_code) == 520: # Cloudflare: Unknown error
      f = urllib2.urlopen(reqdown)
      f.close()

    elif int(response.status_code) == 522: # Cloudflare: Connedction timed out
      f = urllib2.urlopen(reqdown)
      f.close()

    elif int(response.status_code) == 523: # Cloudflare: Origin is unreachable
      f = urllib2.urlopen(reqdown)
      f.close()
        
    elif int(response.status_code) == 524: # Cloudflare: A Timeout occurred
      f = urllib2.urlopen(reqdown)
      f.close()

    time.sleep(wait)

ping()