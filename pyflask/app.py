from flask import Flask
from flask import render_template, request
import solve


app = Flask(__name__)

@app.route('/')
def index ():
    pagetitle = "Palindrome Solver"
    return render_template('index.html',
        mytitle=pagetitle)

@app.route('/palindrome', methods=['GET','POST'])
def palindrome ():
    pagetitle = "Palindrome Results"
    palindrome = request.form['palindrome']
    palindromeList = solve.palindromes(palindrome)
    return render_template('palin_palin.html',
        pagetitle=pagetitle,
        input = palindrome,
        output = palindromeList)
    
    
if __name__ == "__main__":
    app.run(debug=True)