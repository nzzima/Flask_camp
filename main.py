from flask import Flask

app = Flask(__name__)


@app.route("/")                                 #Decorator
def main():                                     #Creating function
    return "<h1>Hello my dear students!</h1>"\
           "<a href='/info'>About me</a><br>"\
           "<a href = '/calc/1/5'>Calculate</a>"

@app.route("/info")                             #Decorator
def info():                                     #Creating function
    return "<b>Creating by Krylov</b>"          #b - bold font

@app.route("/calc/<x>/<y>")
def calc(x, y):
    return f"{x} + {y} = {int(x) + int(y)}"


if __name__ == "__main__":
    app.run()