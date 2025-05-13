from flask import Blueprint, request, jsonify
from app.models import db, Receta

# Blueprint solo con endpoints de prueba para cursos
main = Blueprint('main', __name__)

@main.route('/') # Ambas rutas llevan al mismo lugar
@main.route('/dashboard')
def index():
    return '<h1>Corriendo en Modo de Prueba.</h1>'

@main.route('/recetas', methods=['GET'])
def listar_cursos():
    recetas = Receta.query.all()

    data = [
        {
            'id': receta.id,
            'nombre': receta.nombre,
            'ingredientes': receta.ingredientes,
            'instrucciones': receta.instrucciones,
            'tiempo_preparacion': receta.tiempo_preparacion,
            'porciones': receta.porciones,
            'imagen_url': receta.imagen_url,
            'categoria': receta.categoria,
            'usuario_id': receta.usuario_id
        }
        for receta in recetas
    ]
    return jsonify(data), 200


@main.route('/recetas/<int:id>', methods=['GET'])
def listar_una_receta(id):
    receta = Receta.query.get_or_404(id)

    data = {
        'id': receta.id,
        'nombre': receta.nombre,
        'ingredientes': receta.ingredientes,
        'instrucciones': receta.instrucciones,
        'tiempo_preparacion': receta.tiempo_preparacion,
        'porciones': receta.porciones,
        'imagen_url': receta.imagen_url,
        'categoria': receta.categoria,
        'usuario_id': receta.usuario_id
    }

    return jsonify(data), 200


@main.route('/recetas', methods=['POST'])
def crear_receta():
    data = request.get_json()

    if not data:
        return jsonify({'error': 'No input data provided'}), 400

    receta = Receta(
        nombre=data.get('nombre'),
        ingredientes=data.get('ingredientes'),
        instrucciones=data.get('instrucciones'),
        tiempo_preparacion=data.get('tiempo_preparacion'),
        porciones=data.get('porciones'),
        imagen_url=data.get('imagen_url'),
        categoria=data.get('categoria'),
        usuario_id=data.get('usuario_id')  # sin validación de usuario
    )

    db.session.add(receta)
    db.session.commit()

    return jsonify({'message': 'Receta creada', 'id': receta.id, 'usuario_id': receta.usuario_id}), 201

@main.route('/recetas/<int:id>', methods=['PUT'])
def actualizar_receta(id):
    receta = Receta.query.get_or_404(id)
    data = request.get_json()

    receta.nombre = data.get('nombre', receta.nombre)
    receta.ingredientes = data.get('ingredientes', receta.ingredientes)
    receta.instrucciones = data.get('instrucciones', receta.instrucciones)
    receta.tiempo_preparacion = data.get('tiempo_preparacion', receta.tiempo_preparacion)
    receta.porciones = data.get('porciones', receta.porciones)
    receta.imagen_url = data.get('imagen_url', receta.imagen_url)
    receta.categoria = data.get('categoria', receta.categoria)
    receta.usuario_id = data.get('usuario_id', receta.usuario_id)

    db.session.commit()

    return jsonify({'message': 'Receta actualizada', 'id': receta.id}), 200

@main.route('/recetas/<int:id>', methods=['DELETE'])
def eliminar_receta(id):
    receta = Receta.query.get_or_404(id)
    db.session.delete(receta)
    db.session.commit()

    return jsonify({'message': 'Receta eliminada', 'id': receta.id}), 200
