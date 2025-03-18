from app import PyInxApp

app = PyInxApp()

@app.route("/home")
def home(request, response):
    response.text = "Hello from the Home Page"

@app.route("/about")
def about(request, response):
    response.text = "Hello from the About Page"