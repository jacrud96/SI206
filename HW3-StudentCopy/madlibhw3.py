# Using text2 from the nltk book corpa, create your own version of the
# MadLib program.  

# Requirements:
# 1) Only use the first 150 tokens
# 2) Pick 5 parts of speech to prompt for, including nouns
# 3) Replace nouns 15% of the time, everything else 10%

# Deliverables:
# 1) Print the orginal text (150 tokens)
# 1) Print the new text



# code developed by Jackie Cohen; revised by Paul Resnick
# further revised by Colleen van Lent for Python3
import nltk 
# requires some downloading/installing dependencies to use all its features; numpy is especially tricky to install
import random

from nltk import word_tokenize,sent_tokenize
from nltk.text import Text
from nltk.corpus import gutenberg

debug = False 

if debug:
	print ("Getting information from file austen-sense.txt...\n")


text2 = "austen-sense.txt" # need a file with this name in directory
f = open(text2,'r')
para = f.read()

tokens = nltk.word_tokenize(para)

tagged_tokens = nltk.pos_tag(tokens) # gives us a tagged list of tuples


tagmap = {"NN":"a noun","NNS":"a plural noun","VB":"a verb","JJ":"an adjective", "PRP": "a preposition"}
substitution_probabilities = {"NN":.15,"NNS":.10,"VB":.10,"JJ":.10, "PRP":.10}

def spaced(word):
	if word in [",", ".", "?", "!", ":"]:
		return word
	else:
		return " " + word

sent = ''
for word in para.split()[:150]:
	x = spaced(word)
	sent = sent + x
print (sent)

final_words = []
count = 0 

for (word, tag) in tagged_tokens: 
	if tag not in substitution_probabilities or random.random() > substitution_probabilities[tag]:
		final_words.append(spaced(word))
	else:
		new_word = input("Please enter %s:\n" % (tagmap[tag]))
		final_words.append(spaced(new_word))
		count +=1
		if count == 10:
			break
		else:
			continue 

sent2 = ''
final_text = ''.join(final_words)
for words in final_text.split()[:150]:
	word = spaced(words)
	sent2 = sent2 + word 
print (sent2)
