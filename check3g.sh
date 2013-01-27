#!/bin/bash
# ksx4system's 3G simple monitoring script
# 		version 0.2
#
# ksx4system@sverige:~$ date
# Thu Jan  5 12:48:27 CET 2012
spacer='--------------------------------------------------'
function linecleanup
{
awk '{sub(/^[ \t]+/, "")};1'
}
function getipaddr
{
ip addr show ppp0 | grep inet | linecleanup
}
function check3gstatus
{
echo -n "Duration of current 3G session: " ;
ps -eo etime,cmd | grep ppp | awk '{ print $1 }' | head -n 1
echo $spacer
ifconfig ppp0 | grep bytes | linecleanup | sed 's/TX/\n&/g'
echo $spacer
echo -n "IP address: " ;
getipaddr | awk '{ print $2 }'
echo -n "Routing via: " ;
getipaddr | awk '{ print $4 }'
}
# here comes Notify OSD magic
notify-send '3G wireless broadband stats' "`check3gstatus`"
#
#Copyright 2011 Krzysztof 'ksx4system' Staniorowski. All rights reserved.
#
#Redistribution and use in source and binary forms, with or without modification, are
#permitted provided that the following conditions are met:
#
#   1. Redistributions of source code must retain the above copyright notice, this list of
#      conditions and the following disclaimer.
#
#   2. Redistributions in binary form must reproduce the above copyright notice, this list
#      of conditions and the following disclaimer in the documentation and/or other materials
#      provided with the distribution.
#
#THIS SOFTWARE IS PROVIDED BY Krzysztof Staniorowski ''AS IS'' AND ANY EXPRESS OR IMPLIED
#WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND
#FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL <COPYRIGHT HOLDER> OR
#CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
#CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
#SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
#ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
#NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF
#ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
#The views and conclusions contained in the software and documentation are those of the
#authors and should not be interpreted as representing official policies, either expressed
#or implied, of <copyright holder>.
