from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # replace with your secret key

@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        fname = request.form.get('fname')
        lname = request.form.get('lname')

        if not fname or not lname:
            flash('All fields are mandatory')
            return redirect(request.url)
        
        if not all(part.isalpha() for part in fname.split()) or not all(part.isalpha() for part in lname.split()):
            flash('Names must only contain alphabetic characters')
            return redirect(request.url)
        
        flash('Successful submission')
        return redirect(request.url)

    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True, port = 4000)