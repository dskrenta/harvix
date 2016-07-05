#!/usr/local/bin/python
###################################
# python version 2.7.3 *required* #
###################################
'''
split into sentences								Done
check for query word clustering						Done
add weight to query									Done
substitute pronouns for nouns						Done
add weight to varios forms of "is" after query		Done
add weight to topic sentences						Done
weight numbers										Done
look for common terms near query					On the cite: on mouse over -> iframe
													quick answer of the moused over word
other common words in text							Done
simplify long terms and acronyms					Unnecessary at the moment, TODO
'''
import re, urllib2
from HTMLParser import HTMLParser

def weight(text,query):
	#all changeable or imprecise values are preceded "vary to fit data"
	########################
	# split into sentences #
	########################
	#TODO: fix accronym problem  resolved
	#find the sentences in the text
	sentences=re.split('([A-Z]([^\.!?]|(?<=[0-9\-])[\.](?=[0-9\-]))+[\.!?])',text)
	modifiedSentences=[]
	sentenceWeight=[]
	#find indices of all instances of returns
	indices=[i/3 for i, x in enumerate(sentences[:-1]) if x.count('\n')>0 or i==0]
	#delete inaccuracies
	del sentences[0]
	for i in range(1,len(sentences)/3+1):
		del sentences[i]
		del sentences[i]
		#save lowercase versions of the sentences
		modifiedSentences.append(sentences[i-1].lower())
		#start all sentences off with 0 weight
		sentenceWeight.append(0)
	#make the text lowercase
	text=text.lower()
	#################################
	# add weight to topic sentences #
	#################################
	#amount of weight added to topic sentences, vary to fit data
	topicSentenceWeight=.4
	for i in indices:
		sentenceWeight[i]+=topicSentenceWeight
	###################################
	# check for query word clustering #
	###################################
	#find individual words in the query
	queryWords=re.split(' ',query)
	queryClusters=[]
	queryClustersReference=[]
	#starting position
	for i in range(len(queryWords)):
		#number of words tested
		for j in range(len(queryWords)-i):
			testQueryCluster=''
			testRange=range(i,i+j+1)
			#combine the words
			for k in testRange:
				testQueryCluster+=queryWords[k]+' '
			testQueryCluster=testQueryCluster.strip()
			#check if there are a segnificant number of occurences in the text.
			#number is imprecise, vary to fit data
			if(text.count(testQueryCluster)>1):
				append=True
				#iterate through the words
				k=0
				while k in range(len(queryClustersReference)):
					overlap=0
					#iterate through what words in the query
					#the currently selected cluster is using
					#to check the number of overlapping occurrences
					for l in range(len(queryClustersReference[k])):
						#check if it is used in the tested cluster
						if(testRange.count(queryClustersReference[k][l])):
							overlap+=1
					#check if one completely contains the other
					if(overlap==len(queryClustersReference[k])):
						#the previously recorded cluster is contained
						#check if there are a relevant number of occurrences
						#independent of the larger test cluster
						#the latter part of this formula has no data supporting it
						#vary to fit data
						if(text.count(testQueryCluster)-text.count(queryClusters[k])<\
							max((6/len(queryClustersReference[k]))-1,1)):
							del queryClusters[k]
							del queryClustersReference[k]
					if(overlap==len(testRange)):
						#the currently tested cluster
						#is a subset of a previously recorded one
						#check if there are a relevant number of occurrences
						#independent of the larger test cluster
						#the latter part of this formula has no data supporting it
						#vary to fit data
						if(text.count(queryClusters[k])-text.count(testQueryCluster)<\
							max((6/len(testRange))-1,1)):
							append=False
					k+=1
				if(append):
					queryClusters.append(testQueryCluster)
					queryClustersReference.append(testRange)
	#######################################
	# look for other common words in text #
	#######################################
	#note that the currently utilized method
	#is more efficient than a count of all the elements, don't change
	#the number of most popular words to add weight to, vary to fit data
	topNumber=4
	#amount of weight added to sentences with common words.
	#amount will be added (topNumber) times for most common,
	#(topNumber-1) for second most common etc. for (topNumber) words
	#vary to fit data
	commonWordWeight=.3
	#most common irrelevant to search
	commonIrrelevancies=['the', 'be', 'to', 'of', 'and', 'a', 'in', 'that', 'have', 'is',\
		'it', 'for', 'not', 'on', 'with', 'he', 'as', 'you', 'do', 'at', 'this', 'but',\
		'his', 'by', 'from', 'they', 'we', 'say', 'her', 'she', 'or', 'an', 'will', 'my',\
		'one', 'all', 'would', 'there', 'their', 'what', 'so', 'up', 'out', 'if',\
		'about', 'who', 'get', 'which', 'go', 'me', 'when', 'make', 'can', 'like',\
		'time', 'no', 'just', 'him', 'know', 'take', 'people', 'into', 'year', 'your',\
		'good', 'some', 'could', 'them', 'see', 'other', 'than', 'then', 'now', 'look',\
		'only', 'come', 'its', 'over', 'think', 'also', 'back', 'after', 'use', 'two',\
		'how', 'our', 'work', 'first', 'well', 'way', 'even', 'new', 'want', 'because',\
		'any', 'these', 'give', 'day', 'most', 'us', 'be', 'have', 'do', 'say', 'get',\
		'make', 'go', 'know', 'take', 'see', 'come', 'think', 'look', 'want', 'give',\
		'use', 'find', 'tell', 'ask', 'work', 'seem', 'feel', 'try', 'leave', 'call',\
		'good', 'new', 'first', 'last', 'long', 'great', 'little', 'own', 'other', 'old',\
		'right', 'big', 'high', 'different', 'small', 'large', 'next', 'early', 'young',\
		'few', 'public', 'bad', 'same', 'able', 'to', 'of', 'in', 'for', 'on', 'with',\
		'at', 'by', 'from', 'up', 'about', 'into', 'over', 'after','beneath', 'under',\
		'above', 'the', 'and', 'a', 'that', 'i', 'it', 'not', 'he','as', 'you', 'this',\
		'but', 'his', 'they', 'her', 'she', 'or', 'an', 'will','my', 'one', 'all',\
		'would', 'there', 'their']
	#find all the words in the text
	wordList=filter(None,re.findall("[a-zA-Z]*",text))
	wordList=filter(lambda a: commonIrrelevancies.count(a)==0,wordList)
	wordCounter={}
	#iterate through the words
	for word in wordList:
		#if the tested word has already been recorded
		if word in wordCounter:
			#add one to its count
			wordCounter[word]+=1
		else:
			#otherwise set its count to one
			wordCounter[word]=1
	
	commonWords=sorted(wordCounter, key=wordCounter.get,reverse=True)[:topNumber]
	#######################
	# add weight to query #
	#######################
	#constants, vary to fit data
	pronouns=["she", "her", "he", "him", "it", "they", "them", "that", "this", "these",
		"that", "those", "himself", "herself", "itself", "themselves", "his", "her",
		"hers", "its", "their", "theirs"]
	isForms=["is", "are", "was", "were", "been", "being"]
	queryClusterWeight=1
	queryIsWeight=1
	#other, don't change
	queryOccuredPreviously=[]
	#iterate through the sentences
	for i in range(len(modifiedSentences)):
		queryOccuredCurrently=[]
		#################################
		# substitute pronouns for nouns #
		#################################
		if(queryOccuredPreviously!=[]):
			for j in range(len(pronouns)):
				#if(modifiedSentences[i].count(pronouns[j])>0):
				if(len(re.findall((" %(pronoun)s[. ]" %{"pronoun":pronouns[j]}),\
					modifiedSentences[i]))):
					queryOccuredCurrently.append(queryOccuredPreviously[-1])
		#iterate through the word clusters in the query
		for j in range(len(queryClusters)):
			#check if that cluster is contained in the sentence
			if(modifiedSentences[i].count(queryClusters[j])>0):
				#if it is then add weight to the sentence
				#posible to change to equation involving number of words
				#and number of occurrences, vary to fit data
				queryOccuredCurrently.append(queryClusters[j])
		if(queryOccuredCurrently!=[]):
			sentenceWeight[i]+=queryClusterWeight*len(queryOccuredCurrently)
			##################################################
			# add weight to varios forms of "is" after query #
			##################################################
			wordAfter=[]
			for j in range(len(queryOccuredCurrently)):
				#find the word after the query
				wordAfter+=re.findall(("(?<=%(query)s )[a-zA-z]*" \
					%{"query":queryOccuredCurrently[j]}),modifiedSentences[i])
			#iterate through the word after the instances of the query
			for k in range(len(wordAfter)):
				#if any of them are a form of if
				if(isForms.count(wordAfter[k])>0):
					#add weight to the sentence
					sentenceWeight[i]+=queryIsWeight
		queryOccuredPreviously=queryOccuredCurrently
		for j in range(min(topNumber,len(commonWords))):
			if(modifiedSentences[i].count(commonWords[j])>0):
				sentenceWeight[i]+=commonWordWeight*(topNumber-i)
		#########################
		# add weight to numbers #
		#########################
		#amount of weight added to sentences with numbers, vary to fit data
		numberWeight=.3
		#count the number of numbers there are in the text
		#check if it is greater than 0
		if(len(re.findall("(?<= )([-+]?\d*\.\d+|\d+|[-+]?\d+)",modifiedSentences[i]))>0):
			#add specified weight to query, only adds once no matter the number of occurences
			sentenceWeight[i]+=numberWeight
	##############################
	# return important sentences #
	##############################
	#percentage of the highest value that is concidered important, vary to fit data
	percent=.5
	if sentenceWeight:
		minWeight=max(sentenceWeight)*percent
		returnSentences=[]
		for i in [j for j, x in enumerate(sentenceWeight) if x>=minWeight]:
			returnSentences.append(sentences[i])
		return returnSentences
	else:
		return []

