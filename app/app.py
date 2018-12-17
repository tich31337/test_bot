from flask import Flask
from flask_restplus import Api, Resource, fields
from envparse import env

import requests

env.read_envfile()

app = Flask(__name__)
api = Api(app)

model = api.model('Model', {
    'text': fields.String,
})


class Text:
    def __init__(self):
        self._text = None
        self._observers = set()

    def attach(self, observer):
        self._observers.add(observer)

    def deatach(self, observer):
        self._observers.remove(observer)

    def get_data(self):
        return self._text

    def set_data(self, text):
        self._text = text
        self.notify(text)

    def notify(self, text):
        for observer in self._observers:
            observer.send_message(text)


class ObserverBase:
    def send_message(self, text):
        raise NotImplementedError()


class Telegram(ObserverBase):
    def __init__(self, token):
        self.url = "https://api.telegram.org/bot{}/".format(token)

    def send_message(self, text):
        params = {'chat_id': '@test_chanel171218', 'text': text}
        response = requests.post(self.url + 'sendMessage', data=params)
        return response


@api.route('/api')
class RestService(Resource):

    @api.expect(model)
    @api.marshal_with(model)
    def post(self):
        text = api.payload.get('text', '')
        if not text:
            return {'message': 'Error'}, 400
        text_class.set_data(text)
        return {'message': 'ok'}, 201


text_class = Text()
text_class.attach(Telegram(env('TELEGRAM_TOKEN')))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
