from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def complex_json():
    return jsonify({
        'name': 'John Doe',
        'age': 30,
        'pets': ['cat', 'dog'],
        'address': {
            'street': '123 Main St',
            'city': 'Anytown',
            'state': 'Anystate',
            'zip': '12345'
        },
        'siblings': [
            {'name': 'Jane Doe', 'age': 25},
            {'name': 'Joe Doe', 'age': 35}
        ]
    })


if __name__ == '__main__':
    app.run()
