class InventorySystem:
    def __init__(self):
        self.inventory = {}
    
    
    def add_product(self, product_id: str, name: str, quantity: int, price: float):
        if quantity < 0 or price < 0:
            raise Exception('Quantity or price cannot be negative.')

        self.inventory[product_id] = {
            "product id": product_id,
            "name": name,
            "quantity": quantity,
            "price": price
        }
        
    def remove_product(self, product_id: str):
        if product_id in self.inventory:
            del self.inventory[product_id]
            return True
        else:
            return False
    
    def get_inventory_value(self):
        value = 0
        for item in self.inventory[product_id].values():
            value += item["quantity"] * item["price"]
        return value

    def search_products(self, keyword: str):
        keyword = keyword.lower()
        keyword_results = []
        for item in self.inventory[product_id].values():
            if keyword in item["name"].lower():
                keyword_results.append(item)
        return keyword_results







