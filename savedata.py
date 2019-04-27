#!/usr/bin/python

import sys
import requests

value = sys.argv[1]
requests.post('http://lakshmick.pythonanywhere.com/savedata', data = {'string': value})



