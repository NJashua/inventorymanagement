from flask import Flask, request, redirect, render_template

app = Flask(__name__)

@app.route('/square', methods = ['GET'])
def square_num():
    if request.method == 'GET':
        if(request.args.get('num') == None):
            return render_template("squarenum.html")
        elif (request.args.get('num') == ''):
            return "<html><body><h1>Invalid number entered budy</h1></body></html>"
        else:
            number = request.args.get('num')
            sq = int(number) * int(number)

            return render_template('answer.html', square_num=sq, num=number)

if __name__ == '__main__':
    app.run(debug=True)