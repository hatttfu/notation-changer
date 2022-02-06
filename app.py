from flask import Flask, render_template, redirect, url_for, request, flash

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route("/", methods=['GET', 'POST'])
def index():
    return redirect(url_for('to_two'))

@app.route("/to_two", methods=['GET', 'POST'])
def to_two():
    if request.method == 'POST':
        number = request.form.get('number')
        if number != '':
            result = bin(int(number))
        
            return render_template("totwo.html", number=number, result=result)
        else:
            flash('Введи число!!!')
    return render_template("totwo.html")
    
@app.route("/to_ten", methods=['GET', 'POST'])
def to_ten():
    if request.method == 'POST':
        number = request.form.get('number')
        if number != '':
            result = int(number, 2)
            
            return render_template("toten.html", number=number, result=result)
        else:
            flash('Введи число!!!')
    return render_template("toten.html")
    

if __name__ == '__main__':
    app.run(debug=True)