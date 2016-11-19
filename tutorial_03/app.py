from flask import Flask, request, Response

from kik import KikApi, Configuration
from kik.messages import messages_from_json, TextMessage, VideoMessage

##### NEW #####
from config import username, api_key, webhook

##### NEW #####
from giphypop import translate

app = Flask(__name__)
kik = KikApi(username, api_key)
kik.set_configuration(Configuration(webhook=webhook))

######
def giffy(message):
    img = translate(message, api_key='dc6zaTOxFJmzC')
    gif = img.fixed_height.url
    print(gif)
    return gif
#######

@app.route('/incoming', methods=['POST'])
def incoming():
    print('coming in here')
    if not kik.verify_signature(request.headers.get('X-Kik-Signature'), request.get_data()):
        return Response(status=403)

    messages = messages_from_json(request.json['messages'])
    
    for message in messages:
        if isinstance(message, TextMessage):
            kik.send_messages([
                ####### NEW #######
                VideoMessage(
                    message.from_user, 
                    message.chat_id, 
                    video_url=giffy(message), 
                    loop=True, 
                    autoplay=True
                )
                ###################
            ])

    return Response(status=200)


if __name__ == "__main__":
    app.run(port=8080, debug=True)