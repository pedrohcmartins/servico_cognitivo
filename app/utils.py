# -*- coding: iso-8859-1 -*-

import http.client, urllib.parse, json

def corretorOrtografico(texto):

	text = texto
		
	params = {'mkt': 'pt-BR', 'mode': 'proof', 'text': text}

	key = 'd9cd02759d4d449ebc3f223b3d999314'

	host = 'api.cognitive.microsoft.com'
	path = '/bing/v7.0/spellcheck'

	headers = {'Ocp-Apim-Subscription-Key': key,
	'Content-Type': 'application/x-www-form-urlencoded'}

	conn = http.client.HTTPSConnection(host)
	params = urllib.parse.urlencode (params)
	conn.request ("POST", path, params, headers)
	response = conn.getresponse ()
	
	data = json.loads(response.read())

	for dado in data["flaggedTokens"]:
		token = dado["token"]	
		sug = dado["suggestions"][0]["suggestion"]
		text = text.replace(token, sug)

	return text


def textLanguage(texto):

	uri = 'westcentralus.api.cognitive.microsoft.com'
	path = '/text/analytics/v2.0/languages'

	def GetLanguage (documents):

	    accessKey = '2280ecfc884f4f9e8cd10cb3cd421816'
	    headers = {'Ocp-Apim-Subscription-Key': accessKey}
	    conn = http.client.HTTPSConnection(uri)
	    body = json.dumps  (documents)
	    conn.request ("POST", path, body, headers)
	    response = conn.getresponse ()
	    return response.read ()

	documents = { 'documents': [
	    { 'id': '1', 'text': texto }
	]}

	result = GetLanguage (documents)

	data = json.loads(result)

	language = data["documents"][0]["detectedLanguages"][0]["name"]
	return language


def textSentiment(texto):

	uri = 'westcentralus.api.cognitive.microsoft.com'
	path = '/text/analytics/v2.0/sentiment'

	def GetSentiment (documents):

	    accessKey = '2280ecfc884f4f9e8cd10cb3cd421816'
	    headers = {'Ocp-Apim-Subscription-Key': accessKey}
	    conn = http.client.HTTPSConnection(uri)
	    body = json.dumps  (documents)
	    conn.request ("POST", path, body, headers)
	    response = conn.getresponse ()
	    return response.read ()

	documents = { 'documents': [
	    { 'id': '1', 'text': texto }
	]}

	result = GetSentiment (documents)

	data = json.loads(result)

	score = data["documents"][0]["score"]
	score = score * 100
	if score > 50:
		status = "Positiva"
	else:
		status = "Negativa"
	sentiment = status + " -> {:.2f}".format(score)

	return sentiment


def textKey(texto):

	uri = 'westcentralus.api.cognitive.microsoft.com'
	path = '/text/analytics/v2.0/keyPhrases'

	def GetKeyPhrases (documents):

		accessKey = '2280ecfc884f4f9e8cd10cb3cd421816'
		headers = {'Ocp-Apim-Subscription-Key': accessKey}
		conn = http.client.HTTPSConnection (uri)
		body = json.dumps (documents)
		conn.request ("POST", path, body, headers)
		response = conn.getresponse ()
		return response.read ()

	documents = { 'documents': [
	    { 'id': '1', 'text': texto }
	]}

	result = GetKeyPhrases (documents)

	data = json.loads(result)
	keyPhrases = data["documents"][0]["keyPhrases"]
	keyPhrases = str(keyPhrases).replace('[', '').replace(']', '')
	
	return keyPhrases


def searchText(texto):

	uri = 'westus.api.cognitive.microsoft.com'
	path = '/qnamaker/v2.0/knowledgebases/dcd767e6-601a-4c74-8039-2233a5e2f81e/generateAnswer'

	def GetText (text):

		accessKey = '45b2b7c3be39450b870175aa1c21c13d'
		headers = {'Ocp-Apim-Subscription-Key': accessKey, 'Content-Type': 'application/json'}
		conn = http.client.HTTPSConnection (uri)
		body = json.dumps (text)
		conn.request ("POST", path, body, headers)
		response = conn.getresponse ()

		# print (response.read())
		return response.read ()

	text = { 'question': texto }
	
	result = GetText(text)

	data = json.loads(result)
	result = data["answers"][0]["answer"]

	print (result.encode('utf-8'))
	
	return result