class Resturant:
    #class variable
    menu = {
        "Pizza" : 500,
        "Burger" : 600,
        "Pasta" : 400,
        "Salad" : 300
    }
    def __init__(self,customer_name):
        #object attributes
        self.customer_name = customer_name
        self.order = []
        self.order_summary = {}
        self.discount = 0
    #order process for customer
    def place_order(self,item,quantity):
        if item in Resturant.menu:
            price = Resturant.menu[item]*quantity
            order = (item,quantity,price)
            self.order.append(order)

            # Update dictionary
            self.order_summary[item] = self.order_summary.get(item, 0) + quantity
            print(f"{self.customer_name} ordered {quantity} x {item}")
        else:
            print(f"Sorry, {item} is not available in the menu.")

            # print(f"order placed:{order} with quantity:{quantity} by {self.customer_name}")
            # print("Order placed successfully")
     # Apply discount (percentage)
    def apply_discount(self, percent):
        self.discount = percent
        print(f"A discount of {percent}% has been applied for {self.customer_name}")

    # Calculate total bill
    def calculate_total(self):
        total_func = lambda order: order[2]  # Lambda function to get price
        total = sum(total_func(order) for order in self.order)  # Loop + sum
        if self.discount > 0:
            total = total - (total * self.discount / 100)  # Apply discount
        return total
    # Unique items ordered using set
    def unique_items_ordered(self):
        return set(item[0] for item in self.order)

    # Show full summary
    def show_summary(self):
        print("\n------ Order Summary for", self.customer_name, "------")
        print("Item-wise quantity (dictionary):", self.order_summary)
        print("Unique items ordered (set):", self.unique_items_ordered())
        print("Discount applied:", self.discount, "%")
        print("Total bill after discount:", self.calculate_total(), "INR")
        print("--------------------------------------\n")



    # def show_summary(self):
    #     print("Customer Name:",self.customer_name)
    #     print("Order Details:")
    #     total = 0
    #     for item, quantity, price in self.order:
    #         print(f"{item} - Quantity: {quantity} - Price: {price}")
    #         total += price
    #
    #         print("Total Amount:",total)


customer1 = Resturant("yojana")
customer2 = Resturant("Rahul")
customer1.place_order("Pizza",5)
customer1.place_order("Burger",6)
customer1.apply_discount(10)  # Apply 10% discount

customer2.place_order("Pasta", 2)
customer2.place_order("Pizza", 1)
customer1.apply_discount(5)  # Apply 5% discount

customer1.show_summary()
customer2.show_summary()


# create code for show_summary() - customer_name, item, qnty , price


