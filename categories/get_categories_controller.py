from flask import Flask
from categories.modelCategory import Categories
from flask import jsonify

def getCategoriesController(categoryName=None):
    if categoryName is not None:
        categories = Categories.query.filter(Categories.CategoryName.like(f"%{categoryName}%")).all()
        
        if not categories:
            return jsonify({"msg": "No hay categorias con ese nombre"})
        
        categories_list = [category.serialize() for category in categories]
        return jsonify(categories_list)
    else:
        categories = Categories.query.all() 
        categories_list = [category.serialize() for category in categories]
        return jsonify(categories_list)