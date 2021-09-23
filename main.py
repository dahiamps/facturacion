from flask import Flask, render_template, request, redirect
import controllerCliente

app = Flask(__name__)



@app.route('/insert_cliente')
def form_insert_material():
    return render_template('insertcliente.html')

@app.route('/save_client',methods=["POST"])
def save_client():
    ccnit = request.form["ccnit"]
    nombre = request.form["nombre"]
    telefono = request.form["telefono"]
    direccion = request.form["direccion"]
    estado = request.form["estado"]
    controllerCliente.insert_client(ccnit, nombre, telefono, direccion, estado)
    return redirect("/Clientes")


@app.route("/")
@app.route("/Clientes")
def clientes():
    Clientes = controllerCliente.get_clientes()
    return render_template('clientes.html',Clientes=Clientes)


@app.route("/delete_cliente",methods=["POST"])
def delete_cliente():
    controllerCliente.delete_clientes()
    return redirect("/Clientes")
    

@app.route("/form_edit_cliente/<int:id>")
def form_edit_cliente(id):
    cliente = controllerCliente.get_cliente_id(id)
    return render_template("EditCliente.html",cliente=cliente)

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



# Start server
if __name__ == "__main__":
    app.run(port=4200,debug=True)