from flask import Flask, render_template, request, jsonify
from lexer import html_lexer
from parser import html_parser

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/compile', methods=['POST'])
def compile():
    code = request.form.get('code', '')
    try:
        tokens = html_lexer(code)
        output = html_parser(tokens)
        return jsonify({'success': True, 'output': output})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

@app.route('/fix', methods=['POST'])
def fix():
    code = request.form.get('code', '')
    try:
        tokens = html_lexer(code)
        fixed_code = html_parser(tokens, fix_errors=True)
        return jsonify({'success': True, 'fixed_code': fixed_code})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
