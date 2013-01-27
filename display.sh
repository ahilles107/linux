#!/bin/bash
#
# author: maciej plonski / mplonski / sokoli.pl
# licence: GNU GPL
#
# changing screen resolution to 1920x1080 if there's
# any screen connected using HDMI and to 1024x600
# when it can't find any connected using HDMI
# (useful for laptops when screen resolution
# auto-set is not correctly working)
#
# add to your desktop environment's autostart
#
xrandr |grep HDMI-0 |grep " connected "
if [ $? -eq 0 ]; then
    xrandr --output HDMI-0 --auto --mode 1920x1080
    xrandr --output LVDS --off
    xrandr --output HDMI-0 --auto --mode 1920x1080
else
    xrandr --output LVDS --mode 1024x600
fi

