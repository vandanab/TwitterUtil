'''
Created on Feb 26, 2013
@author: vandana
'''
import os

#basedir = os.path.expanduser('~/workspace/LocalExperts/data/results/%s/')
basedir = os.path.expanduser('~/LocalExperts/data/results/%s/')
hdfs_basedir = 'hdfs:///user/vbachani/data/results/%s/'

#noun_cloud_input = basedir % 'local_tweets' + 'tweets_for_analysis' 
noun_cloud_input = hdfs_basedir % 'local_tweets' + 'tweets_for_analysis'
noun_cloud_output = basedir % 'local_tweets' + 'noun_cloud'