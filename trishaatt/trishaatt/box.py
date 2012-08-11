#!/usr/bin/python

import urllib, urllib2, mimetools, mimetypes, os, sys, time
from util import XMLNode

'''
@author: anant bhardwaj
@date: Aug 8, 2011

'''

URL = 'http://www.box.net/api/1.0/rest?'
API_KEY = "qzahk2t68aexot06my47sj6oigqu8mas"
RETURN_CODES = {
		'get_ticket'        :   'get_ticket_ok',
		'get_auth_token'    :   'get_auth_token_ok',
		'get_account_tree'  :   'listing_ok',
		'logout'            :   'logout_ok',
		'create_folder'     :   'create_ok',
		'upload'            :   'upload_ok',
		'delete'            :   's_delete_node'
	}
	

class Main():
	def __init__(self, api_key):
		box = Box()
		self.auth_token = box.load_creds()
		print self.auth_token
		resp = box.upload("token_box.txt", self.auth_token);
		resp = box.get_listing(self.auth_token);
		
		
	
        


class Box():
	TOKEN_FILE = "token_box.txt"	

	def load_creds(self):
		try:
			stored_creds = open(self.TOKEN_FILE).read()
			print "[loaded access token]"
			return stored_creds
		except IOError:
			self.store_token()
			self.load_creds()
            

	def write_token(self, token):
		f = open(self.TOKEN_FILE, 'w')
		f.write(token)
		f.close()   
	

	def store_token(self):
		rsp = self.get_ticket ()
		ticket = rsp.ticket[0].elementText
		auth_url = "http://www.box.net/api/1.0/auth/%s" % ticket
		print auth_url
		raw_input()	
		rsp = self.get_auth_token(ticket)
		auth_token = rsp.auth_token[0].elementText
		self.write_token(auth_token)
     
	
	def get_ticket(self):
		arg = {}
		arg["action"] = "get_ticket"
		arg["api_key"] = API_KEY
		request = url_encode_params(params=arg)
		print "--request----------------------------------------"
		print request
		f = urllib.urlopen(URL + request)
		resp = f.read()
		print "--response----------------------------------------"
		print resp
		f.close()
		xml = XMLNode().parseXML(resp, True)
		check_errors("get_ticket", xml)
		return xml
		
	def get_auth_token(self, ticket):
		arg = {}
		arg["action"] = "get_auth_token"
		arg["api_key"] = API_KEY
		arg["ticket"] = ticket
		request = url_encode_params(params=arg)
		print "--request----------------------------------------"
		print request
		f = urllib.urlopen(URL + request)
		resp = f.read()
		print "--response----------------------------------------"
		print resp
		f.close()

		xml = XMLNode().parseXML(resp, True)
		check_errors("get_auth_token", xml)
		return xml
	
	
	def get_listing(self, auth_token):		
		arg = {}
		arg["auth_token"] = auth_token
		arg["api_key"] = API_KEY
		arg["action"] = "get_account_tree"
		arg["folder_id"] = 0		
		
		request = url_encode_params(params=arg)
		print "--request----------------------------------------"
		print request
		f = urllib.urlopen(URL + request)	
		resp = f.read()
		print "--response----------------------------------------"
		print resp
		f.close()
		xml = XMLNode().parseXML(resp)
		check_errors("get_account_tree", xml)
		return xml
	
	def upload(self, filename, auth_token):        
		if filename == None:
			raise UploadException("filename OR jpegData must be specified")

		
		arg = {}
		arg["auth_token"] = auth_token
		arg["folder_id"] = 0
		arg["share"] = 1
		url = 'http://upload.box.net/api/1.0/upload/%s/%s' % (arg['auth_token'], arg['folder_id'])

		boundary = mimetools.choose_boundary()
		body = ""

		body += "--%s\r\n" % (boundary)
		body += 'Content-Disposition: form-data; name="share"\r\n\r\n'
		body += "%s\r\n" % (arg['share'])

		body += "--%s\r\n" % (boundary)
		body += "Content-Disposition: form-data; name=\"file\";"
		body += " filename=\"%s\"\r\n" % filename
		body += "Content-Type: %s\r\n\r\n" % get_content_type(filename)

		fp = file(filename, "rb")
		data = fp.read()
		fp.close()

		postData = body.encode("utf_8") + data + \
			("\r\n--%s--" % (boundary)).encode("utf_8")

		request = urllib2.Request(url)
		request.add_data(postData)
		request.add_header("Content-Type", \
			"multipart/form-data; boundary=%s" % boundary)
		f = urllib2.urlopen(request)
		resp = f.read()
		print resp
		f.close()
		xml = XMLNode().parseXML(resp)
		return xml



def url_encode_params(params={}):
	if not isinstance(params, dict):
		raise Exception("You must pass a dictionary!")
	params_list = []
	for k,v in params.items():
		if isinstance(v, list): params_list.extend([(k+'[]',x) for x in v])
		else:					params_list.append((k, v))
	return urllib.urlencode(params_list)


def check_errors(method, xml):
	status = xml.status[0].elementText
	if status == RETURN_CODES[method]:
		return
	raise Exception("Box.net returned [%s] for action [%s]" % (status, method))

def get_content_type(filename):
	return mimetypes.guess_type(filename)[0] or 'application/octet-stream'



def main():
    Main(API_KEY)

if __name__ == '__main__':
    main()
