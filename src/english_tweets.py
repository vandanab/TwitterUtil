"""
filter english tweets from the location tweets collected
"""
import cjson
import sys
from twitter_util import LangDetectTwitter

def filter(infile, outfile):
	ld = LangDetectTwitter()
	f = open(infile, 'r')
	f1 = open(outfile, 'w')
	for l in f:
		data = cjson.decode(l)
		lang = ld.detect([data['tx']])
		if lang == ['en']:
			f1.write(l)
	f1.close()
	f.close()

def main():
	infile = '/mnt/chevron/vbachani/data/results/local_tweets/tweets'
	outfile = '/home/vbachani/TwitterUtil/src/tweets_en'
	if len(sys.argv) >= 2:
		infile = sys.argv[1]
	print "start filtering... ", infile
	filter(infile, outfile)

if __name__ == "__main__":
	main()
