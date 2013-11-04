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
MP4=`youtube-dl -t $YT | grep "Destination:" | awk '{ for (i = 3; i <= NF; i++) { printf("%s ", $i); } }' | rev | cut -c 2- | rev`
MP3=`echo "$MP4" | rev | cut -c 5- | rev`

echo "Converting to mp3..."
avconv -i "$MP4" -f mp3 -ab 192000 -vn "$MP3.mp3"

echo "Removing all .flv/.mp4..."
ls ./ | grep ".mp4$\|.flv$" | while read line; do rm -f "./$line"; done

echo "Done! Saved file to $MP3.mp3"

