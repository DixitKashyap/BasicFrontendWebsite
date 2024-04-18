from flask import Flask,render_template
import requests

app = Flask(__name__)


def getData():
    response = requests.get("https://api.npoint.io/674f5423f73deab1e9a7")
    data = response.json()
    return data

def getIdSpecificData(id):
    data = getData()
    for item in data:
        if item['id'] == id:
            return item
@app.route('/')
def home_route():
    data = getData()
    return render_template("index.html",data = data)


@app.route("/about")
def about_route():
    return render_template("about.html")

@app.route("/post/<int:id>")
def sample_route(id):
        response = requests.get("https://api.npoint.io/674f5423f73deab1e9a7")
        data = response.json()
        if(id == 0):
           return render_template('post.html',title ="Sample Post",subtitle="A Place where you can find blog content",body="")
        else :
            for item in data:
                if item['id']==id:
                    return render_template("post.html",title=item["title"],body=item["body"],subtitle=item['subtitle'])          

@app.route("/contact")
def contact_route():
    return render_template("contact.html")

if __name__ == '__main__':
    app.run(debug=True)

