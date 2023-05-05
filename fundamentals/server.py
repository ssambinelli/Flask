from flask import Flask
app = Flask(__name__)  

@app.route('/')          
def hello_world():
    return 'Hello World!' 

@app.route('/dojo')        
def dojo():
    return 'Dojo!'   

@app.route('/say/<name>')
def say(name):
    print(name)
    return 'Hi, ' + str(name.capitalize())

@app.route('/repeat/<number>/<word>')
def repeat(number, word):
    print(word)
    return str(word) * int(number)

#Handling error 404 and displaying relevant web page
@app.errorhandler(404)
def not_found_error(error):
    return ('Sorry! No response. Try again.'),404

if __name__=="__main__":      
    app.run(debug=True)    

