from flask import Flask, request
import os
from controller.db_request import *
from model.db_data import *

app = Flask(__name__)


@app.route('/insert', methods=['GET', 'POST'])
def home(data="ya russkiy"):
 if request.method == 'POST':
    result = request.get_json()
    data = result['text']
    conn = get_db_donnect()
    insert_some_data(data, conn)
    return f"Sucess insert. Insert data: {data}"

@app.route('/select')
def buttom():
    conn = get_db_donnect()
    result = select_data(conn)
    return result

@app.route('/', methods=['GET', 'POST'])
def home_page():
    return f'Succes connect to web. {give_dict_conn_data()}'

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 3222))
    app.run(debug=True, host='0.0.0.0', port=port)