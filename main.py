from states import IdleState
from transitions import StateTransition

class VendingMachine:
    """
    This is a description
    """

    def __init__(self):
        self.state = IdleState()
        self.inventory = {  # Inventory is dictionary, products are keys
            "9 oz": {"price": 10.00, "quantity": 10, "name": "Creamed Honey 9 oz"},
            "15 oz": {"price": 15.00, "quantity": 0, "name": "Creamed Honey 15 oz"}
            # Not currently supporting more than one item
        }  # import a config file later (item, price, qty)
        self.transition = StateTransition()

    def display_inventory(self):
        self.state.display_inventory(self)
    def purchase_item(self, item, quantity):
        self.state = self.transition.to_processing_purchase(self, item, quantity)

    def complete_purchase(self):
        self.state = self.transition.to_idle()


vendor = VendingMachine()
vendor.display_inventory()
print(vendor.state)

while True:
    selection = input("Make a selection: ")
    qty = input("Select a quantity: ")
    vendor.purchase_item(selection, qty)
