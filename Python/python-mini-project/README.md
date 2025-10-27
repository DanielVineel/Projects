# 🔁 Infix ↔ Postfix Converter (Flask App)
A simple **Flask** web app to convert **Infix to Postfix** and **Postfix to Infix** expressions with validation.  
Created by **G. Daniel Vineel**.

## ⚙️ Features
- Convert Infix ➜ Postfix  
- Convert Postfix ➜ Infix  
- Validates invalid syntax  
- Supports unary minus (-a)  
- Checks for balanced braces & operators  
- It considers multi-digit numbers like **10** as a single operand.  
- In **Postfix to Infix** conversion, the symbol **~** is used to represent unary negative values.  
- Spaces are **mandatory** to separate operands and operators, for example:  
  `10 ~20 + 30 *`
## 🗂️ Structure
app.py  
pythonFiles/ → InfixToPostfix.py, PostfixToInfix.py, Exceptions.py  
templates/ → index.html, infix-postfix.html, postfix-infix.html  

## 🚀 Run Locally
pip install flask  
python app.py  
Then open: http://127.0.0.1:300  

## 🔹 API
| Route | Method | Description |
|--------|--------|-------------|
| /InToPost | POST | Infix → Postfix |
| /PostToIn | POST | Postfix → Infix |

Example:  
POST /InToPost  
{"expression": "(a+b)*c"}  
Response → `a b + c *`

## 👨‍💻 Author
**G. Daniel Vineel**  
MIT License © 2025
🛡️ All commits in this repository are GPG-signed to verify authentic authorship by G. Daniel Vineel.
