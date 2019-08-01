import json
from flask import Flask, jsonify, render_template, request


app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/save', methods=['POST'])
def save():
	dados = request.get_json()
	with open('cache.dat', 'w') as f:
		f.write(json.dumps(dados))
	return jsonify({'mensagem': 'Dados gravados'})

@app.route('/status')
def status():
	return jsonify({'mensagem': 'Olaaaaar Flask!'})

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000, debug=True)