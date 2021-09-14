from balance import app


@app.route('/')
def index():
    return "flask funcionando"
