from balance import app
from flask import render_template, request, redirect, url_for
from balance.models import ListaMovimientos


@app.route ('/')
def inicio():
    lm = ListaMovimientos()
    lm.leer()

    return render_template("inicio.html", items=lm.movimientos)

@app.route ('/nuevo', methods=['GET', 'POST'])
def nuevo():
    if request.method == 'GET':
        return render_template("nuevo_movimiento.html")
    else:
        datos = request.form

        # Validar datos 
        
        lm = ListaMovimientos()
        lm.leer()
        lm.añadir(datos)
        lm.escribir()
        return redirect(url_for('inicio'))
