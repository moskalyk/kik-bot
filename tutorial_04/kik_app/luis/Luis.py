import urllib
from ..credentials.username_api import luis_url
import ruamel.yaml as yaml

class Luis:
	def __init__(self):
		self.URL = luis_url

	def query(self, message):
		print(message)
		print(type(message))

		encoded_message = urllib.parse.quote_plus(message)
		luis_endpoint = self.URL + '=' + encoded_message
		raw_result = urllib.request.urlopen(luis_endpoint).read()
		parsed_result = yaml.safe_load(raw_result)
		return parsed_result['intents'][0]['intent']