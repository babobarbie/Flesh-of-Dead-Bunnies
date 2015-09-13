from flask import Flask,render_template
import sodapy
import time
import datetime
import csv
import re
import sys
import numpy as np
import json

#backend: gets data from baltimore open data, processes everything. should turn into a class later
baltimore=sodapy.Socrata('data.baltimorecity.gov','LVq4aS6jaUvEi55ssKd2BRca3',username="thegoofyguber@gmail.com",password='12TTfbicc89!')
vacancy=baltimore.get('/resource/qqcv-ihn5.csv')
crime=baltimore.get('/resource/wsfq-mvij.csv')

#crime heatmap algorithm
vacancymap=[]
crimelat=[]
crimelong=[]
crimemap=[]
current=time.time()
crimetime=[]
poop=range(1,1001)
heat=[]
gps=(39.2, 76.6)

#vacancy 5th column is the latitude longitude
#crime 9th column is the latitude longitude
#crime 4th column is type of crime

for i in range(1,1001):
	result = re.findall(r'[0-9.]+', vacancy[i][5])
	lat=float(result[0])
	lon=float(result[1])
	vacancymap=vacancymap+[(lat, lon)]

for i in range(1,1001):
	result = re.findall(r'[0-9.]+', crime[i][9])
	if result != []:
		lat=float(result[0])
		lon=float(result[1])
		crimemap=crimemap+[(lat, lon)]
		crimelat=crimelat+[lat]
		crimelong=crimelong+[lon]
	else:
		poop.remove(i)

for i in poop:
	temptime=time.mktime(datetime.datetime.strptime(crime[i][0], "%m/%d/%Y").timetuple())
	crimetime=crimetime+[(current-temptime)]

for j in range(0,1000):
	for i in range(0,len(poop)):
		oneheat=0
		oneheat=oneheat+(1000000/crimetime[i])*np.exp((np.power((vacancymap[j][0]-crimemap[i][0]),2)+(np.power((vacancymap[j][1]-crimemap[i][1]),2)))/.016)
	heat=heat+[oneheat]

outjson={}
for i in range(0,len(vacancymap)):
    outjson.update({i:(vacancymap[i][0], vacancymap[i][1], heat[i])})

givevacancy=json.dumps(outjson)

heatmap = []
for i in range(0,len(crimetime)):
	heatmap.append((1000000/crimetime[i]))

# jsonheat={"ListofCrimes": heatmap}

# tojsoncrime=json.dumps(jsonheat)

#app starts here
app = Flask(__name__)

@app.route("/")
def main():
	return render_template('mapmap.html', crimelat=crimelat, crimelong=crimelong, crimeheat=heatmap)


if __name__ == "__main__":
	app.run()