from flask import Blueprint
from controllers.pages import home, insert, subscribe, unsubscribe

blueprint = Blueprint('blueprint', __name__, template_folder="/templates")

blueprint.route('/', methods=['GET'])(home)
blueprint.route('/insert', methods=['GET'])(insert)
blueprint.route('/subscribe', methods=['POST'])(subscribe)
blueprint.route('/unsubscribe', methods=['GET', 'POST'])(unsubscribe)