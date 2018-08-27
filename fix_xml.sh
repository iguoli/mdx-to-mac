#!/usr/bin/env bash


# fix abs path to relative path
head -100 oald8.xml | perl -p -e 's:src="/:src=":g' | grep 'src="'

# fix sound link
head -100 oald8.xml | perl -p -e 's,<a class="fayin" href="x-dictionary:d:sound://(u[sk]/)(.+?).mp3">(.+?img.+?)/></a>,<audio class="fayin" id="\2" src="\1\2.mp3"/>\3 onmousedown="document.getElementById('\''\2'\'').play(); return false;" onmouseover="" style="cursor: pointer;"/>,g' | grep -E '<audio.+?img.+?/>'

# fix entry://
head -100 oald8.xml | perl -p -e 's,entry://,,g' | grep 'entry://'

# fix x-dictionary:d:word#ref to x-dictionary:d:word:#ref
head -100 oald8.xml | perl -p -e 's/x-dictionary:d:(.{1,20})(#.+?")/x-dictionary:d:\1:\2/g' | grep -E 'x-dictionary:d:.+?:.+?"'

# fix word reference
# head -100 oald8.xml | perl -p -e 's,\@\@\@LINK=(.+?)</p>,<a href="x-dictionary:d:\1:dict_bundle_id">\1</a></p>,'
# run ./fix_links.py manually
