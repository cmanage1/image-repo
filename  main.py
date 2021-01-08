from flask import Flask, render_template
import sqlite3 as sql

app = Flask( __name__)

@app.route('/', methods=['GET'])
def main():
    return 'Hi'

if __name__ == '__main__':
    app.run(debug=True)