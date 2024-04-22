from flask import Flask

app = Flask(__name__)
@app.route('/home')
def hello_flask():
    name = "Flask"
    return "Nithin says Hello,{} ".format(name)

if __name__ == '__main__':
    app.run()