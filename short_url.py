import random 
import string
from flask import Flask ,render_template, redirect,url_for,request
app = Flask(__name__)
shortened_urls = {}

def generate_short_url(length =6):
    chars = string.ascii_letters + string.digits
    short_url = "".join(random.choice(chars)for k in range(length))
    return short_url

@app.route("/", methods=["GET", "POST"])
def index():
    short_url = None
    if request.method == "POST":
        long_url = request.form['long_url']
        short_url = generate_short_url()
        while short_url in shortened_urls:
            short_url = generate_short_url()
        
        shortened_urls[short_url] = long_url
        short_url = request.url_root + short_url  

    return render_template("index.html", short_url=short_url)



@app.route("/<short_url>")
def redirect_url(short_url):
    long_url = shortened_urls.get(short_url)
    if long_url:
        return redirect(long_url)
    else:
        return "URL not found",404

if __name__ == "__main__":
    app.run(debug=True)
    



    
    
    
