from ..luis.Luis import Luis
from ..faq.responses import faq
import ruamel.yaml as yaml

class Engine:
	def __init__(self):
		self.luis = Luis()

	def computeResponse(self, message):
		response = faq[self.luis.query(message)]
		print(response)
		return response['text']