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
class Chat(object): 
	def __init__(self, pairs, reflections={}):
		self._pairs = [(re.compile(x, re.IGNORECASE),y) for (x,y) in pairs] 
 		self._reflections = reflections

 	def _substitute(self, str):
 		words = "" 
		for word in string.split(string.lower(str)): 
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

	def respond(self, str):
		def NN(str):
		    temp=[]
		    N=['NN', 'NNP']
		    def ie_preprocess(document):
		        sentences = nltk.sent_tokenize(document) 
		        sentences = [nltk.word_tokenize(sent) for sent in sentences] 
		        sentences = [temp.append(nltk.pos_tag(sent)) for sent in sentences] 
		    ie_preprocess(str)
		    for i in range(len(temp[0])):
		        if (temp[0][i][1]) in N:
		            if (temp[0][i][0]) not in noun:
		                if (temp[0][i][1]) not in noun:
		                    noun.append((temp[0][i][0], str))
		    return noun

		def prp(str):
			temp=[]
			prp= ["PRP","PRP$"]
			sentences = nltk.sent_tokenize(str) 
			sentences = [nltk.word_tokenize(sent) for sent in sentences] 
			[temp.append(nltk.pos_tag(sent)) for sent in sentences]
			for i in range(len(temp[0])):
			    if temp[0][i][1] in prp:
			        pr = "Are you talking about " + (noun[random.randint(1,len(noun))][0])
			    else:
			    	pr="NA"
			return pr


		def mo(str):
			print str
			m=["mother","ma", "mom", "madre", "mamma", "maama", "mama"]
			temp=[]
			sentences = nltk.sent_tokenize(str) 
			sentences = [nltk.word_tokenize(sent) for sent in sentences] 
			[temp.append(nltk.pos_tag(sent)) for sent in sentences]
			for i in range(len(temp[0])):
			    if temp[0][i][0] in m:
			    	return True
		
		def fa(str):
			f=["father","dad", "papa", "pop", "pappa", "daddy"]
			temp=[]
			sentences = nltk.sent_tokenize(str) 
			sentences = [nltk.word_tokenize(sent) for sent in sentences] 
			[temp.append(nltk.pos_tag(sent)) for sent in sentences]
			for i in range(len(temp[0])):
			    if temp[0][i][0] in f:
			    	return True

		def fr(str):
			print str
			f=["friend","bro","bff","amigo","dude","bestie", "best friend"]
			temp=[]
			sentences = nltk.sent_tokenize(str) 
			sentences = [nltk.word_tokenize(sent) for sent in sentences] 
			[temp.append(nltk.pos_tag(sent)) for sent in sentences]
			for i in range(len(temp[0])):
			    if temp[0][i][0] in f:
			    	return True

		ip_temp=[]
		for i in range(len(ip)):
		    ip_temp.append(ip[i][0])
		if str == ip_temp[-1]:
			return "Please do not repeat yourself."

		if fa(str):
			for (pattern, response) in self._pairs: 
	 			match = pattern.match("father") 
				if match: 
					resp = random.choice(response)    # pick a random response 
	 				resp = self._wildcards(resp, match) # process wildcards 
					if resp[-2:] == '?.': resp = resp[:-2] + '.' 
					if resp[-2:] == '??': resp = resp[:-2] + '?'
					ip.append((str, resp)) 	
					return resp, ip, NN(str), prp(str)

		if mo(str):
			for (pattern, response) in self._pairs: 
	 			match = pattern.match("mother") 
				if match: 
					resp = random.choice(response)    # pick a random response 
	 				resp = self._wildcards(resp, match) # process wildcards 
					if resp[-2:] == '?.': resp = resp[:-2] + '.' 
					if resp[-2:] == '??': resp = resp[:-2] + '?'
					ip.append((str, resp)) 	
					return resp, ip, NN(str), prp(str)

		if fr(str):
			for (pattern, response) in self._pairs: 
	 			match = pattern.match("friend") 
				if match: 
					resp = random.choice(response)    # pick a random response 
	 				resp = self._wildcards(resp, match) # process wildcards 
					if resp[-2:] == '?.': resp = resp[:-2] + '.' 
					if resp[-2:] == '??': resp = resp[:-2] + '?'
					ip.append((str, resp)) 	
					return resp, ip, NN(str), prp(str)

		else:
			for (pattern, response) in self._pairs: 
	 			match = pattern.match(str) 
				if match: 
					resp = random.choice(response)    # pick a random response 
	 				resp = self._wildcards(resp, match) # process wildcards 
					
					if resp[-2:] == '?.': resp = resp[:-2] + '.' 
					if resp[-2:] == '??': resp = resp[:-2] + '?'
					ip.append((str, resp)) 	
					return resp, ip, NN(str), prp(str)



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
