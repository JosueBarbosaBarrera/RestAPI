from flask import Flask, jsonify, request
app = Flask(__name__)

from products import products

# RESTAPI, send data in json format

@app.route("/ping")
def ping():
    return jsonify({"message": "testing"})

#Methods most popular on HTTP: POST(guardar) - PUT(actualizar) - DELETE(eliminar)

@app.route("/products", methods={"GET"})
def getProducts():
    return jsonify({"products": products, "message": "Product's list"})

@app.route("/products/<string:product_name>")
def getproduct(product_name):
    productsFound = [products for product in products if product["name"] == product_name]
    if(len(productsFound) > 0):
        return jsonify({"product": productsFound[0]})
    return jsonify({"message": "product not found"})

# We can use POSTMAN or INSOMNIA (is better and simple) to send data to our RESAPI

@app.route("/products", methods=["POST"])
def addProduct():
    new_product = {
        "name": request.json["name"],
        "price": request.json["price"],
        "quantity": request.json["quantity"]
    }
    products.append(new_product)
    return jsonify({"message": "Product Added Succesfully", "products": products})

@app.route("/products/<string:product_name>", methods=["PUT"])
def editProduct(product_name):
    productFound = [product for product in products if  product["name"] == product_name]
    if(len(productFound) > 0):
        productFound[0]["name"] = request.json["name"]
        productFound[0]["price"] = request.json["price"]
        productFound[0]["quantity"] = request.json["quantity"]
        return jsonify({
            "message": "Product Updated",
            "product": productFound[0]
        })
    return jsonify({"message": "Product not found"})

@app.route("/products/<string:product_name>", methods=["DELETE"])
def delProduct(product_name):
    productFound = [product for product in products if product["name"] == product_name]
    if(len(product_name) > 0):
        products.remove(productFound[0])
        return jsonify({
            "message": "Product deleted",
            "products": products
        })
    return jsonify({"mesaage": "Product not found"})

if __name__ == "__main__":
    app.run(debug=True)