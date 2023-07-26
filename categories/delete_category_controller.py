from flask import Flask, request, jsonify
from categories.modelCategory import db, Categories

def deleteCategoryController(category_id):
    ##Se identifica la categoría a eliminar
    category = Categories.query.get(category_id)
    if not category:
        return jsonify({"msg": "Categoría no encontrada"}), 404

    ##Elimina la categoría de la bse de datos
    db.session.delete(category)  
    db.session.commit()
    return jsonify({"msg": "Categoría borrada exitosamente"}), 200

    