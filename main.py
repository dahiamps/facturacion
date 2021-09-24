from flask import Flask, render_template, request, redirect
import controllerCliente
import controllerFactura

app = Flask(__name__)



@app.route('/insert_cliente')
def form_insert_material():
    return render_template('insertcliente.html')

@app.route('/insert_factura')
def form_insert_factura():
    return render_template('insertFactura.html')


@app.route('/save_client',methods=["POST"])
def save_client():
    ccnit = request.form["ccnit"]
    nombre = request.form["nombre"]
    telefono = request.form["telefono"]
    direccion = request.form["direccion"]
    estado = request.form["estado"]
    controllerCliente.insert_client(ccnit, nombre, telefono, direccion, estado)
    return redirect("/Clientes")

@app.route('/save_factura',methods=["POST"])
def save_factura():
    ccnit = request.form["ccnit"]
    fecha = request.form["fecha"]
    valor = request.form["valor"]
    saldo = request.form["saldo"]
    controllerFactura.insert_factura(ccnit, fecha, valor, saldo)
    return redirect("/Facturas")


@app.route("/")
@app.route("/Clientes")
def clientes():
    Clientes = controllerCliente.get_clientes()
    return render_template('clientes.html',Clientes=Clientes)

@app.route("/Facturas")
def facturas():
    Facturas = controllerFactura.get_factura()
    return render_template('factura.html',Facturas=Facturas)



@app.route("/delete_cliente",methods=["POST"])
def delete_cliente():
    controllerCliente.delete_clientes()
    return redirect("/Clientes")


@app.route("/delete_factura",methods=["POST"])
def delete_factura():
    controllerFactura.delete_factura(request.form["nrofact"])
    return redirect("/Facturas")
    
    

@app.route("/form_edit_cliente/<int:id>")
def form_edit_cliente(id):
    cliente = controllerCliente.get_cliente_id(id)
    return render_template("EditCliente.html",cliente=cliente)

@app.route("/form_edit_factura/<int:nrofact>")
def form_edit_factura(nrofact):
    factura = controllerFactura.get_factura_id(nrofact)
    return render_template("EditFactura.html",factura=factura)


@app.route("/update_cliente",methods=["POST"])
def update_cliente():
    id = request.form["id"]
    ccnit = request.form["ccnit"]
    nombre = request.form["nombre"]
    telefono = request.form["telefono"]
    direccion = request.form["direccion"]
    estado = request.form["estado"]
    controllerCliente.update_cliente(ccnit, nombre, telefono, direccion, estado, id)
    return redirect("/")


@app.route("/update_factura",methods=["POST"])
def update_factura():
    nrofact = request.form["nrofact"]
    fecha = request.form["fecha"]
    valor = request.form["valor"]
    saldo = request.form["saldo"]
    controllerFactura.update_factura(fecha, valor, saldo, nrofact)
    return redirect("/Facturas")



# Start server
if __name__ == "__main__":
    app.run(port=4200,debug=True)