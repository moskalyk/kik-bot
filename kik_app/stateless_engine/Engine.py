from ..luis.Luis import Luis
from ..faq.responses import faq

class Engine:
	def __init__(self):
		self.luis = Luis()

	def computeResponse(self, message):
		response = faq[self.luis.query(message)]
		print('Response', response)
		for response_type in response:

			if response_type is 'text':
				return response, 'text'

			elif response_type is 'attachment':

				if response[response_type]['type'] is 'template':
					return response, 'buttons'

				elif response[response_type]['type'] is 'image':
					return response, 'image'
			break
