#!/bin/bash
#
# author: maciej plonski / mplonski / sokoli.pl
# licence: GNU GPL
#
# changing screen resolution to 1920x1080 if there's
# one connected using HDMI and to 1024x600 when it can't
# find any connected (useful for laptops when screen
# resolution auto-set is not correctly working)
#
# add to your desktop environment's autostart
#
# Waring!
# use xrandr to know how is your external montior named!
# change LVDS to the name of the internal monitor and DFP1
# to the name of the external monitor
#

xrandr |grep DFP1 |grep " connected "
if [ $? -eq 0 ]; then
    xrandr --output DFP1 --auto --mode 1920x1080
    xrandr --output LVDS --off
    xrandr --output DFP1 --auto --mode 1920x1080
else
    xrandr --output LVDS --mode 1024x600
fi

