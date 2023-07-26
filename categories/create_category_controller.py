from flask import Flask, request, jsonify
from categories.modelCategory import db, Categories

def createCategoryController(category_data):
    category_name = category_data.get("CategoryName")
    description = category_data.get("Description")
    picture = category_data.get("Picture")

    if not category_name or not description:
        return {"msg": "Nombre y descripción son campos requeridos"}, 400

    ##Verifica si la categoría ya existe
    existing_category = Categories.query.filter_by(CategoryName=category_name).first()
    if existing_category:
        return {"msg": "El nombre de categoría ya está en uso"}, 409

    # Decodifica la imagen desde base64 si se envía
    Picture = None
    if Picture:
        try:
            Picture = base64.b64decode(Picture)
        except Exception as e:
            return {"msg": "Error al decodificar la imagen"}, 400

    ##Se crea una nueva instancia de la categoría
    new_category = Categories(CategoryName=category_name, Description=description, Picture=Picture)

    try:
        db.session.add(new_category)
        db.session.commit()
        return {"msg": "Categoría creada correctamente", "CategoryId": new_category.CategoryId}, 201
    except Exception as e:
        db.session.rollback()
        return {"msg": "Error al crear la categoría"}, 500