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
    return [mgroups[0] for mgroups in URL_PATTERN.findall(s)]

def validurl(s):
    return bool(URL_PATTERN.match(s))

def join(x, y):
    return y.join(x)

def truncate(s, length):
    return '%s ...' % s[:length] if len(s) > length else s

def markdown(html, safe_mode=True, replace_with=''):
    return md.Markdown(safe_mode=safe_mode,
                       html_replacement_text=replace_with).convert(html)
