from flask import Flask, request, jsonify

app = Flask(__name__)

# Mock foydalanuvchi ma'lumotlar bazasi (o'zingizning asl ma'lumotlar bazangiz bilan almashtiring)
users = {
    'john': 'secret123',
    'alice': 'password456'
}

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if username in users and users[username] == password:
        return jsonify({'message': 'Login muvaffaqiyatli'})
    else:
        return jsonify({'message': 'Notogri foydalanuvchi nomi yoki parol'}), 401

if __name__ == '__main__':
    app.run(debug=True)
