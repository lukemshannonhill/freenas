#!/usr/bin/env python3.6

# Author: Eric Turgeon
# License: BSD

import sys
import os
apifolder = os.getcwd()
sys.path.append(apifolder)
from functions import GET, POST


def test_01_get_core_services():
    results = GET('/core/get_services/')
    assert results.status_code == 200, results.text
    assert isinstance(results.json(), dict) is True
    global services
    services = results


def test_02_get_ssh_type_service():
    assert services.json()['ssh']['type'] == 'config', services.text


def test_03_get_core_methods():
    results = POST('/core/get_methods/')
    assert results.status_code == 200, results.text
    assert isinstance(results.json(), dict) is True


def test_04_get_core_jobs():
    results = GET('/core/get_jobs/')
    assert results.status_code == 200, results.text
    assert isinstance(results.json(), list) is True


def test_05_get_core_ping():
    results = GET('/core/ping/')
    assert results.status_code == 200, results.text
    assert isinstance(results.json(), str) is True
    assert results.json() == 'pong'