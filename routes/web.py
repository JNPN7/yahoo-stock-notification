from flask import Blueprint
from controllers.pages import home, subscribe, unsubscribe, getStock, searchStock

blueprint = Blueprint('blueprint', __name__, template_folder="/templates")

blueprint.route('/', methods=['GET'])(home)
blueprint.route('/stock/', defaults={'stock_sym': None}, methods=['GET'])(getStock)
blueprint.route('/stock/<stock_sym>', methods=['GET'])(getStock)
blueprint.route('/search', methods=['POST'])(searchStock)
blueprint.route('/subscribe', methods=['POST'])(subscribe)
blueprint.route('/unsubscribe', methods=['GET', 'POST'])(unsubscribe)