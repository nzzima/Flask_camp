from flask import Flask

app = Flask(__name__)


@app.route("/", methods=['GET'])                #Decorator
def main():                                     #Creating function
    return "<h1>Hello my dear students!</h1>"   #h1 - first header in HTML


if __name__ == "__main__":
    app.run()