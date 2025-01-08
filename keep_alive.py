from flask import Flask, request

app = Flask(__name__)

@app.route('/login', methods=['GET'])
def login():
    email = request.args.get('email')
    password = request.args.get('password')
    # Authenticate the user using email and password (server-side logic)
    return f"Logged in with email: {email} and password: {password}"

if __name__ == '__main__':
    app.run(debug=True)
