from flask import Flask, render_template
app = Flask(__name__)  

@app.route('/play')          
def play():
    return render_template('index.html', number = 3) 

@app.route('/play/<number>')          
def play_number(number):
    # print(render_template('index.html'))
    return render_template('index.html', number = int(number))

@app.route('/play/<number>/<color>')          
def play_color(number, color):
    color=color
    return render_template('index.html',  color=color, number = int(number))


if __name__=="__main__":      
    app.run(debug=True, port=5001)    

