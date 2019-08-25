from flask import Flask, jsonify, request, render_template


app = Flask(__name__)
stores = [
    {
        'name': 'My Wonderful Store',
        'items': [
            {
                'name': 'My Item',
                'price': 15.99
            }
        ]
    }
]


@app.route('/')
def home():
    return render_template('index.html')


# POST /store data: {name:}
@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)


# GET /store/<string:name>
@app.route('/store/<string:name>')
def get_store(name: str):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message': 'Error! Store does not exist!'})


# GET /store
@app.route('/store')
def get_stores():
    return jsonify({'stores': stores})


# POST /store/<string:name>/item{name:, price:}
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item(name: str):
    request_data = request.get_json()
    new_item = {'name': request_data['name'],
                'price': request_data['price']}
    for store in stores:
        if store['name'] == name:
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message': 'Error! Store does not exist!'})


# GET /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_item(name: str):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items': store['items']})
    return jsonify({'message': 'Error! Store does not exist!'})


if __name__ == "__main__":
    app.run()