def getgoogleurl(search,siteurl=False):
	if siteurl==False:
		return 'http://www.google.com/search?q='+urllib2.quote(search)+'&oq='+urllib2.quote(search)
	else:
		return 'http://www.google.com/search?q=site:'+urllib2.quote(siteurl)+'%20'+\
			urllib2.quote(search)+'&oq=site:'+urllib2.quote(siteurl)+'%20'+urllib2.quote(search)

def getgooglelinks(search,siteurl=False):
	#google returns 403 without user agent
	headers = {'User-agent':'Mozilla/11.0'}
	req = urllib2.Request(getgoogleurl(search,siteurl),None,headers)
	site = urllib2.urlopen(req)
	data = site.read()
	site.close()
	#no beatifulsoup because google html is generated with javascript
	start = data.find('<div id="res">')
	end = data.find('<div id="foot">')
	if data[start:end]=='':
		#error, no links to find
		return False
	else:
		links =[]
		data = data[start:end]
		start = 0
		end = 0        
		while start>-1 and end>-1:
			#get only results of the provided site
			if siteurl==False:
				start = data.find('<a href="/url?q=')
			else:
				start = data.find('<a href="/url?q='+str(siteurl))
			data = data[start+len('<a href="/url?q='):]
			end = data.find('&amp;sa=U&amp;ei=')
			if start>-1 and end>-1: 
				link =  urllib2.unquote(data[0:end])
				data = data[end:len(data)]
				if link.find('http')==0:
					links.append(link)
		return links

