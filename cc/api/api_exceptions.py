## Copyright (c) 2010, John Doig, Creative Commons

## Permission is hereby granted, free of charge, to any person obtaining
## a copy of this software and associated documentation files (the "Software"),
## to deal in the Software without restriction, including without limitation
## the rights to use, copy, modify, merge, publish, distribute, sublicense,
## and/or sell copies of the Software, and to permit persons to whom the
## Software is furnished to do so, subject to the following conditions:

## The above copyright notice and this permission notice shall be included in
## all copies or substantial portions of the Software.

## THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
## IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
## FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
## AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
## LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
## FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
## DEALINGS IN THE SOFTWARE.

import lxml.etree as ET

def _error_tree(error_id, message):
    error = ET.Element('error')
    ET.SubElement(error, 'id').text = error_id
    ET.SubElement(error, 'message').text = message
    return error

def invalidclass():
    return _error_tree('invalidclass', 'Invalid License Class.')

def invalidjurisdiction():
    return _error_tree('invalidjurisdiction', 'Invalid License Jurisdiction.')

def invaliduri():
    return _error_tree('invaliduri', 'Invalid license uri.')

def invalidanswer():
    return _error_tree('invalidanswer', 'Invalid answer in answers.')

def pythonerr():
    return _error_tree('pythonerr', 'An internal Python excpetion occurred.')

def missingparam(param):
    return _error_tree('missingparam',
                       'A value for %s must be supplied.' % param )
