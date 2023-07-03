from flask import Flask, render_template, request, redirect, url_for
import pyshorteners

# Initializing Flask instance
app = Flask(__name__)

@app.route('/')
def redirect_to_index():
    return redirect(url_for('index'))

@app.route('/index', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        #Getting The value of input from the HTML page which is index.html
        long_url = request.form['url']
        if long_url:
            # TinyURL shortener service
            type_tiny = pyshorteners.Shortener()
            short_url = type_tiny.tinyurl.short(long_url)
        return render_template('index.html',url=short_url)
    else:
        return render_template('index.html')

#Running the application
if __name__ == '__main__':
    #allow debug mode 
    app.run(debug=True)
