'''
Created on Feb 27, 2013
@author: kykamath, vandana
get reduced size geo tweets (only english tweets)
'''
import os, gzip, cjson
from library.geo import getCenterOfMass
from library.file_io import FileIO

us_boundary = [[24.527135, -127.792969], [49.61071, -59.765625]]
year = '2012'
checkinsFile = 'checkins/%s' % year + '_%s'
# checkinsFile = '/mnt/chevron/dataset/twitter/reduced_geo/%s'%year+'_%s'

def tweetFilesIterator():
  bdeDataFolder = '/mnt/chevron/bde/Data/TweetData/GeoTweets/%s' % year + '/%s/%s/'
  for month in range(1, 12):
    outputFile = checkinsFile % month
    for day in range(1, 32):
      tweetsDayFolder = bdeDataFolder % (month, day)
      if os.path.exists(tweetsDayFolder):
        for _, _, files in os.walk(tweetsDayFolder):
          for f in files:
            yield outputFile, tweetsDayFolder + f

def getCheckinObject(data):
  checkin = {'user': {'id': data['user']['id'], 'l': data['user']['location'],
             'lg': data['lang']}, 'id': data['id'], 't': data['created_at'],
             'h': [], 'ats': [], 'tx': data['text']}
  for h in data['entities']['hashtags']: checkin['h'].append(h['text'])
  for at in data['entities']['user_mentions']: checkin['ats'].append(at['screen_name'])
  return checkin

def getGeoData(data):
  if 'geo' in data and data['geo'] != None: return ('geo', data['geo']['coordinates'])
  elif 'place' in data: 
    point = getCenterOfMass(data['place']['bounding_box']['coordinates'][0])
    return ('bb', [point[1], point[0]])

for outputFile, f in tweetFilesIterator():
  print 'Parsing: %s' % f
  for line in gzip.open(f, 'rb'):
    # try:
    data = cjson.decode(line)
    geo = getGeoData(data)
    if geo and data['user']['lang'] == "en":  # and isWithinBoundingBox(geo[1], us_boundary): 
      checkin = getCheckinObject(data)
      checkin[geo[0]] = geo[1]
      #print checkin
      FileIO.writeToFileAsJson(checkin, outputFile)
    #except Exception as e:
      #print line
      #print e
