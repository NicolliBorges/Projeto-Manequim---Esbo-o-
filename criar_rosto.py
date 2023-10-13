from flask import Flask, render_template

app = Flask(__name__)

@app.route('/rostro3d')
def rosto3d():
    return render_template('rostro3d.html')

if __name__ == '__main__':
    app.run(debug=True)
