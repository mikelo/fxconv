#!/usr/bin/python3

import urllib3
from xml.dom.minidom import parseString
from flask import Flask
app = Flask(__name__)
from flask import request

http = urllib3.PoolManager()
eurofxref = {}
date = None
xmlresponse = http.request('GET', 'https://www.ecb.europa.eu/stats/eurofxref/eurofxref-hist-90d.xml')
xmlresponse = parseString(xmlresponse.data)
for i in xmlresponse.getElementsByTagName('Cube'):
    # print(dir(i))
    if i.hasAttribute('time'):
        date = i.getAttribute('time')
        eurofxref[date] = {}
    elif i.hasAttribute('currency') and i.hasAttribute('rate'):
        eurofxref[date][i.getAttribute('currency')] = float(i.getAttribute('rate'))

@app.route('/convert')
def convert():
    response = {}
    euro = 1
    try:
        src = request.args.get('src​_currency')
        dest = request.args.get('dest​_currency')
        amount = float(request.args.get('amount'))
        date = request.args.get('re​ference_date')
        euro = amount
        if src != 'EUR':
            euro = amount / eurofxref[date][src]
        amount = euro
        if dest != 'EUR':
            amount = eurofxref[date][dest] * euro
        response['currency'] = dest
        response['amount'] = amount
    except Exception as ex:
        response['error message'] = repr(ex)
    return response
