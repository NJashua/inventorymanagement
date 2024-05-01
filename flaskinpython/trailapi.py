from flask import Flask

app = Flask("__name")

@app.route('/post/<int:id>')
def get_num(id):
    return f"the return id is {id}"
@app.route('/post/<username>')
def username(username):
    return f"name of person is {username}"
           

if __name__ == "__main__":
    app.run(debug=True)