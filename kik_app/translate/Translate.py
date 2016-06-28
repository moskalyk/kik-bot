import requests

class Translate:
	def __init__(self):
		self.url = 'https://www.googleapis.com/language/translate/v2'
		self.key = 'AIzaSyD88YmDJil9N_KTYjks1mDco1xEpGZ_ugs',

	def translate(self, source_language, target_langauge, text):

		payload = {
			'key': self.key,
			'source': source_language,
			'target': target_langauge,
			'q': text
		}

		headers = { 'Content-Type': 'charset=UTF-8' }
		r = requests.get(self.url, params=payload,  headers=headers)
		print(r.json())
		return r.json()