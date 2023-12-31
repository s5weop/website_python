from flask import Flask, render_template, url_for, request, redirect
from g4f import ChatCompletion, models

app = Flask(__name__)


def get_response_GPT(request_for_GPT):
    response = ChatCompletion.create(
        model=models.gpt_35_turbo,
        messages=[{"role": "user", "content": request_for_GPT}],
        proxy="http://host:port"
    )
    return response


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/1')
def first():
    return render_template('1.html')


@app.route('/2')
def second():
    return render_template('2.html')


@app.route('/3')
def third():
    return render_template('3.html')


@app.route('/4')
def fourth():
    return render_template('4.html')


@app.route('/support', methods=['POST', 'GET'])
def support():
    if request.method == 'POST':
        request_for_GPT = request.form['request_user']
        answer_gpt = get_response_GPT(request_for_GPT)
        return render_template('support.html', answer_gpt=answer_gpt)
    else:
        return render_template('support.html', answer_gpt='Hello, I am bot helper!')


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=False)