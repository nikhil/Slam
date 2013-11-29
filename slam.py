#!/usr/bin/env python
 
import subprocess
import time
import urllib2
import xml.etree.ElementTree as ET
import os
import datetime
 
#Location of Stream to be SAVED
DefaultStation="wtfx-fm"
 
def getXML():
    data=urllib2.urlopen('http://p2.'+station+'.ccomrcdn.com/player/player_dispatcher.html?section=radio&action=listen_live').read()
    xml=ET.fromstring(data)
    return xml
 
def getSongInfo():
    xml=getXML()
    artist=xml.find('ListenLiveInitialize/JustPlayed/song/artist').attrib['name']
    title=xml.find('ListenLiveInitialize/JustPlayed/song/track').attrib['track_title']
    return artist,title
 
 
 
while True:
    station=raw_input("Enter Station ID [" + DefaultStation + "]: ")
 
    if not station:
        station=DefaultStation
    try:
        xml=getXML()
    except urllib2.URLError:
        print "Error - Invalid Station ID or Web Server Problem - Try Again"
    else:
        break
 
while True:
    try:
        TIME=int(raw_input("Time Stream will Play (in minutes): "))
    except ValueError:
        print "Error - Invalid Time - Try Again"
    else:
        break
 
rtmpurl=xml.find("ListenLiveInitialize/StreamInfo/stream").attrib['primary_location']
 
mp=subprocess.Popen(['/usr/bin/mplayer', rtmpurl, '-novideo', '-ao', 'alsa', '-quiet'], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
mpPID=mp.pid
 
endTime = datetime.datetime.now() + datetime.timedelta(minutes=TIME)
 
OldSongInfo=[]
 
while datetime.datetime.now() < endTime:
    SongInfo=getSongInfo()
    if not SongInfo == OldSongInfo:
        OldSongInfo = SongInfo
        print SongInfo[0] + " - " + SongInfo[1]
    time.sleep(5)
 
 
 
print("Stopping MPlayer...")
os.kill(mpPID, 2)
 
print "Done"
