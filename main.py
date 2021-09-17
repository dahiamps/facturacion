from flask import Flask, render_template, request, redirect
import controllerCliente

app = Flask(__name__)


@app.route("/")
@app.route("/Clientes")
def clientes():
    Clientes = controllerCliente.get_clientes()
    return render_template('clientes.html',Clientes=Clientes)



# Start server
if __name__ == "__main__":
    app.run(port=4200,debug=True)