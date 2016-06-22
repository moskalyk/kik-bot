import requests
import json

from kik.messages import TextMessage, TextResponse, \
	SuggestedResponseKeyboard, messages_from_json
from kik import KikApi, Configuration
from flask import Response
from ..stateless_engine.Engine import Engine

class Kik_Helper:
	def __init__(self, username, api_key):
		self.engine = Engine()
		self.username = username
		self.api_key = api_key
		self.kik = KikApi(username, api_key)

	def set_config(self, end_point, manually_send_read_receipts,
				  receive_read_receipts, receive_delivery_receipts, receive_is_typing):
		requests.post(
			'https://api.kik.com/v1/config',
			auth=(self.username, self.api_key),
			headers={
				'Content-Type': 'application/json'
			},
			data=json.dumps({
				"webhook": end_point,
				"features": {
					"manuallySendReadReceipts": manually_send_read_receipts,
					"receiveReadReceipts": receive_read_receipts,
					"receiveDeliveryReceipts": receive_delivery_receipts,
					"receiveIsTyping": receive_is_typing
				}
			})
		)
		return Response(status=200)

	def check_config(self):
		config = self.kik.get_configuration()
		return config.webhook

	def send_messages(self, request):

		if not self.kik.verify_signature(request.headers.get('X-Kik-Signature'), request.get_data()):
			return Response(status=403)

		messages = messages_from_json(request.json['messages'])
		for message in messages:
			if isinstance(message, TextMessage):
				self.kik.send_messages(self.__choose_response(message))

		return Response(status=200)

	def __choose_response(self, message):
		messages = []
		response = self.engine.computeResponse(message.body)

		message = TextMessage(
			to=message.from_user,
			chat_id=message.chat_id,
			body=response
		)

		message.keyboards.append(
			SuggestedResponseKeyboard(
				hidden = False,
				responses = [TextResponse('OK')]
			)
		)

		messages.append(message)

		return messages

