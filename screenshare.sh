#!/bin/sh

# Apple remote Desktop sometimes is buggy and doesn't work
# This always seems to work.

/usr/bin/osascript -e 'tell application "Screen Sharing" to GetURL "vnc://dnsname.local"'
