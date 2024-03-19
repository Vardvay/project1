!/usr/bin/env python3

import cgi

our_form = cgi.FieldStorage ()

in_comment = our_form.getfirst("in_comment", "не задано")

print("Content-type: text/html")
print()
print(in_comment)
