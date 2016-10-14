#-*-coding: utf-8 -*-

"""
    utils
    ~~~~~

    General project independent utilities
"""

import re
import markdown as md

URL_PATTERN = re.compile(ur'(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z0-9.\-]{0,3}|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'".,<>?\xab\xbb\u201c\u201d\u2018\u2019]))')

def findurls(s):
    """
    """
    return [mgroups[0] for mgroups in URL_PATTERN.findall(s)]

def validurl(s):
    """
    """
    return bool(URL_PATTERN.match(s))

def truncate(s, length):
    return '%s ...' % s[:length] if len(s) > length else s

def join(lst, delim):
    return delim.join(lst)

def markdown(html, safe_mode=True, replace_with=''):
    return md.Markdown(safe_mode=safe_mode,
                       html_replacement_text=replace_with).convert(html)

def commify(n):
    """
    Add commas to an integer `n`.

    >>> commify(1)
    '1'
    >>> commify(123)
    '123'
    >>> commify(1234)
    '1,234'
    >>> commify(1234567890)
    '1,234,567,890'
    >>> commify(123.0)
    '123.0'
    >>> commify(1234.5)
    '1,234.5'
    >>> commify(1234.56789)
    '1,234.56789'
    >>> commify('%.2f' % 1234.5)
    '1,234.50'
    >>> commify(None)
    >>>
    """
    if n is None: return None
    n = str(n)
    if '.' in n:
        dollars, cents = n.split('.')
    else:
        dollars, cents = n, None

    r = []
    for i, c in enumerate(str(dollars)[::-1]):
        if i and (not (i % 3)):
            r.insert(0, ',')
        r.insert(0, c)
    out = ''.join(r)
    if cents:
        out += '.' + cents
    return out
