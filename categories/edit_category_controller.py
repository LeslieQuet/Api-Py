from flask import Flask, request, jsonify
from categories.modelCategory import db, Categories

def editCategoryController(category_data):

    categoryId = category_data.get('categoryId')
    category = Categories.query.get(categoryId)

    if not category:
        return {"msg": "Categoría no encontrada"}, 404

    if category_data.get("Picture"):
        try:
            Picture = base64.b64decode(Picture)
        except Exception as e:
            return {"msg": "Error al decodificar la imagen"}, 400

    for key, value in category_data.items():
        setattr(category, key, value)

    try:
        db.session.commit()
        return {"msg": "Categoría actualizada correctamente"}, 200
    except Exception as e:
        db.session.rollback()
        return {"msg": "Error al actualizar la categoría"}, 500