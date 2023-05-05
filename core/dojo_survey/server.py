from flask import Flask, render_template, request, redirect, session
app = Flask(__name__) 
app.secret_key='its a secret'

@app.route('/')
def survey():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    print(request.form)
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language']= request.form['language']
    session['submit'] = request.form['submit']
    # return render_template('result.html', name=name, location = location, language=language, submit=submit)
    return redirect('/result')

@app.route('/result')
def result():
    name = session['name']
    location = session['location']
    language = session['language']
    
    submit = session['submit']
    return render_template('result.html', name=name, location = location, language=language, submit=submit)



if __name__=="__main__":      
    app.run(debug=True, port=5001) 