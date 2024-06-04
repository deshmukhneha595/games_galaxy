from flask import Flask, request, jsonify
from flask_cors import CORS
import subprocess

app = Flask(__name__)
CORS(app)


@app.route('/run-tictactoe', methods=['GET'])
def run_tictactoe():
    try:
        subprocess.Popen(["python", "tictactoe.py"])
        return jsonify({"message": "Tic Tac Toe started"}), 200
    except Exception as e:
        return jsonify({"message": f"An error occurred: {str(e)}"}), 50


@app.route('/run-connect', methods=['GET'])
def run_connector():
    try:
        subprocess.Popen(["python", "connecter_game.py"])
        return jsonify({"message": "Connector game started"}), 200
    except Exception as e:
        return jsonify({"message": f"An error occurred: {str(e)}"}), 50


@app.route('/run-dino', methods=['GET'])
def run_dino():
    try:
        subprocess.Popen(["python", "dino/main.py"])
        return jsonify({"message": "Dino game started"}), 200
    except Exception as e:
        return jsonify({"message": f"An error occurred: {str(e)}"}), 50


@app.route('/run-snake', methods=['GET'])
def run_snake():
    try:
        subprocess.Popen(["python", "snake_and_apple/main.py"])
        return jsonify({"message": "Snake and apple game started"}), 200
    except Exception as e:
        return jsonify({"message": f"An error occurred: {str(e)}"}), 50


@app.route('/run-sandl', methods=['GET'])
def run_sandl():
    try:
        subprocess.Popen(["python", "snake_and_Ladder/main.py"])
        return jsonify({"message": "Dino game started"}), 200
    except Exception as e:
        return jsonify({"message": f"An error occurred: {str(e)}"}), 50


def process_data(data):
    # Example function to process data
    return {"message": "Hello from Python", "input": data}


if __name__ == '__main__':
    app.run(debug=True)
