from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

users = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user', methods=['POST'])
def create_user():
    data = request.get_json()
    if not data or 'name' not in data:
        return jsonify({'error': 'Invalid data'}), 400
    user = {'id': len(users) + 1, 'name': data['name']}
    users.append(user)
    return jsonify(user), 201

if __name__ == '__main__':
    app.run(debug=True)
