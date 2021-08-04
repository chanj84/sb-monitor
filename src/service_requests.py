#!/usr/bin/env python3

import sys
import urllib3


class ServiceRequests:

    def __init__(self, host):
        self.host = host

    def run_request(self):
        url = '{host}'.format(host=self.host)
        http = urllib3.PoolManager()
        try:
            response = http.request('GET', url)
        except:
            print('Unable to connect to {url}'.format(url=url))
            sys.exit(2)
        return response
