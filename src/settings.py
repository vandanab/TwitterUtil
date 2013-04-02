import os
hdfs_input_folder = 'hdfs:///user/vbachani/data/results/%s/'
local_data_folder = os.path.expanduser('~/LocalExperts/data/results/%s/')
#hdfs_input_folder = '%s/'

hdfs_local_tweets_input = hdfs_input_folder % 'local_tweets' + 'tweets_for_analysis'
hdfs_local_tweets_output = local_data_folder % 'local_tweets' + 'tweets_for_analysis_modified'
