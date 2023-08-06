# Copyright 2015 by Toben "Narcolapser" Archer. All Rights Reserved.
#
# Permission to use, copy, modify, and distribute this software and its documentation for any purpose 
# and without fee is hereby granted, provided that the above copyright notice appear in all copies and 
# that both that copyright notice and this permission notice appear in supporting documentation, and 
# that the name of Toben Archer not be used in advertising or publicity pertaining to distribution of 
# the software without specific, written prior permission. TOBEN ARCHER DISCLAIMS ALL WARRANTIES WITH 
# REGARD TO THIS SOFTWARE, INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS. IN NO EVENT 
# SHALL TOBEN ARCHER BE LIABLE FOR ANY SPECIAL, INDIRECT OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES 
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE 
# OR OTHER TORTIOUS ACTION, ARISING OUT
# OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

from O365 import Attachment
from O365 import Contact
import logging
import json
import requests

logging.basicConfig(filename='o365.log',level=logging.DEBUG)

log = logging.getLogger(__name__)

class Message( object ):
	'''
	Management of the process of sending, recieving, reading, and editing emails.
	
	Note: the get and set methods are technically superflous. You can get more through control over
	a message you are trying to craft throught he use of editing the message.json, but these
	methods provide an easy way if you don't need all the power and would like the ease.
	
	Methods:
		constructor -- creates a new message class, using json for existing, nothing for new.
		fetchAttachments -- kicks off the process that downloads attachments.
		sendMessage -- take local variables and form them to send the message.
		markAsRead -- marks the analougs message in the cloud as read.
		getSender -- gets a dictionary with the sender's information.
		getSenderEmail -- gets the email address of the sender.
		getSenderName -- gets the name of the sender, if possible.
		getSubject -- gets the email's subject line.
		getBody -- gets contents of the body of the email.
		addRecipient -- adds a person to the recipient list.
		setRecipients -- sets the list of recipients.
		setSubject -- sets the subject line.
		setBody -- sets the body.

	Variables: 
		att_url -- url for requestiong attachments. takes message GUID
		send_url -- url for sending an email
		update_url -- url for updating an email already existing in the cloud.
	
	'''
	
	att_url = 'https://outlook.office365.com/api/v1.0/me/messages/{0}/attachments'
	send_url = 'https://outlook.office365.com/api/v1.0/me/sendmail'
	draft_url = 'https://outlook.office365.com/api/v1.0/me/folders/{folder_id}/messages'
	update_url = 'https://outlook.office365.com/api/v1.0/me/messages/{0}'

	def __init__(self, json=None, auth=None):
		'''
		Makes a new message wrapper for sending and recieving messages.
		
		Keyword Arguments:
			json (default = None) -- Takes json if you have a pre-existing message to create from.
			this is mostly used inside the library for when new messages are downloaded.
			auth (default = None) -- Takes an (email,password) tuple that will be used for
			authentication with office365.
		'''
		if json:
			self.json = json
			self.hasAttachments = json['HasAttachments']

		else:
			self.json = {'Message':{'Body':{}},'ToRecipients':{}}
			self.hasAttachments = False
	
		self.auth = auth
		self.attachments = []
		self.reciever = None


	def fetchAttachments(self):
		'''kicks off the process that downloads attachments locally.'''
		if not self.hasAttachments:
			log.debug('message has no attachments, skipping out early.')
			return False

		response = requests.get(self.att_url.format(self.json['Id']),auth=self.auth)
		log.info('response from O365 for retriving message attachments: %s',str(response))
		json = response.json()

		for att in json['value']:
			try:
				self.attachments.append(Attachment(att))
				log.debug('successfully downloaded attachment for: %s.',self.auth[0])
			except Exception as e:
				log.info('failed to download attachment for: %s', self.auth[0])

		return len(self.attachments)

	def sendMessage(self):
		'''takes local variabls and forms them into a message to be sent.'''

		headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

		try:
			data = {'Message':{'Body':{}}}
			data['Message']['Subject'] = self.json['Subject']
			data['Message']['Body']['Content'] = self.json['Body']['Content']
			data['Message']['Body']['ContentType'] = self.json['Body']['ContentType']
			data['Message']['ToRecipients'] = self.json['ToRecipients']
			data['Message']['Attachments'] = [att.json for att in self.attachments]
			data['SaveToSentItems'] = "false"
			data = json.dumps(data)
			log.debug(str(data))
		except Exception as e:
			log.error(str(e))
			return False

		response = requests.post(self.send_url,data,headers=headers,auth=self.auth)
		log.debug('response from server for sending message:'+str(response))

		if response.status_code != 202:
			return False

		return True

		

		
	def markAsRead(self):
		'''marks analogous message as read in the cloud.'''
		read = '{"IsRead":true}'
		headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
		try:
			response = requests.patch(self.update_url.format(self.json['Id']),read,headers=headers,auth=self.auth)
		except:
			return False
		return True


	def getSender(self):
		'''get all available information for the sender of the email.'''
		return self.json['Sender']

	def getSenderEmail(self):
		'''get the email address of the sender.'''
		return self.json['Sender']['EmailAddress']['Address']
	
	def getSenderName(self):
		'''try to get the name of the sender.'''
		try:
			return self.json['Sender']['EmailAddress']['Name']
		except:
			return ''

	def getSubject(self):
		'''get email subject line.'''
		return self.json['Subject']

	def getBody(self):
		'''get email body.'''
		return self.json['Body']['Content']

	def setRecipients(self,val):
		'''
		set the recipient list.
		
		val: the one argument this method takes can be very flexible. you can send:
			a dictionary: this must to be a dictionary formated as such:
				{"EmailAddress":{"Address":"recipient@example.com"}}
				with other options such ass "Name" with address. but at minimum it must have this.
			a list: this must to be a list of libraries formatted the way specified above,
				or it can be a list of libraries objects of type Contact. The method will sort
				out the libraries from the contacts. 
			a string: this is if you just want to throw an email address. 
			a contact: type Contact from this library. 
		For each of these argument types the appropriate action will be taken to fit them to the 
		needs of the library.
		'''
		if isinstance(val,list):
			self.json['ToRecipients'] = val
		elif isinstance(val,dict):
			self.json['ToRecipients'] = [val]
		elif isinstance(val,str):
			if '@' in val:
				self.json['ToRecipients'] = []
				self.addRecipient(val)
		elif isinstance(val,Contact):
			self.json['ToRecipients'] = []
			self.addRecipient(val)
		else:
			return False
		return True

	def addRecipient(self,address,name=None):
		'''
		Adds a recipient to the recipients list.
		
		Arguments:
		address -- the email address of the person you are sending to. <<< Important that.
			Address can also be of type contact. if it is name is superflous. Else, it
			uses the name passed if you sent it one.
		name -- the name of the person you are sending to. mostly just a decorator.
		'''
		if isinstance(address,Contact):
			self.json['ToRecipients'].append(address.getFirstEmailAddress())
		else:
			if name is None:
				name = address[:address.index('@')]
			self.json['ToRecipients'].append({'EmailAddress':{'Address':address,'Name':name}})

	def setSubject(self,val):
		'''Sets the subect line of the email.'''
		self.json['Subject'] = val

	def setBody(self,val):
		'''Sets the body content of the email.'''
		cont = False

		while not cont:
			try:
				self.json['Body']['Content'] = val
				self.json['Body']['ContentType'] = 'Text'
				cont = True
			except:
				self.json['Body'] = {}


#To the King!
