from flask import Flask,render_template,request,jsonify
from pythonFiles.InfixToPostfix import InfixExpression
from pythonFiles.PostfixToInfix import PostfixExpression

    # created by G Daniel Vineel


app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/infix-postfix")
def infix():
    return render_template("infix-postfix.html")

@app.route("/postfix-infix")
def postfix():
    return render_template("postfix-infix.html")

@app.route("/InToPost",methods=["POST"])
def getPostfixExpression():
    data=request.json.get("expression"," ")
    
    expression=data.replace(" ","")
    try:
        postfixExpression=InfixExpression(expression).getPostfixExpression()
        
        return f"{postfixExpression}"
    except Exception as e:
        return f"Invalid Syntax"

@app.route("/PostToIn",methods=["POST"])
def getInfixExpression():
    expression=request.json.get("expression"," ")
    
    try:
        postfixExpression=PostfixExpression(expression).getInfixExpression()
        
        return f"{postfixExpression}"
    except Exception as e:
        return f"Invalid Syntax"

if(__name__=="__main__"):
    app.run(host="127.0.0.1",port=300,debug=True)

    # created by G Daniel Vineel