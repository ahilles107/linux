#! /bin/sh
# Description:		unloads kernel modules (wifi - wifi modules, etc)
# Requires:		sudo, modprobe
# Author:		maciej plonski / mplonski / sokoli.pl 
#
# Warining! Works only with atheros (wifi module) and r8169 (eth module).
# Do inspire and check with kernel modules loaded in your system!
#

case "$1" in
  eth)
	sudo modprobe -r r8169
	sudo modprobe -r mii
	sudo modprobe -r toshiba_bluetooth
	sudo echo "Done (wifi)"
  ;;
  wifi)
	sudo modprobe -r mii
	sudo modprobe -r toshiba_bluetooth
	sudo modprobe -r ath9k_common
	sudo modprobe -r ath9k_hw
	sudo modprobe -r ath9k
	sudo modprobe -r mac80211
	sudo modprobe -r ath
	sudo modprobe -r cfg80211
	echo "Done (eth)"
  ;;
  all)
	$0 wifi
	$0 eth
	echo "Done (all)"
  ;;
  load)
	sudo modprobe r8169
	sudo modprobe mii
	sudo modprobe toshiba_bluetooth
	sudo modprobe ath9k_common
	sudo modprobe ath9k_hw
	sudo modprobe ath9k
	sudo modprobe mac80211
	sudo modprobe ath
	sudo modprobe cfg80211
	echo "Done (load)"
  ;;
  *|help)
        echo "Usage: battery {wifi|eth|all|load|help}"
        exit 1
  ;;
esac

exit 0
