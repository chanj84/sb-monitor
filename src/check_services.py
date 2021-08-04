#!/usr/bin/env python3

import json
import sys
import os

from src.service_requests import ServiceRequests


check_host = os.environ.get('check_host')

status_keys = ['status']
status_down = ['DOWN', 'UNKNOWN']

errors = { 'status': [] }

stack = ['service']


def get_host_data():
    request = ServiceRequests(check_host)
    response = request.run_request()
    try:
        return json.loads(response.data.decode('utf-8'))
    except:
        return None

def parse_status(json):
    if isinstance(json, dict):
        for k, v in json.items():
            if k in status_keys:
                check_status(stack.pop(), v)
            else:
                stack.append(k)
                parse_status(v)

def check_status(service, status):
    dict_status = { service: status }
    if status in status_down:
        errors['status'].append(dict_status)

def report_errors(errors):
    if errors['status']:
        print(json.dumps(errors, indent=2))
        sys.exit(2)
    else:
        print('OK')

response_json = get_host_data()
parse_status(response_json)
report_errors(errors)
