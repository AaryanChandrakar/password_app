from flask import Flask, request

import random
import string

app = Flask(__name__)

HTML_HEAD = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Password Generator by Aaryan Chandrakar</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body { background-color: #f0fff4; color: #333; }
        .container { margin-top: 80px; max-width: 600px; }
        .card { border-radius: 15px; box-shadow: 0 2px 8px rgba(0,0,0,0.2); }
        h1 { color: #198754; }
    </style>
</head>
<body>
<div class="container text-center">
"""

HTML_FOOT = """
</div>
</body>
</html>
"""

def generate_password(length=12, include_upper=True, include_digits=True, include_symbols=True):
    characters = string.ascii_lowercase
    if include_upper:
        characters += string.ascii_uppercase
    if include_digits:
        characters += string.digits
    if include_symbols:
        characters += "!@#$%^&*()-_=+[]{};:,.<>?/|"

    return ''.join(random.choice(characters) for _ in range(length))

@app.route('/', methods=['GET', 'POST'])
def home():
    password = ""
    if request.method == 'POST':
        length = int(request.form.get('length', 12))
        include_upper = 'upper' in request.form
        include_digits = 'digits' in request.form
        include_symbols = 'symbols' in request.form
        password = generate_password(length, include_upper, include_digits, include_symbols)

    content = f"""
    <div class="card p-4">
        <h1>🔐 Password Generator</h1>
        <form method="POST" class="mt-4">
            <div class="mb-3">
                <label for="length" class="form-label">Password Length:</label>
                <input type="number" id="length" name="length" value="12" min="4" max="50" class="form-control text-center">
            </div>
            <div class="form-check text-start ms-5">
                <input class="form-check-input" type="checkbox" name="upper" id="upper" checked>
                <label class="form-check-label" for="upper">Include Uppercase Letters</label>
            </div>
            <div class="form-check text-start ms-5">
                <input class="form-check-input" type="checkbox" name="digits" id="digits" checked>
                <label class="form-check-label" for="digits">Include Numbers</label>
            </div>
            <div class="form-check text-start ms-5 mb-3">
                <input class="form-check-input" type="checkbox" name="symbols" id="symbols" checked>
                <label class="form-check-label" for="symbols">Include Symbols</label>
            </div>
            <button type="submit" class="btn btn-success">Generate</button>
        </form>
        <hr>
        <h5 class="mt-3">Generated Password:</h5>
        <div class="alert alert-light border mt-2"><strong>{password}</strong></div>
    </div>
    """

    return HTML_HEAD + content + HTML_FOOT

if __name__ == '__main__':
    app.run(debug=True)
