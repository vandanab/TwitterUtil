'''
Created on Feb 26, 2013
@author: vandana
for running mrjob script
'''
from library.mrjobwrapper import runMRJob
from src.constellations.nouncloud import POSTagger
from src.constellations.settings import noun_cloud_input, noun_cloud_output

class NounCloudMRJobRunner(object):
  @staticmethod
  def noun_extractor(input_files):
    mr_class = POSTagger
    output_file = noun_cloud_output
    runMRJob(mr_class,
             output_file,
             # uncomment when running on local
             #fs.get_local_input_files(local_tweets_input_folder),
             input_files,
             mrJobClassParams = {'job_id': 'as'},
             # uncomment when running on local
             #args = [],
             jobconf={'mapred.reduce.tasks':300, 'mapred.task.timeout': 86400000}
    )
  
  @staticmethod
  def run():
    input_files = [noun_cloud_input]
    NounCloudMRJobRunner.noun_extractor(input_files)

if __name__ == '__main__':
  NounCloudMRJobRunner.run()
