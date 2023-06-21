#!/usr/bin/env python3
#
# Forked from
# https://github.com/kragen/xcompose/blob/master/scan4dups.py

import re
import sys

entries: dict[str, str] = dict()
values: set[str] = set()

print("Parsing input...")

for line in sys.stdin:
	# print "((%s))"%line
	startpos = 0
	name = ''
	# dups: list = []
	while True:
		m = re.match(r"\s*<(\w+)>", line[startpos:])
		if not m:
			break
		word = m.group(1)
		name += ' ' + word
		startpos += m.end()
	if startpos <= 0:
		continue
	m = re.match(r'[^"]*"(.+)"', line)
	if not m:
		# Shouldn't happen, but just in case
		val = '???'
		print("Couldn't make sense of line: " + line)
	else:
		val = m.group(1)
		values.add(val)
	if name in entries:
		if val != entries[name]:
			print("Exact conflict found: (%s ) [%s] [%s]"%(name, entries[name], val))
		else:
			print("\tRedundant definition: (%s ) [%s]"%(name, val))
	else:
		entries[name] = val

print("Done.")
print("Checking prefixes...")

for key in entries.keys():
	# print "Key: (%s)"%key
	pref = ''
	# Careful when splitting. The key always starts with a space.
	for word in key.split(" ")[:-1]:	# chop the last one; that'll always match
		# Skip the empty first entry
		if not word:
			continue
		pref += " " + word
		# print "checking (%s)"%pref
		if pref in entries:
			print("Prefix conflict found: "
				  "(%s ) [%s] vs. (%s ) [%s]"%(pref, entries[pref], key, entries[key]))

print("Done.")
print("%s entries total"%len(entries))
print("%s unique characters"%len(values))
