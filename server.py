import random
from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "yeeterskeeter"

# our index route will handle rendering our form
@app.route('/')
def index():
    if 'rando_num' not in session:
        session['rando_num'] = random.randint(1,100)
        session['feedback'] = 'new_game'
    print(session['rando_num'])
    return render_template('index.html')

@app.route('/check_num', methods=['POST'])
def check_num():

    if 'attempts' in session:
        session['attempts'] += 1
    else:
        session['attempts'] = 1

    if session['rando_num'] == int(request.form['user_input']):
        session['feedback'] = 'correct'
    elif session['rando_num'] < int(request.form['user_input']):
        session['feedback'] = 'hi'
    else:
        session['feedback'] = 'low'
    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)

