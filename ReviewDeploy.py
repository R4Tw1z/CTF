from flask import Flask, request

app = Flask(__name__)

FLAG = "R4Tw1z{d1d_y0u_r3m0v3_7h3_c0mm3n75}"

@app.route('/')
def index():
    return """
    <html>
    <head>
        <title>Smart IoT Login</title>
    </head>
    <body style="text-align:center;">
        <h1>IoT Smart Home</h1>
        <p>The smart home security system requires authentication. Can you log in?</p>

        <h2>Login</h2>
        <form action="/login" method="POST">
            <input type="text" name="username" placeholder="Username">
            <input type="password" name="password" placeholder="Password">
            <input type="submit" value="Submit">
        </form>

        <!-- TODO: Please Make sure this is Removed ("Remove this before deployment") -->
        <!-- A!].Siap5GApoIT: NDkgNmYgNTQgMmQgNTMgNjUgNjMgNzIgNjUgNzQgMmQgMzEgMzIgMzM= -->
    </body>
    </html>
    """

@app.route('/login', methods=['POST'])
def login():
    return "Invalid credentials. Try again!"

@app.route('/ks3bitesize')
def backdoor():
    access_key = request.headers.get("X-Access-Key")

    if access_key == "IoT-Secret-123":
        return f"Congrats! Here is your flag: {FLAG}"
    
    return "403 Forbidden - Unauthorized access"

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=50000)
