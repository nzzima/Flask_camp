from flask import Flask, render_template
from reg import RegisterForm

app = Flask(__name__, template_folder='templates')
app.config['SECRET_KEY'] = 'nzzima nzzima nzzima nzzima'

@app.route("/")                                 #Decorator
def main():                                     #Creating function
    return  "<h1>Hello my dear students!</h1>"\
            "<a href='/info'>About me</a><br>"\
            "<a href = '/calc/1/5'>Calculate</a><br>"\
            "<a href = '/auth'>Authentication</a><br>"\
            "<a href = '/register'>Registration</a><br>"

@app.route("/info")                             #Decorator
def info():                                     #Creating function
    return "<b>Creating by Krylov</b>"          #b - bold font

@app.route("/calc/<x>/<y>")
def calc(x, y):
    return f"{x} + {y} = {int(x) + int(y)}"

@app.route("/auth", methods=['GET', 'POST'])
def auth():
    return render_template('auth.html', title='Authentication')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    
    if form.validate_on_submit():
        with open('db.txt', 'a', encoding='utf-8') as file:
            file.write(f"{form.data['name']};{form.data['email']};{form.data['password']}\n")
            
    return render_template('register.html', title='Registration', form=form)


if __name__ == "__main__":
    app.run()