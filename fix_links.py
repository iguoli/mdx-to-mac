#!/usr/bin/env python3


import xml.etree.ElementTree as ET

'''
1. find the d:entry node which descendant contains the keyword "@@@LINK=" in text
2. parse the value behind "@@@LINK=" keyword and save it to variable title
3. save the index node belongs to the d:entry to variable index
4. find the d:entry node which title property exactly matches title
5. append index to the current d:entry node as child
6. remove the d:entry which descendant contains the keyword "@@@LINK="

NOTE: please remove the default namespace from oald8.xml file manually before the script running
and add it back when script done.
'''

tree = ET.parse('./oald8.xml')
root = tree.getroot()

ns = {'d': 'http://www.apple.com/DTDs/DictionaryService-1.0.rng'}
ET.register_namespace('d', 'http://www.apple.com/DTDs/DictionaryService-1.0.rng')

# find all d:entry nodes which contains the keyword "@@@LINK=" in text
link_entries = root.findall('.//p/..', ns)

for l_entry in link_entries:
    index = l_entry.find('./d:index', ns)
    title = l_entry.find('./p', ns).text.replace('@@@LINK=', '')
    entry = root.find('./d:entry[@d:title="' + title + '"]', ns)

    # remove l_entry directly if title cannot be found in entries
    if entry is None:
        print(title)
        root.remove(l_entry)
        continue

    # append the index element to right entry
    entry.insert(0, index)
    root.remove(l_entry)

tree.write('oald8f.xml', 'UTF-8')
