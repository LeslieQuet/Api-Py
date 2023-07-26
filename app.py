from flask import Flask, request, jsonify
from categories.modelCategory import db, Categories
import os
from logging import exception
from categories.get_categories_controller import getCategoriesController
from categories.edit_category_controller import editCategoryController
from categories.create_category_controller import createCategoryController
from categories.delete_category_controller import deleteCategoryController

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{os.path.join(os.path.dirname(__file__), 'database', 'northwind.db')}"
app.config["SQLALCHEMY_TRACK_MOFICATIONS"] = False
db.init_app(app)

##Rutas
@app.route("/")
def home():
    return "<h2>Esta es una API que hace uso del framework Flask para Consultar, Crear, Editar y Eliminar una 'Categoría' de la BD. <h2>Los endpoints que utiliza son GET /api/categories (recibe query name), GET /api/category/:categoryId, POST /api/createCategory, PUT /api/editCategory y DELETE /api/deleteCategory"

    texto_actualizado = texto.replace("Los endpoints", "\nLos endpoints")

    print(texto_actualizado)

##Ruta get all categories & get por coincidencia en el nombre por query "name"
@app.route("/api/categories", methods=["GET"])
def getCategories():
    try:
        categoryName = request.args.get("name")
        
        if categoryName is not None:
            response = getCategoriesController(categoryName)
        else:
            response = getCategoriesController()
        return response, 200

    except Exception as e: 
        print("[SERVER]: Error:", e) 
        return jsonify({"msg": "Ha ocurrido un error"}), 500

##Ruta getCatagoryById     
@app.route("/api/category/<int:category_id>", methods=["GET"])
def getCategoryById(category_id):
    try:

        category = Categories.query.get(category_id)
        if not category:
            return jsonify({"msg": "Categoría no encontrada"}), 404

        return jsonify(category.serialize()), 200

    except Exception as e:
        print("[SERVER]: Error:", str(e))
        return jsonify({"msg": "Ha ocurrido un error"}), 500

##Ruta crea categorías (recibe por body las propiedades CategoryName, Description y Picture)
@app.route("/api/createcategory", methods=["POST"])
def createCategory():
    try:
        category_data = request.get_json()
        response, status_code = createCategoryController(category_data)
        return jsonify(response), status_code

    except Exception as e:
        print("[SERVER]: Error:", str(e))
        return jsonify({"msg": "Ha ocurrido un error"}), 500

##Ruta modfica categorías (recibe por body categoryId para identificar a la categoría y se agregan las propiedades con los valores a modificar)
@app.route("/api/editcategory", methods=["PUT"])
def editCategoryById():
    try:
        category_data = request.get_json()
        response, status_code = editCategoryController(category_data)
        return jsonify(response), status_code

    except Exception as e:
        print("[SERVER]: Error:", str(e))
        return jsonify({"msg": "Ha ocurrido un error"}), 500

##Ruta elimina categorías
@app.route("/api/deletecategory/<int:category_id>", methods=["DELETE"])
def deleteCategoryById(category_id):
    try:
        response, status_code = deleteCategoryController(category_id)
        return response, status_code

        # return response, 200

    except Exception as e:
        print("[SERVER]: Error:", str(e))
        return jsonify({"msg": "Ha ocurrido un error"}), 500

if __name__ == "__main__":
    app.run(debug=True, port=4000)
