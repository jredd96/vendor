

class IdleState:
    def display_idle_message(self):
        print("Select Product")

    def display_inventory(self, vendor):
        for item, details in vendor.inventory.items():
            print(f"Item: {item}, Product Name: {details['name']}, Price: ${details['price']}, Quantity: {details['quantity']}")

class VendState:
    def purchase_processing(self, vendor, item, quantity):
        qty = int(quantity)
        print(f"Item selected: {item}")  # debug
        print(f"Quantity selected: {quantity}") # debug
        if item in vendor.inventory and vendor.inventory[item]["quantity"] >= qty:
            # Begin payment
            cost = vendor.inventory[item]["price"] * qty  # Calculate cost to customer
            payment_success = self.venmo_request(cost, item, qty)  # Send venmo request
            if payment_success:
                # Begin vending
                vend_successful = self.vend(qty)
                if vend_successful:
                    # Wrap up transaction
                    vendor.inventory[item]["quantity"] -= qty
                    print(f"You bought {quantity} {item}(s) for ${cost:.2f}.")
                    print(f"Thank you for supporting local business.")
                    return True
                else:
                    print("Vend unsuccessful. Processing refund.")
                    # will we refund the money? or have them contact us because that's not expected to happen much?
                    # send to maintenance state
            else:
                print("Payment not successful, please try again.")
                return False
        else:
            print("Sorry, the item is unavailable or insufficient quantity.")
            return False

    def venmo_request(self, cost, item, quantity):
        print(f"Sending Venmo payment request...")  # Venmo code goes here
        # activate camera
        # scan person's venmo tag
        # send request
        # if it goes through, evaluate payment_successful as True
        payment_successful = True  # Code goes here!  -- maybe for practice, take console input?
        return payment_successful

    def vend(self, qty):
        print("Vending...")
        return True
        # activate an LED here with RPi
        # eventually, implement actuator control here
