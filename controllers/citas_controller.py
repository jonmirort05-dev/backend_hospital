from flask import jsonify
from db import get_connection


# GET TODAS LAS CITAS
def obtener_citas():

    conexion = get_connection()
    cursor = conexion.cursor(dictionary=True)

    query = """
    SELECT 
        c.id_cita,
        p.nombre AS paciente,
        c.fecha,
        CAST(c.hora AS CHAR) AS hora,
        c.estado
    FROM cita c
    INNER JOIN paciente p
        ON c.id_paciente = p.id_paciente
    """

    cursor.execute(query)

    citas = cursor.fetchall()

    cursor.close()
    conexion.close()

    return jsonify(citas)


# GET CITA POR ID
def obtener_cita(id):

    conexion = get_connection()
    cursor = conexion.cursor(dictionary=True)

    query = """
    SELECT 
        c.id_cita,
        p.nombre AS paciente,
        c.fecha,
        CAST(c.hora AS CHAR) AS hora,
        c.estado
    FROM cita c
    INNER JOIN paciente p
        ON c.id_paciente = p.id_paciente
    WHERE c.id_cita = %s
    """

    cursor.execute(query, (id,))

    cita = cursor.fetchone()

    cursor.close()
    conexion.close()

    if cita:
        return jsonify(cita)

    return jsonify({
        "error": "Cita no encontrada"
    }), 404


# POST CREAR CITA
def crear_cita(data):

    conexion = get_connection()
    cursor = conexion.cursor()

    query = """
    INSERT INTO cita
    (id_paciente, id_medico, fecha, hora, motivo)
    VALUES (%s, %s, %s, %s, %s)
    """

    valores = (
        data["id_paciente"],
        data["id_medico"],
        data["fecha"],
        data["hora"],
        data["motivo"]
    )

    cursor.execute(query, valores)

    conexion.commit()

    nueva_cita = cursor.lastrowid

    cursor.close()
    conexion.close()

    return jsonify({
        "mensaje": "Cita creada",
        "id_cita": nueva_cita
    }), 201

    # PUT ACTUALIZAR CITA
def actualizar_cita(id, data):

    conexion = get_connection()
    cursor = conexion.cursor()

    query = """
    UPDATE cita
    SET
        id_paciente = %s,
        id_medico = %s,
        fecha = %s,
        hora = %s,
        motivo = %s,
        estado = %s
    WHERE id_cita = %s
    """

    valores = (
        data["id_paciente"],
        data["id_medico"],
        data["fecha"],
        data["hora"],
        data["motivo"],
        data["estado"],
        id
    )

    cursor.execute(query, valores)

    conexion.commit()

    filas_afectadas = cursor.rowcount

    cursor.close()
    conexion.close()

    if filas_afectadas == 0:
        return jsonify({
            "error": "Cita no encontrada"
        }), 404

    return jsonify({
        "mensaje": "Cita actualizada"
    })

# DELETE ELIMINAR CITA
def eliminar_cita(id):

    conexion = get_connection()
    cursor = conexion.cursor()

    query = "DELETE FROM cita WHERE id_cita = %s"

    cursor.execute(query, (id,))

    conexion.commit()

    filas_afectadas = cursor.rowcount

    cursor.close()
    conexion.close()

    if filas_afectadas == 0:
        return jsonify({
            "error": "Cita no encontrada"
        }), 404

    return jsonify({
        "mensaje": "Cita eliminada"
    })