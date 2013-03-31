#!/bin/sh

# requires youtube-dl and avconv

ID="$1"

if [ -z "$ID" ]; then
echo "$0 "
echo "Example: $0 PryP9IRTJLo"

exit 1
fi

YT="http://www.youtube.com/watch?v=$ID"

echo "Downloading video..."
MP4=`youtube-dl -t $YT | grep "Destination:" | awk '{print $3}'`

echo "Converting to mp3..."
avconv -i "$MP4" -f mp3 -ab 192000 -vn "$MP4.mp3"

rm -f "$MP4"
echo "YouTube Link: $YT"
echo "Downloaded video to file: $MP4"

