#!/usr/bin/env python
"""This script tests django.localflavor==1.2 for tax number validations for slovenia (SI)

Control number calculation example:
    tax = "1234567X"
    SUM = 1*8 + 2*7 + 3*6 + 4*5 + 5*4 + 6*3 + 7*2
    X = 11 - (SUM mod 11)
    if X=10 or X=11 then X=0
"""
from localflavor.si.forms import SITaxNumberField
from tax_generator import si_tax_control_number
import sys

# Theese numbers were randomly generated
TEST_TAX_NUMBERS = [
    '81652941', # cn=1
    '43907172', # cn=2
    '31212123', # cn=3
    '49649094', # cn=4
    '95831185', # cn=5
    '29702216', # cn=6
    '58271007', # cn=7
    '40870308', # cn=8
    '14045559', # cn=9
    '94536040', # cn=10 -> 0
    '25215930', # cn=11 -> 1 (This should validate OK in django-localflavor==1.2, but it does not)
]

for tax in TEST_TAX_NUMBERS:
    chk, chk_updated = si_tax_control_number(tax)
    sys.stdout.write("Testing tax %s [chk=%s, chk_updated=%s]\t" % (tax, chk, chk_updated))
    try:
        # Validate tax number with django-localflavor
        SITaxNumberField().clean(tax)
        print "OK"
    except:
        print "ERROR"
