import requests
import json
import time
import random


class ApiHandler:
	"""
	A class that manages the IUB api
	username: The IUB username
	apiSite: The IUB api endpoint
	tokenPath: The path to an empty file that contains the IUB API token
	loggingHandler: The logging handler where any error is sent
	"""
	def __init__(self, username, apiSite, tokenPath, loggingHandler):
		self.username = username
		self.apiSite = apiSite
		self.tokenPath = tokenPath
		self.logging = loggingHandler
		#Read token
		self.token = self.readToken()
		self.toRestore = {}
	
	res = {
		"ONLINE": "Files already online",
		"WAIT": "Wait before next refresh",
		"RESTORING": True,
		"ALREADY_REQ": "Link already requested"
	}

	def readToken(self):
		"""
		Read the token from the given url
		:return: The read API token
		"""
		file = open(self.tokenPath, "r")
		if not file:
			self.logging.error('Token file not read - Cannot execute any request')
			exit()
		token = file.read().strip()
		self.logging.info('ApiHandler - readToken - IUB Token read from file '+self.tokenPath)
		return token

	def getActiveGenres(self):
		"""
		Request the available genres
		:return: The list of active genres
		"""
		req = "getActiveGenre"
		r = requests.post(self.apiSite+"/api/genre.php", data={'user': self.username, 'psw': self.token, 'req': req})
		return json.loads(r.text)

	def searchRelease(self, title):
		"""
		Search a certain title
		:param title: The title to search
		:return:
		"""
		req = "searchTitles"
		r = requests.post(self.apiSite+"/api/release.php", data={'user': self.username, 'psw': self.token, 'req': req, 'title': title})
		return json.loads(r.text)
	
	#Download a certain release
	def downloadRelease(self, releaseId):
		req = "download_tm"
		r = requests.post(self.apiSite+"/api/download.php", data={'user': self.username, 'psw': self.token, 'req': req,  'code': releaseId})
		return json.loads(r.text)
	
	#Array of IUB genres 
	# 0	-> id
	# 1	-> name
	def getAllGenres(self):
		req = "listAllGenre"
		r = requests.post(self.apiSite+"/api/genre.php", data={'user': self.username, 'psw': self.token, 'req': req})
		return self.decode(r)
	
	#Return the list of all releases to save
	def getAllReleasesToSave(self):
		self.logging.info('Requested all releases that need to be saved')
		req = "get_all_releases_to_save"
		r = requests.post(self.apiSite+"/api/release_saver.php", data={'user': self.username, 'psw': self.token, 'req': req})
		return self.getParsedResponse(self.decode(r))
	
	#Retrieve the list of all releases in a free 1fichier account from the server		
	def getAllReleasesPerFreeAccount(self):
		self.logging.info('Requested all releases with a free account')
		req = "get_all_releases_per_account"
		r = requests.post(self.apiSite+"/api/release.php", data={'user': self.username, 'psw': self.token, 'req': req})
		return self.decode(r)
	
	#Retrieve the list of all materials having the given materials
	def getAllReleases(self, genres):
		self.logging.info("Request all releases present in the server")
		req = "get_all_releases"
		r = requests.post(self.apiSite+"/api/release.php", data={'user': self.username, 'psw': self.token, 'req': req, 'genres': json.dumps(genres)})
		return self.decode(r)
		
	#Creates the dictionaries
	def manageReleases(self):
		all_rel = self.getAllReleasesPerFreeAccount()
		#Creates a list of all releases ignoring the genre
		for genre in all_rel:
			for account in all_rel[genre]:
				#Creates array in the dictionary if needed
				try:
					self.toRestore[account]
				except KeyError:
					self.logging.info("Generated key in library for: "+account)
					self.toRestore[account] = []
				
				#Populate dictionary
				for release in all_rel[genre][account]:
					self.toRestore[account].append(release)
		
		#Log the account to check
		for account in self.toRestore:
			now = len(self.toRestore[account])
			self.logging.info("Account: "+account+" - To check "+str(now)+" releases")
	
	#Restore a single release
	# TODO - Reimplement WAIT!!!
	def restoreRelease(self, code):
		self.logging.debug('Request restore: '+str(code))
		req = "refresh_1f"
		r = requests.post(self.apiSite+"/api/release_refresher.php", data={'code': code, 'user': self.username, 'psw': self.token, 'req': req})
		return self.decode(r)
		
	#Start restoring all until I can only wait
	def restoreAll(self):
		cloneToRestore = self.toRestore.copy()
		#Iterate over all account
		for account in cloneToRestore:
			now = len(self.toRestore[account])
			print("START: Account: "+account+" - To check "+str(now)+" releases")
			#Create initial copy and iterate over it
			new_list = self.toRestore[account].copy()
			#Iterate over all the releases
			for code in new_list:
				try:
					resp = self.restoreRelease(code)

					if resp == self.res["ONLINE"]:
						self.logging.debug('Already online: '+str(code))
						self.removeObject(account, code)
					elif resp == self.res["WAIT"]:
						#Exit from this loop and not remove the object!
						self.logging.debug('Wait before new request: '+str(code)+'\nExit from loop')
						break
					elif self.res["RESTORING"]:
						print("Restoring: "+str(code))
						self.logging.info('Restore request successful: '+str(code))
						self.removeObject(account, code)
					elif resp == self.res["ALREADY_REQ"]:
						print("Already requested: "+str(code))
						self.logging.warning('Unexpected: Restore already requested of: '+str(code))
						self.removeObject(account, code)
				except Exception as e:
					print("Problem restoring release: " + str(code) + " [" + str(e) + "]")
					self.logging.error("Problem restoring release: "+str(code))
				
				print(str(random.randrange(0, 1000)/1000))
				time.sleep(random.randrange(0, 1000)/1000)
				
			after = len(self.toRestore[account])
			print("STOP: Account: "+account+" - To check "+str(after)+" releases")
			#Remove empty dictionaries
			if not after:
				lib_bef = len(self.toRestore)
				print(account+" removed")
				self.toRestore.pop(account, None)
				lib_aft = len(self.toRestore)
				self.logging.info("Removed account: "+account+" - Before: "+str(lib_bef)+' elem - After: '+str(lib_aft))
			else:
				print("There are still "+str(after)+" elements for account: "+account)

	def removeObject(self, account, item):
		"""
		Remove an object from the original library
		:param account: The account used for the item
		:param item: The item to remove
		:return:
		"""
		self.logging.debug('Remove: '+str(item)+' from '+account)
		elem_before = len(self.toRestore[account])
		self.toRestore[account].remove(item)
		elem_after = len(self.toRestore[account])
		self.logging.debug('-->Before: '+str(elem_before)+' Now: '+str(elem_after))

	def countObjectLeft(self):
		"""
		Return the count of objects left
		:return: The number of objects left
		"""
		numElem = 0
		for account in self.toRestore:
			numElem += len(self.toRestore[account])
		return numElem
	
	#Insert a new material		
	def insertNewMaterial(self, type_file, number_files):
		self.logging.info('Inserting: '+type_file)
		req = "insert_new_material"
		#Send request
		r = requests.post(
			self.apiSite+"/api/release.php",
			data={
				'user': self.username, 
				'psw': self.token, 
				'req': req, 
				'num': number_files,
				'material': type_file
			}
		)
		#Control if the response is ok
		try:
			res = json.loads(r.text)
			print("Parsed json response: "+str(res))
			if "upped" in res:
				return int(res["upped"])
			else:
				self.logging.error("Not found appropriate upped key ["+r.text+"]")
				return 0
		except (ValueError, TypeError) as e:
			self.logging.error("Error decoding Json response ["+r.text+"] [" + str(e) + "]")
			return 0

	#Return the count of left objects
	def orderThisRelease(self, code):
		self.logging.debug('Ordering: '+str(code))
		req = "order_prem_dir_fichier"
		r = requests.post(self.apiSite+"/api/release.php", data={'code': code, 'user': self.username, 'psw': self.token, 'req': req})
		return self.decode(r)
	
	#Request the available genres
	def saveRelease(self, code):
		req = "save_release"
		r = requests.post(self.apiSite+"/api/release_saver.php", data={'user': self.username, 'psw': self.token, 'req': req, 'code': code})
		return self.getParsedResponse(self.decode(r))

	#Request to refresh the premium links inside the DB taking them from the directory
	def refreshPremiumLinks(self, code):
		req = "new_1f_links"
		r = requests.post(self.apiSite+"/api/release.php", data={'user': self.username, 'psw': self.token, 'req': req, 'code': code})
		return self.decode(r)
	
	#Refresh torrent cache
	def refreshTorrentCache(self):
		req = "icv_refresh_cache"
		r = requests.post(self.apiSite+"/api/torrent.php", data={'user': self.username, 'psw': self.token, 'req': req})
		return self.decode(r)
			
	def decode(self, r):
		try:
			return json.loads(r.text)
		except ValueError as e:
			self.logging.error("Cannot decode: " + r.text + "[" + str(e) + "]")
			return r.text
		except Exception as e:
			self.logging.exception("JSON decode error [" + str(e) + "]")

	def getParsedResponse(self, result):
		if type(result) is not dict:
			self.logging.error("Expected a dict, obtained a " + type(result))
			print("Expected a dict, obtained a " + type(result))
			return result
		else:
			return result['result']


class UnknownTypeFile(Exception):
	"""
	Custom exceptions for unknown file type
	"""
	pass
