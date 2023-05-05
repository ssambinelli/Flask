from flask import Flask, render_template, redirect, session
app = Flask(__name__) 
app.secret_key='hello'
@app.route('/')
def counter():
    if 'count' in session:
        session['count'] += 1
    else:
        session['count'] =1
    print(session['count'])
    return render_template('index.html', count = session['count'])


@app.route('/destroy_session')
def destroy():
    session.clear()
    return redirect('/')

if __name__=="__main__":      
    app.run(debug=True, port=5001) 