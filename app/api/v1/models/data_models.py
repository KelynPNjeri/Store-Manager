from flask import jsonify, make_response
from flask_restful import abort
import datetime as dt

product_list = []
sales_list = []

# This is a model for products and sales that specifies how its payload is structured.


class ProductOps:
    def __init__(self):
        self.products = product_list

    def save_product(self, name, price, category, quantity):
        payload = {
            "Id": len(self.products)+1,
            "Product Name": name,
            "Product Price": price,
            "Product Category": category,
            "Quantity in Inventory": quantity
        }
        self.products.append(payload)
        return self.products

    def retrieve_all_items(self):
        return self.products

    def show_one(self, product_id):
        for product_item in self.products:
            if product_item["Id"] == product_id:
                return product_item
        return abort(404, message="Product {} does not exist in inventory".format(product_id))


class SalesOps():
    def __init__(self):
        self.sales = sales_list

    def save_sales_record(self, sales_by, quantity_sold, unit_price):

        payload = {
            "Id": len(self.sales)+1,
            "Sold By": sales_by,
            "Quantity Sold": quantity_sold,
            "Date Created": dt.datetime.now(),
            "Price per unit": unit_price,
            "Total": quantity_sold * unit_price
        }
        self.sales.append(payload)
        return self.sales

    def retrieve_all_items(self):
        return self.sales

    def show_one(self, sale_id):
        for sale_records in self.sales:
            if sale_records["Id"] == sale_id:
                return sale_records
        return abort(404)
