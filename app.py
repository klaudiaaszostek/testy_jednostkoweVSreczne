from flask import Flask, jsonify, request, render_template, redirect, url_for

app = Flask(__name__)

users = []

@app.route('/')
def index():
    return render_template('index.html', users=users)

@app.route('/user', methods=['POST'])
def create_user():
    name = request.form.get('name')
    if not name:
        return jsonify({'error': 'Invalid data'}), 400
    user = {'id': len(users) + 1, 'name': name}
    users.append(user)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
