from flask import *
import json, time
from flask import jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home_page():
        data_set = {'Page':'Home'}
        json_dump = json.dumps(data_set)

        return json_dump

@app.route('/user/', methods=['GET'])
def request_page():
        user_query = str(request.args.get('user'))

        data_set = {'Page':'Request', 'user':user_query}
        json_dump = json.dumps(data_set)

        return json_dump


@app.route('/data/', methods=['GET'])
def wordle_page():
        data = get_wordle_data_set()
        response = jsonify({'Page':'Wordle', 'data': data, 'avg': 1324})
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response

def get_wordle_data_set():
    f = open("data/cuvinte_wordle.txt", "r")  
    return [line[:-1] for line in f]


if __name__ == '__main__':
    app.run(port=8000)

