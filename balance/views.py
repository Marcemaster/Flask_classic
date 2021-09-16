from balance import app
from flask import render_template
from balance.models import ListaMovimientos


@app.route ('/')
def index():
    lm = ListaMovimientos()
    lm.leer()

    return render_template("inicio.html", items=lm.movimientos)
