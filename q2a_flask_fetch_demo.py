from flask import Flask, request

app = Flask(__name__)

# Run a local listener in another terminal: python -m http.server 8000
@app.route("/")
def demo():
    data = request.args.get("data", "test")
    return f'''
    <h2>Localhost Fetch Demo</h2>
    <p>Received: {data}</p>
    <button onclick="fetch('http://localhost:8000/?data=test')">Send Test Request to Port 8000</button>
    '''

if __name__ == "__main__":
    app.run(debug=True)
