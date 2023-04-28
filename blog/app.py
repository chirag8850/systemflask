from flask import Flask, render_template, request

app = Flask(__name__)

posts = [
    {
        'title': 'Post 1',
        'content': 'This is the first post.'
    },
    {
        'title': 'Post 2',
        'content': 'This is the second post.'
    }
]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        posts.append({'title': title, 'content': content})
    return render_template('index.html', posts=posts)

if __name__ == '__main__':
    app.run(debug=True)