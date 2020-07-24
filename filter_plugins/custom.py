#!/usr/bin/python

def search_for_key(stdout_lines, key):
    for i in stdout_lines:
        if key in i:
            return i.split(":")[-1].strip()
    return ""

class FilterModule(object):
    def filters(self):
        return {
            "search_for_key": search_for_key
        }
