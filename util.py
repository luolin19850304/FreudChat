import string 
import re 
import random 
import nltk

reflections = {
  "i am"       : "you are",
  "i was"      : "you were",
  "i"          : "you",
  "i'm"        : "you are",
  "i'd"        : "you would",
  "i've"       : "you have",
  "i'll"       : "you will",
  "my"         : "your",
  "you are"    : "I am",
  "you were"   : "I was",
  "you've"     : "I have",
  "you'll"     : "I will",
  "your"       : "my",
  "yours"      : "mine",
  "you"        : "me",
  "me"         : "you"
}
ip=["NA",]
noun=[]
inp=[]
class Chat(object): 
	def __init__(self, pairs, reflections={}):
		self._pairs = [(re.compile(x, re.IGNORECASE),y) for (x,y) in pairs] 
 		self._reflections = reflections

 	def _substitute(self, x):
 		words = "" 
		for word in string.split(string.lower(x)): 
			if self._reflections.has_key(word): 
				word = self._reflections[word] 
			words += ' ' + word 
		return words 

	def _wildcards(self, response, match): 
 		pos = string.find(response,'%') 
 		while pos >= 0: 
			num = string.atoi(response[pos+1:pos+2]) 
 			response = response[:pos] + self._substitute(match.group(num)) + response[pos+2:] 
			pos = string.find(response,'%') 
		return response 

	def respond(self, x):
		def NN(x):
		    temp=[]
		    N=['NN', 'NNP']
		    def ie_preprocess(document):
		        sentences = nltk.sent_tokenize(document) 
		        sentences = [nltk.word_tokenize(sent) for sent in sentences] 
		        sentences = [temp.append(nltk.pos_tag(sent)) for sent in sentences] 
		    ie_preprocess(x)
		    for i in range(len(temp[0])):
		        if (temp[0][i][1]) in N:
		            if (temp[0][i][0]) not in noun:
		                if (temp[0][i][1]) not in noun:
		                    noun.append((temp[0][i][0], x))
		    return noun

		def prp(x):
			temp=[]
			pr= ["he","she","his","her","himself","herself","it","itself","they","them","themselves"]
			sentences = nltk.sent_tokenize(x) 
			sentences = [nltk.word_tokenize(sent) for sent in sentences] 
			[temp.append(nltk.pos_tag(sent)) for sent in sentences]
			for i in range(len(temp)):
			    # print len(temp)
			    if temp[0][i][0] in pr:
			    	if len(noun)>0:
			    		# print "Are you talking about " + str((noun[-1][0]))
			    		pr = "Are you talking about " + str((noun[-1][0]))
			    		print pr
			    	else:
			    		# print "Whom you are talking about"
			    		pr = "Whom you are talking about"
			    		print pr
					return True
			    else:
			    	return None
			# return pr


		def mo(x):
			m=["mother","ma", "mom", "madre", "mamma", "maama", "mama"]
			temp=[]
			sentences = nltk.sent_tokenize(x) 
			sentences = [nltk.word_tokenize(sent) for sent in sentences] 
			[temp.append(nltk.pos_tag(sent)) for sent in sentences]
			for i in range(len(temp[0])):
			    if temp[0][i][0] in m:
			    	return True
		
		def fa(x):
			f=["father","dad", "papa", "pop", "pappa", "daddy"]
			temp=[]
			sentences = nltk.sent_tokenize(x) 
			sentences = [nltk.word_tokenize(sent) for sent in sentences] 
			[temp.append(nltk.pos_tag(sent)) for sent in sentences]
			for i in range(len(temp[0])):
			    if temp[0][i][0] in f:
			    	return True

		def fr(x):
			f=["friend","bro","bff","amigo","dude","bestie", "best friend"]
			temp=[]
			sentences = nltk.sent_tokenize(x) 
			sentences = [nltk.word_tokenize(sent) for sent in sentences] 
			[temp.append(nltk.pos_tag(sent)) for sent in sentences]
			for i in range(len(temp[0])):
			    if temp[0][i][0] in f:
			    	return True

		ip_temp=[]
		for i in range(len(ip)):
		    ip_temp.append(ip[i][0])
		if x == ip_temp[-1]:
			return "Please do not repeat yourself."

		if fa(x):
			for (pattern, response) in self._pairs: 
	 			match = pattern.match("father") 
				if match: 
					resp = random.choice(response)    # pick a random response 
	 				resp = self._wildcards(resp, match) # process wildcards 
					if resp[-2:] == '?.': resp = resp[:-2] + '.' 
					if resp[-2:] == '??': resp = resp[:-2] + '?'
					ip.append((x, resp)) 	
					return resp

		if mo(x):
			for (pattern, response) in self._pairs: 
	 			match = pattern.match("mother") 
				if match: 
					resp = random.choice(response)    # pick a random response 
	 				resp = self._wildcards(resp, match) # process wildcards 
					if resp[-2:] == '?.': resp = resp[:-2] + '.' 
					if resp[-2:] == '??': resp = resp[:-2] + '?'
					ip.append((x, resp)) 	
					return resp

		if fr(x):
			for (pattern, response) in self._pairs: 
	 			match = pattern.match("friend") 
				if match: 
					resp = random.choice(response)    # pick a random response 
	 				resp = self._wildcards(resp, match) # process wildcards 
					if resp[-2:] == '?.': resp = resp[:-2] + '.' 
					if resp[-2:] == '??': resp = resp[:-2] + '?'
					ip.append((x, resp)) 	
					return resp

		if prp(x)== True:
			prp(x)



		else:
			for (pattern, response) in self._pairs: 
	 			match = pattern.match(x) 
				if match:
					if x in inp:
						for i in range(len(ip)):
							if x==ip[i][0]:
								# print "yes"
								tmp=[]
								temp=str(response).split(",")
								for j in range(len(temp)):
									if temp[j][2:-1]!=ip[i][1]:
										tmp.append(temp[j])
								resp=random.choice(tmp)

					else:
						resp = random.choice(response)
					# print resp    # pick a random response 
	 				resp = self._wildcards(resp, match) # process wildcards 
					
					# if resp[-2:] == '?.': resp = resp[:-2] + '.' 
					# if resp[-2:] == '??': resp = resp[:-2] + '?'
					ip.append((x, resp))
					NN(x)
					if x not in inp:
						inp.append(x)
						
					return resp



	def converse(self, quit="quit"): 
		input = "" 
		while input != quit: 
			input = quit 
			try: input = raw_input(">") 
			except EOFError: 
				print input 
			if input: 
				while input[-1] in "!.": input = input[:-1]
				# if self.respond(input) != None:
				print self.respond(input) 
