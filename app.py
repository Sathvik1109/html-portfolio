from flask import Flask, render_template

# Initialize the Flask app
app = Flask(__name__)

# Define the homepage route
@app.route('/')
def home():
    return "Hello, Flask!"

# Another route for a greeting page
@app.route('/greet/<name>')
def greet(name):
    return f"Hello, {name}! Welcome to the Flask app."

# Running the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
