#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This script generates random slovenian tax numbers.
It was written to test a bug in slovenian tax validator in django-localflavor==1.2
"""
import random

def si_tax_control_number(tax):
    """ Calculate tax control number from first 7 digits """

    # Calculate control number
    s = 0
    int_values = [int(i) for i in tax]
    for a, b in zip(int_values, range(8, 1, -1)):
        s += a * b
    chk = 11 - (s % 11)

    # If control number is 10 or 11 set it to zero
    chk_updated = 0 if chk in (10, 11) else chk

    return chk, chk_updated

def si_tax_generate():
    """ Generate single random tax number """
    
    # Random string - 8 digits, leading digit without zero
    d = '';
    d += random.choice('123456789')
    for _ in range(8):
        d += random.choice('0123456789')

    # 8. digit is control number - calculate and update
    chk, chk_updated = si_tax_control_number(d)
    d = d[:7] + str(chk_updated)

    return d, chk, chk_updated

# Generate tax numbers
if __name__ == "__main__":
    nr = int(raw_input('How many numbers should I create [1]: ') or 1)
    for i in range(nr):
        d, chk, chk_updated = si_tax_generate()
        print "%s [cn=%s]" % (d, chk)
