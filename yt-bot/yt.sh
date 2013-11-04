#!/bin/sh

# requires youtube-dl and avconv

youtube-dl -x --audio-format mp3 --audio-quality 192K "$@"
