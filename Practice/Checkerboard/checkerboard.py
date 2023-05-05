from flask import Flask, render_template
app = Flask(__name__)  

@app.route('/')                  
def standard():
    return render_template('index.html', number1=int(4), number2=int(4))

@app.route('/4')                  
def four():
    return render_template('index.html', number1=int(4), number2=int(2))

@app.route('/<int:x>/<int:y>')                  
def size(x,y):
    return render_template('index.html', number1=x, number2=y)

@app.route('/<int:x>/<int:y>/<color1>/<color2>')                  
def color(x,y,color1, color2):
    return render_template('index.html', number1=x, number2=y, color1=color1, color2=color2)

if __name__=="__main__":      
    app.run(debug=True, port=5002)    
