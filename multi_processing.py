#!/usr/bin/env python
from multiprocessing.pool import ThreadPool
from time import time as timer
import requests

urls = ["http://www.google.com", "http://www.apple.com", "http://www.microsoft.com", "http://www.amazon.com", "http://www.facebook.com",
"http://www.google.com", "http://www.apple.com", "http://www.microsoft.com", "http://www.amazon.com", "http://www.facebook.com",
"http://www.google.com", "http://www.apple.com", "http://www.microsoft.com", "http://www.amazon.com", "http://www.facebook.com",
"http://www.google.com", "http://www.apple.com", "http://www.microsoft.com", "http://www.amazon.com", "http://www.facebook.com","http://www.google.com", "http://www.apple.com", "http://www.microsoft.com", "http://www.amazon.com", "http://www.facebook.com",
"http://www.google.com", "http://www.apple.com", "http://www.microsoft.com", "http://www.amazon.com", "http://www.facebook.com",
"http://www.google.com", "http://www.apple.com", "http://www.microsoft.com", "http://www.amazon.com", "http://www.facebook.com",
"http://www.google.com", "http://www.apple.com", "http://www.microsoft.com", "http://www.amazon.com", "http://www.facebook.com",
"http://www.google.com", "http://www.apple.com", "http://www.microsoft.com", "http://www.amazon.com", "http://www.facebook.com","http://www.google.com", "http://www.apple.com", "http://www.microsoft.com", "http://www.amazon.com", "http://www.facebook.com",
"http://www.google.com", "http://www.apple.com", "http://www.microsoft.com", "http://www.amazon.com", "http://www.facebook.com",
"http://www.google.com", "http://www.apple.com", "http://www.microsoft.com", "http://www.amazon.com", "http://www.facebook.com",
"http://www.google.com", "http://www.apple.com", "http://www.microsoft.com", "http://www.amazon.com", "http://www.facebook.com",
"http://www.google.com", "http://www.apple.com", "http://www.microsoft.com", "http://www.amazon.com", "http://www.facebook.com","http://www.google.com", "http://www.apple.com", "http://www.microsoft.com", "http://www.amazon.com", "http://www.facebook.com"]

def fetch_url(url):
    try:
        verb = 'GET'
        uri = url

        resp = requests.request(
            verb,
            url=uri
            )
        return url,resp,None
    except Exception as e:
        return url, None, e


def parallelProcessing():
    start = timer()
    results = ThreadPool(20).imap_unordered(fetch_url, urls)
    for url, html, error in results:
        if error is None:
            print("%r fetched in %ss" % (url, timer() - start))
            print(html)
        else:
            print("error fetching %r: %s" % (url, error))
    print("Elapsed Time: %s" % (timer() - start,))


def sequentialProcessing():
    start = timer()
    for url in urls:
        _url,html,error = fetch_url(url)
        print("%r fetched in %ss" % (url, timer() - start))
        print(html)
    print("Elapsed Time: %s" % (timer() - start,))


print("Sequential calling....")

sequentialProcessing()

print("\n")

print("=================================================================\n")

print("parallel calling....")

parallelProcessing()