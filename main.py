from flask import Flask, render_template, request
import sys
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if request.form['submit_button'] == 'Run Full Scan':
            os.system("notify-send 'SpiderClam' 'Starting Full ClamAV Scan'")
            os.system("clamscan -r --quiet --bell --remove=yes /")
            print('Running Full Scan')
            return render_template('index.html')
        
        elif request.form['submit_button'] == 'Run':
            os.system("notify-send 'SpiderClam' 'Fresh Clam has started an update'")
            os.system("freshclam --show progress")
            return render_template('index.html')
        else:
            pass # unknown
    elif request.method == 'GET':
        return render_template('index.html')

        if "__name__" == "__main__":
            app.run(debug=True)
