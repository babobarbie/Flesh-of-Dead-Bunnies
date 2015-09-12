import heatmap
import random
import sodapy

baltimore=sodapy.Socrata('data.baltimorecity.gov','LVq4aS6jaUvEi55ssKd2BRca3',username="thegoofyguber@gmail.com",password='12TTfbicc89!')
vacancy=baltimore.get('/resource/qqcv-ihn5.json')
crime=baltimore.get('/resource/4ih5-d5d5.json')

#vacancy 5th column is the latitude longitude
#crime 9th column is the latitude longitude
#crime 4th column is type of crime

hm = heatmap.Heatmap()
img = hm.heatmap(pts)
img.save("baltimorecrime.png")
