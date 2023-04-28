from flask import Flask, render_template, request, redirect, url_for, flash
app = Flask(__name__)
app.secret_key = 'your_secret_key'
@app.route('/', methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        feedback = request.form['feedback']
        flash(f'Thank you {name}, your feedback has been submitted.', 'success')
        return redirect(url_for('feedback'))
    return render_template('feedback.html')
if __name__ == '__main__':
    app.run(debug=True)