from balance import app
from flask import render_template, request, redirect, url_for
from balance.models import ListaMovimientos, Movimiento


@app.route ('/')
def inicio():
    lm = ListaMovimientos()
    lm.leer()
    return render_template("inicio.html", items=lm.movimientos)

@app.route ('/nuevo', methods=['GET', 'POST'])
def nuevo():
    if request.method == 'GET':
        return render_template("nuevo_movimiento.html", errores=[], form={"fecha":"","concepto":"","cantidad":""})
    else:
        datos = request.form
        try:
            movimiento = Movimiento(datos)
        except ValidationError as msg:
            return render_template("nuevo_movimiento.html", errores=movimiento.errores, form=datos)



        lm = ListaMovimientos()
        lm.leer()
        lm.añadir(datos)
        lm.escribir()
        return redirect(url_for('inicio'))
