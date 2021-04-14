class Product:
    def __init__(self, title=None, code=None, quantity=None, keywords=None, short_description=None,
                 long_description=None, head_title=None,meta_description=None, purchase_price=None):
        self.title = title
        self.code = code
        self.quantity = quantity
        self.keywords = keywords
        self.short_description = short_description
        self.long_description = long_description
        self.head_title = head_title
        self.meta_description = meta_description
        self.purchase_price = purchase_price
