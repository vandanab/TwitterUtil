#!/usr/bin/env python
# encoding: utf-8
'''
Created on Feb 22, 2013
@author: vandana
“We all shine on...like the moon and the stars and the sun...
we all shine on...come on and on and on...” 
― John Lennon
The module tries to construct a noun graph (constellations) which connect
the nouns which co-occur and hence are related.
TweetSpace (going with this for now) or wikipedia?

Steps:
Collect documents
Do POS tagging using nltk
take nouns and create noun dict
construct a graph with connections
'''
import nltk
import cjson
from library.mrjobwrapper import ModifiedMRJob

class POSTagger(ModifiedMRJob):
  """
  Processes the documents (tweets) by first pos tagging then getting rid of all
  words except nouns (lower case, remove stop words)
  """
  DEFAULT_INPUT_PROTOCOL = 'raw_value'

  def __init__(self, *args, **kwargs):
    super(POSTagger, self).__init__(*args, **kwargs)
    grammar = r"""NP: {<DP>?<JJ>+<NN.*>+}
                      {<NN.*>+}
              """
    self.cp = nltk.RegexpParser(grammar)
  """
  def __init__(self):
    grammar = "NP: {<NN.*>+}"
    self.cp = nltk.RegexpParser(grammar)
  """

  def mapper(self, key, line):
    data = cjson.decode(line)
    tx = data['tx'].lower()
    words = nltk.word_tokenize(tx)
    tagged = nltk.pos_tag(words)
    final = self.chunk_tags(tagged)
    nouns = []
    for i in final:
      if i[1] in ["NN", "NNP", "NP", "NNPS"]:
        nouns.append(i[0])
    if len(nouns) > 0:
      yield key, " ".join(nouns)
  
  def chunk_tags(self, tagged_words):
    sent_tree = self.cp.parse(tagged_words)
    chunked = []
    for i in sent_tree:
      if isinstance(i, nltk.tree.Tree):
        chunked.append((" ".join([x[0] for x in i.leaves()]), "NP"))
      else:
        chunked.append(i)
    return chunked

if __name__ == '__main__':
  POSTagger.run()
  """
  pt = POSTagger()
  pt.mapper(1, 'I am the president of United States.')
  """