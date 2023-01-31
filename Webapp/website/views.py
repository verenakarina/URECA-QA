from flask import Flask, Blueprint, render_template, request, redirect

# views = Blueprint('views', __name__)
views = Flask(__name__)

@views.route('/')
def index():
    return render_template('index.html')

@views.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']

    file.save(f'uploads/{file.filename}')

    return redirect('/')