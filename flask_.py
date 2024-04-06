from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/add', methods=['POST'])
def add_numbers():
    data = request.get_json()
    if 'num1' in data and 'num2' in data:
        num1 = data['num1']
        num2 = data['num2']
        if isinstance(num1, int) and isinstance(num2, int):
            result = num1 + num2
            return jsonify({'result': result})
        else:
            return jsonify({'error': 'Invalid input. Both numbers must be integers.'})
    else:
        return jsonify({'error': 'Invalid input. Please provide both num1 and num2.'})

if __name__ == '__main__':
    app.run(debug=True)
