from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Product(BaseModel):
    id: int
    name: str
    price: float

products = []
@app.get("/")
def home():
    return {"Message":"FastAPI is running"}

@app.get("/products/{product_id}")
def get_products(product_id: int):
    for product in products:
        if product.id == product_id:
            return product
    raise HTTPException(status_code=404, detail="Product not found")

@app.post("/products")
def add_product(product: Product):
    products.append(product)
    return {
        "message": "Product added",
        "products": product
    }

@app.put("/products/{product_id}")
def update_product(product_id: int, updated_product: Product):
    for index, product in enumerate(products):
        if product.id == product_id:
            products[index] = updated_product
            return updated_product
    raise HTTPException(status_code=404, detail="Product not found")

@app.delete("/products/{product_id}")
def delete_product(product_id: int):
    for index, product in enumerate(products):
        if product.id == product_id:
            deleted=products.pop(index)
            return {
                "message": "Product deleted",
                "products": deleted

            }
    raise HTTPException(status_code=404, detail="Product not found")