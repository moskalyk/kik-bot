from flask import request, Response, Blueprint
from ..easy_kik.Kik_Helper import Kik_Helper
from ..credentials.username_api import username, api_key

kik_helper = Kik_Helper( username=username, api_key=api_key)
main = Blueprint('main', __name__)

@main.route('/')
def index():
	return Response(status=200)

@main.route('/config', methods=['POST'])
def setConfig():
	return kik_helper.set_config( str(request.form['end_point']) + 'incoming', False, False, False, False)

@main.route('/config', methods=['GET'])
def config():
	return kik_helper.check_config()

@main.route('/incoming', methods=['POST'])
def incoming():
    return kik_helper.send_messages(request)