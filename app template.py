Here is an example of a simple website created using Flask:

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=

You will need to create two HTML templates, `index.html` and `about.html`, in a `templates` folder within the same directory as your Flask app. Here is an example of what these templates might look like:

`index.html`:
```html
<!DOCTYPE html>

```

To run the website, save the Python code as `app.py` and run it in your terminal. You can then access the website by navigating to `http://127.0.0.1:5000/` in your web browser. This will display the homepage. You can then navigate to `http://127.0.0.1:5000/about` to see the About Us page.