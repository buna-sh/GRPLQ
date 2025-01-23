from flask import Flask, jsonify, request
import threading
from werkzeug.serving import make_server
from colorama import Fore, Style, init



MODULE_NAME = "Flask Module"
VERSION = "1.0.0"


init(autoreset=True)

# Create the Flask app
app = Flask(__name__)

# Define a sample route
@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Flask Module!"})

@app.route('/echo', methods=['POST'])
def echo():
    """
    A route that echoes back the posted JSON data.
    Example request:
    POST /echo
    {
        "data": "Hello, Flask!"
    }
    """
    data = request.json
    if not data:
        return jsonify({"error": "No JSON data provided"}), 400
    return jsonify({"echoed": data})


class FlaskServerThread:
    """
    Manages the Flask server in a background thread.
    """

    def __init__(self):
        self.server = make_server('0.0.0.0', 5000, app)  # Create a Werkzeug server
        self.server_thread = threading.Thread(target=self.server.serve_forever, daemon=True)
        self.is_running = False

    def start(self):
        """Starts the Flask server in a background thread."""
        if not self.is_running:
            print("Starting Flask app in background...")
            self.server_thread.start()
            self.is_running = True
            print("Flask server is now running in the background.")
        else:
            print("Flask server is already running.")

    def stop(self):
        """Stops the Flask server."""
        if self.is_running:
            print("Stopping Flask server...")
            self.server.shutdown()
            self.server_thread.join()
            self.is_running = False
            print("Flask server has stopped.")
        else:
            print("Flask server is not running.")



# Create a FlaskServerThread instance
flask_server = FlaskServerThread()

def run():
    """
    Starts the Flask server in the background.
    """
    flask_server.start()

def stop():
    """
    Stops the Flask server.
    """
    flask_server.stop()