def grabpage(url):
	try:
		pageFp = urllib2.urlopen(url)
	except urllib2.HTTPError, e:
		#wikipedia error
		#YAY CHROME!
		req = urllib2.Request(url, headers={'User-Agent' : "Chrome"}) 
		pageFp = urllib2.urlopen( req )
	pageData = pageFp.read()
	return pageData

'''
remove unlikely candidates (negative and no maybe)							Done			
if there is a positive use that as a base									TODO
look for data mostly														Done
delete divs with mostly a href												Done
divs with only one link might be ok											Done
delete anything questionable with the first thing a link					Done
delete any divs with headers including ad, ads, related as words or alone	Done
delete divs with less than 50 characters									Done
delete paragraphs without periods											Done
'''

class mainarticleparser(HTMLParser):
	def __init__(self):
		#called when the class is initiated
		HTMLParser.__init__(self)
		self.reset_variables()
	
	def reset_variables(self):
		#the array containing the dom
		self.dom=[[0,0]]
		#the current position in walking the dom
		self.domPos=[0]
		#a reference to the positon in the dom
		self.domBranch=self.dom[0]
		#regular expression denoting a probable candidate
		self.positive=re.compile(\
			".*(article|body|content|entry|hentry|main|page|pagination|post|text|blog|story).*")
		#regular expression denoting a possible candidate
		self.maybe=re.compile(".*(and|article|body|column|main|shadow).*")
		#regular expression denoting a improbable candidate
		self.negative=\
			re.compile(".*(combx|comment|com-|contact|foot|footer|footnote|masthead|meta|outbrain|\
			promo|related|scroll|shoutbox|sidebar|sponsor|shopping|tags|tool|widget|references).*")
		self.nonData=re.compile("(\t|\n)+")
		#note: temp variable, not ment for storing, reset before using check for data.
		self.branchData=[]
		self.dataParent=[]
	
	def handle_starttag(self, tag, attrs):
		#print tag, attrs
		#run when the start of a tag is found, the type is in tag, the attributes in attrs
		#update the dom position
		self.domPos.append(len(self.domBranch))
		#add the tag to the dom
		self.domBranch.append([tag,attrs])
		#update the reference
		self.update_branch()
	
	def handle_endtag(self, tag):
		#print tag
		#run when the end of a tag is found, the type is in tag
		#is the tag irrelevant?
		toDelete=False
		#it definitely is with script style and head because those aren't even shown
		#TODO: check if there are any other tags
		#"table" is experimental delete if needed
		if self.domBranch[0] == "script" or self.domBranch[0] == "style" or \
			self.domBranch[0] == "head" or self.domBranch[0] == "table":
			#mark as irrelevant
			toDelete=True
			#test code
			#print "#1"
		#iterate through the attributes of the tag
		for attr in self.domBranch[1]:
			#if the value of any of them is irredeemably immaterial
			if attr[1] and self.negative.match(attr[1]) and not self.maybe.match(attr[1]):
				#mark it as such
				toDelete=True
				#test code
				#print "#2"
		#what divs should be passed down
		toTransfer=[]
		#if the tag is a div
		#TODO: spans etc.
		if self.domBranch[0] == "div":
			#the amount of potential content the div would contribute to the article
			contentAdded=0
			#look through the current layer for text
			for i in range(2,len(self.domBranch)):
				#if there is content
				if type(self.domBranch[i]) == str:
					#add it to the amount of text added by the current layer
					contentAdded = len(self.domBranch[i])
			#reset the branch data
			self.branchData=[]
			#reset the data parents
			self.dataParent=[]
			#the length of all of the data in the div
			textLength=0
			#all the text in the div
			fullText=""
			#look for the data in the current branch
			self.check_for_data(self.domBranch)
			#the number of links in the text
			linkCount=len(self.branchData)
			#iterate through the branch
			for i in range(linkCount):
				#add the data to the compilation of all the text in the div
				fullText+=self.branchData[i]
				#if it isn't a link
				if(self.dataParent[i]!='a'):
					#add the length of the text to the count
					textLength+=len(self.branchData[i])
					#subtract it from the link count
					linkCount-=1
				if(self.dataParent[i]!='div'):
					contentAdded+=len(self.branchData[i])
			#if there is less than 50 characters of added content, vary to fit data
			if contentAdded < 50:
				#delete the div
				toDelete=True
				#test code
				#print "#3"
				#but pass down surviving divs
				#look through the current layer
				for i in range(2,len(self.domBranch)):
					#if the currently tested element is a div
					if type(self.domBranch[i]) == list and self.domBranch[i][0]=="div":
						#transfer down
						toTransfer.append(self.domBranch[i])
			#maximum percentage of content that are links, vary to fit data
			maxLinkPercent=.7
			#minium number of characters that are not links 
			miniumNonLinkContent=50
			#if there is no data in the branch
			if len(self.branchData)==0:
				#delete the element
				toDelete=True
				#test code
				#print "#4"
			#otherwise
			else:
				#if the first data is a link or there is more than the max percent of links
				#unless the only content of the div is the link (in which case it's just bad format)
				#or the length of the text is less than the minium and there is more than just a div
				#or there are no periods
				#or there's something unrelated at the top of the div
				#sorry about the lack of readability
				if ((self.dataParent[0]=='a' or float(linkCount)/float(len(self.branchData))\
					>maxLinkPercent) and not len(self.branchData)==1) or \
					(textLength<miniumNonLinkContent and self.dataParent[0]!='a' and \
					len(self.branchData)!=1) or fullText.count(".")==0 or \
					re.match(".*(^| )(ad|advertisement|related)[s]?($| ).*",self.branchData[0]):
					#delete it
					toDelete=True
					#test code
					#print "#5"
		#go down a level
		self.domPos=self.domPos[:-1]
		#update the branch
		self.update_branch()
		#if the appended tag is to be deleted
		if toDelete:
			#delete it
			#test code
			#print self.domBranch[-1]
			del self.domBranch[-1]
			#append the elements to be transfered
			self.domBranch+=toTransfer
	
	def handle_data(self, data):
		#run when innerHTML content is found (text not in a tag)
		#log the data
		self.domBranch.append(data)
		#print it (for test purposes)
		#print data
	
	def handle_comment(self, data):
		#run when there is a comment in the HTML
		#doesn't really matter to the current method
		#potentially contains "main article" or something similar
		#TODO: check for common words suggesting the main body
		''''''
	
	def update_branch(self):
		#update the branch
		self.domBranch=eval("self.dom[%s]" %']['.join([str(i) for i in self.domPos]))
	
	def check_for_data(self, domTree):
		#recursive function
		#TODO: crashs with a dom depth of >1000
		#never will actually happen but it's still a good thing to fix...
		#iterate through
		for i in range(2,len(domTree)):
			#if there is a child element
			if type(domTree[i]) == list:
				#look for data in there
				self.check_for_data(domTree[i])
			#if it is a string
			elif type(domTree[i]) == str:
				if self.nonData.match(domTree[i]):
					continue
				#log it
				self.branchData.append(domTree[i])
				#log the parent element
				self.dataParent.append(domTree[0])
		#return it
		return self.branchData
	
	def get_data(self):
		#run after feed
		#reset variables
		self.branchData=[]
		self.dataParent=[]
		#test code
		#print self.dom
		#check for data
		return self.check_for_data(self.dom[0])

