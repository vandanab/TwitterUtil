'''
Created on Jan 25, 2013
@author: vandana
Important utilities for processing tweets
1. Language detection for tweets, based on the language supported by twitter
'''
import httplib2
import cjson
import zipfile
from langdetect import LangDetect

class LangDetectTwitter:
  def __init__(self):
    http = httplib2.Http()
    langurl = "https://api.twitter.com/1/help/languages.json"
    hdr, content = http.request(langurl, 'GET')
    if hdr["status"] == "200":
      content = cjson.decode(content)
      supported_langs = [x["code"] for x in content]
      #print "Languages supported: ", supported_langs
      valid_langs = []
      f = zipfile.ZipFile("/home/vbachani/nltk_data/corpora/langid.zip", "r")
      for i in supported_langs:
        fname = "langid/" + i + "-3grams.txt"
        if fname in f.namelist():
          valid_langs.append(i)
      self.langs = valid_langs
      self.ld = LangDetect(valid_langs)
    else:
      self.ld = LangDetect()

  def detect(self, texts):
    result = []
    for text in texts:
      result.append(self.ld.detect(text))
    return result
	
def twitter_langs():
	ld = LangDetectTwitter()
	print ld.langs

if __name__ == "__main__":
	twitter_langs()
