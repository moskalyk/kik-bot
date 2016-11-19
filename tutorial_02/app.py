from flask import Flask, request, Response

from kik import KikApi, Configuration
from kik.messages import messages_from_json, TextMessage

username = "mmoskalyk"
api_key = "1caa1e1a-0aae-4377-8b87-ccddb4fcbf3b"
webhook = "http://1094d911.ngrok.io/incoming"

app = Flask(__name__)
kik = KikApi(username, api_key)
kik.set_configuration(Configuration(webhook=webhook))

@app.route('/incoming', methods=['POST'])
def incoming():
    print('coming in here')
    if not kik.verify_signature(request.headers.get('X-Kik-Signature'), request.get_data()):
        return Response(status=403)

    messages = messages_from_json(request.json['messages'])

    for message in messages:
        if isinstance(message, TextMessage):
            kik.send_messages([
                TextMessage(
                    to=message.from_user,
                    chat_id=message.chat_id,
                    body=message.body
                )
            ])

    return Response(status=200)


if __name__ == "__main__":
    app.run(port=8080, debug=True)