from flask import Flask,jsonify
from config import config
from flask_mysqldb import MySQL

app = Flask(__name__)
db = MySQL(app)


@app.route('/personas/<id_estado>', methods=['GET'])
def listar_personas(id_estado):
    try:
        cursor = db.connection.cursor()
        sql = "SELECT * FROM personas WHERE id_estados = '{0}'".format(id_estado)
        cursor.execute(sql)
        datos = cursor.fetchall()
        personas = []
        for fila in datos:
            persona = {'Id':fila[0],'Apellido':fila[1], 'Nombres':fila[2], 'DNI':fila[3], 'Domicilio' :fila [4], 'Telefono':fila[5], 'Id_Estado':fila[6], 'FecHora_Registros':fila[7], 'FecHora_Modificacion':fila[8]}
            personas.append(persona)
        return jsonify(personas)
    except Exception as ex:
        return jsonify({'mensaje': "Error"})


def pagina_no_encontrada(error):
    return "<h1>La página que estás buscando no existe</h1>"

if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(404, pagina_no_encontrada)
    app.run()