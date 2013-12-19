
 #streams live music from iheart radio using the rtmp link
#mplayer "rtmp://cp19971.live.edgefcs.net/live/Nyo_NY_WAXQ-FM_OR@s7907?auth=daEbqdWcRa3c_b2bzaTcjbFdmcKaHdsasdy-bsS09n-4q-RO5X3_6poEEor1HCwkwuyr&aifp=1234&CHANNELID=1465&CPROG=SIMULCAST&MARKET=NEWYORK-NY&REQUESTOR=WAXQ-FM&SERVER_NAME=service.ccrd.clearchannel.com&SITE_ID=1674&STATION_ID=WAXQ-FM&MNM=2&TYPEOFPLAY=0}"

import subprocess
import time
import urllib2
import json


station=raw_input("Enter the 4 digit stream number")
data = urllib2.urlopen('http://www.iheart.com/a/live/station/'+station+'/stream/','1')



