import nltk
from nltk.stem.lancaster import LancasterStemmer

stemmer = LancasterStemmer()

import numpy as np
import tflearn
import tensorflow as tf
import random
import json
import pickle


with open("intents.json") as file:
	data = json.load(file)

print(data["intents"])


words = []
labels = []
docs_x = []
docs_y = []

#Stemming(Brings any word to it's root/origin word)
for intent in data["intents"]:
	for pattern in intent["patterns"]:
		wrd = nltk.word_tokenize(pattern)
		words.extend(wrd) #Extending the empty list, therby adding the tokenized words
		docs_x.append(wrd)
		docs_y.append(intent["tag"])

	if intent["tag"] not in labels:
		labels.append(intent["tag"])

	#Remove duplicates from words list to find vocabulary size of model

words = [stemmer.stem(w.lower()) for w in words if w != "?"]
words = sorted(list(set(words))) #Removing duplicates and sending them back into the list and sorts them

labels = sorted(labels) #Sorting the labels

training = []
output = []

out_empty = [0 for _ in range(len(labels))] #To create one-hot encoded vectors

for x,doc in enumerate(docs_x):

	bag = []   #Bag of words to contain the one-hot encoded words

	wrd = [stemmer.stem(w) for w in doc]

#One hot encoding
	for w in words:
		if w in wrd:
			bag.append(1)
		else:
			bag.append(0)

	output_row = out_empty[:]
	output_row[labels.index(docs_y[x])] = 1

	training.append(bag)
	output.append(output_row)

training = np.array(training)
output = np.array(output)


tf.reset_default_graph()

net = tflearn.input_data(shape=[None, len(training[0])]) #Finds input shape we're expecting for our model

net = tflearn.fully_connected(net,8) #Connecting this fully connected layer to our input data

net = tflearn.fully_connected(net,8) #Another hidden layer

net = tflearn.fully_connected(net,len(output[0]), activation="softmax") #Allows us to get probabilities for each neuron in output layer

net = tflearn.regression(net)

model = tflearn.DNN(net) #Deep Neural Network



model.fit(training, output, n_epoch=1000, batch_size=8, show_metric=True)

model.save("chatbot_modelll")
