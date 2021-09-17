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



# Start server
if __name__ == "__main__":
    app.run(port=4200,debug=True)