"""
Site Checker with Time Scheduling - An application that attempts to connect to a website or
server every so many minutes or a given time and check if it is up. If it is down,
it will notify you by email or by posting a notice on screen.
"""
__author__ = 'jeff'
# Simple site monitor.
# Usage: $ python3 site_checker.py domain time_interval
# Usage example: $ python3 site_checker.py github.com 60

from sys import argv
# noinspection PyCompatibility
from urllib import request
from smtplib import SMTP
import re
import time
import sched
import threading

SCHEDULER = sched.scheduler(time.time)


def connection_is_on():
    """
    Check the internet connection by getting status of google and yahoo.
    They can't be down at the same time, right?
    """
    google = get_status('http://google.com')
    yahoo = get_status('http://yahoo.com')
    return google and yahoo


def get_status(url):
    """
    Open given url and check the response status code against 200 and 302.
    If response status code is something else we can consider that the server is down.
    """
    url = normalize_url(url)
    url_file = request.urlopen(url)
    response = url_file.code

    return response in (200, 302)


def email_alert(status):
    """
    Simple e-mail sender.
    Takes only one argument which will be used for both subject and message body.
    """
    sender = 'monitor@yourdomain.com'  # E-mail account to send alert mails.
    password = 'password'
    recipient = 'you@gmail.com'  # Recipient address for down alerts.
    server = SMTP('mail.your_domain.com:25')  # Your email server and port to login and send mails.
    server.ehlo()
    server.starttls()
    server.login(sender, password)
    headers = ["from: " + sender,
               "subject: " + status,
               "to: " + recipient,
               "mime-version: 1.0",
               "content-type: text/html"]
    headers = "\r\n".join(headers)
    server.sendmail(sender, recipient, headers + "\r\n\r\n" + status)
    server.quit()


def normalize_url(url):
    """
    If a url doesn't have a http/https prefix, add http://
    """
    if not re.match('^http[s]?://', url):
        url = "http://" + url
    return url


def test(url):
    """
    First check the internet connection if it's on then check the requested url.
    """
    if connection_is_on():
        site_is_up = get_status(url)
        if site_is_up:
            pass
        else:
            status = '%s is down!' % url
            email_alert(status)
    else:
        print('Internet connection is down!')


def periodic(sh_clr, per_int, action, action_args):
    """
    Scheduler to check server status in given time intervals.
    """
    sh_clr.enter(per_int, 1, periodic,
                 (sh_clr, per_int, action, action_args))
    action(action_args)


if __name__ == '__main__':
    SITE_URL = argv[1]
    INTERVAL = int(argv[2])
    periodic(SCHEDULER, INTERVAL, test, SITE_URL)

    T = threading.Thread(target=SCHEDULER.run)
    T.start()