#renaming function call parser.feed(html) then call parser.get_data() for the content
parser = mainarticleparser()

def parsepage(url):
	#parse a url
	#reset the parser
	parser.reset_variables()
	#feed it the data
	parser.feed(grabpage(url))
	#return the response
	return parser.get_data()

def getresults(query):
	#get the results
	#start off with google links
	#sorry google...
	results=getgooglelinks(query)
	#the summaries of the results
	summaries=[]
	#for every result
	for i in results:
		print i
		#append the string version of the array of the summaries to the array of summaries
		#it's in a string array so it can be fed into javascript
		summaries.append("[\""+("\",\"".join(weight(" ".join(parsepage(i)),query)))+"\"]")
	#set up the results and the summaries to be fed into javascript
	return "summeries=["+(",".join(summaries))+"];results=[\""+("\",\"".join(results))+"\"]"

if __name__ == "__main__":
	#this is run when the program is run
	#run whatever code here
	#test code
	#print " ".join(parsepage("http://en.wikipedia.org/wiki/Absolute_zero"))
	import sys
	#Raise exceptions
	#Wrong version
	version=sys.version
	version=re.split("\.", re.split(" ", version)[0])
	if version[0]!="2" or int(version[1])<7 or int(version[2])<3:
		raise Exception("Incorrect version")
	'''
	test case:
	http://chemistry.about.com/od/chemistryfaqs/f/absolutezero.htm
	
	returns this error with Python < 2.7.3
	  File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/HTMLParser.py",
	  	line 108, in feed
	  File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/HTMLParser.py",
	  	line 148, in goahead
	  File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/HTMLParser.py",
	  	line 229, in parse_starttag
	  File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/HTMLParser.py",
	  	line 304, in check_for_whole_start_tag
	  File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/HTMLParser.py",
	  	line 115, in error
	HTMLParser.HTMLParseError: malformed start tag, at line 38, column 150
	
	problem is with tags generated by JavaScript,
	mistaken as HTML and crashes if something is inserted
	'''
	#No arguments
	if len(sys.argv)==1:
		raise Exception("No arguments imputed")
	#run the program
	print getresults(sys.argv[1])
