
 #streams live music from iheart radio using the rtmp link
#mplayer "rtmp://cp19971.live.edgefcs.net/live/Nyo_NY_WAXQ-FM_OR@s7907?auth=daEbqdWcRa3c_b2bzaTcjbFdmcKaHdsasdy-bsS09n-4q-RO5X3_6poEEor1HCwkwuyr&aifp=1234&CHANNELID=1465&CPROG=SIMULCAST&MARKET=NEWYORK-NY&REQUESTOR=WAXQ-FM&SERVER_NAME=service.ccrd.clearchannel.com&SITE_ID=1674&STATION_ID=WAXQ-FM&MNM=2&TYPEOFPLAY=0}"

import subprocess
import time
import json
import requests
import pprint

station=raw_input("Enter the 4 digit stream number")
data = requests.post('http://www.iheart.com/a/live/station/'+station+'/stream/',stream=True).json()
rtmp = data[u'stream_urls'][u'rtmp']
name = data[u'info'][u'station_name']
#cmd = 'rtmpdump -r '+rtmp + ' -v | mplayer' 
#subprocess.call(cmd.split(),shell=False)
mp=subprocess.Popen(['mplayer', rtmp, '-novideo', '-ao', 'alsa'], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
mpPID=mp.pid





