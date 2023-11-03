import os
import pickle

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class ProductList:
    def __init__(self):
        self.product_list = self.load_products()
        self.clear_screen()

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def save_products(self):
        with open('product_list.pkl', 'wb') as f:
            pickle.dump(self.product_list, f)

    def load_products(self):
        try:
            with open('product_list.pkl', 'rb') as f:
                return pickle.load(f)
        except FileNotFoundError:
            return []

    def add_product(self):
        self.clear_screen()
        self.show_product_list()
        new_name = input("Enter new product name: ")
        if not new_name:
            print("Product name cannot be empty.")
            return

        try:
            new_price = float(input("Enter new product price: "))
        except ValueError:
            print("Invalid price. Please enter a valid number.")
            return

        product = Product(new_name, new_price)
        self.product_list.append(product)
        self.save_products()
        print(f"{new_name} has been added to the product list.")

    def show_product_list(self):
        self.clear_screen()
        if not self.product_list:
            print("No products in the list.")
        else:
            self.product_list.sort(key=lambda p: p.name)
            print("{:<5} {:<15} {:<10}".format("Index", "Product Name", "Price"))
            for idx, product in enumerate(self.product_list, start=1):
                print("{:<5} {:<15} ${:<10.2f}".format(idx, product.name, product.price))

    def edit_product(self):
        self.show_product_list()
        try:
            edit_idx = int(input("Enter the number of the product you want to edit: ")) - 1
            if 0 <= edit_idx < len(self.product_list):
                product = self.product_list[edit_idx]
                print("What do you want to edit?")
                print("1. Name")
                print("2. Price")
                edit_choice = input("Enter your choice: ")
                if edit_choice == '1':
                    new_name = input("Enter new product name: ")
                    if not new_name:
                        print("Product name cannot be empty.")
                        return
                    product.name = new_name
                    self.save_products()
                    print("Product name has been updated.")
                elif edit_choice == '2':
                    try:
                        new_price = float(input("Enter new product price: "))
                        product.price = new_price
                        self.save_products()
                        print("Product price has been updated.")
                    except ValueError:
                        print("Invalid price. Please enter a valid number.")
                else:
                    print("Invalid choice. Please select either '1' for name or '2' for price.")
            else:
                print("Invalid index.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    def delete_product(self):
        self.clear_screen()        
        self.show_product_list()
        try:
            # Input a comma-separated list of indices to delete
            del_indices = input("Enter the numbers of the products you want to delete: ")
            del_indices = [int(idx) - 1 for idx in del_indices.split(",")]
            
            # Ensure that the indices are within valid range
            invalid_indices = [idx for idx in del_indices if idx < 0 or idx >= len(self.product_list)]
            
            if invalid_indices:
                print("Invalid indices:", invalid_indices)
                return

            # Sort and remove products by index
            del_products = [self.product_list[idx] for idx in sorted(del_indices, reverse=True)]
            for product in del_products:
                self.product_list.remove(product)
            
            self.save_products()
            
            print("Products deleted:")
            for product in del_products:
                print(f"{product.name} has been deleted.")
        except ValueError:
            print("Invalid input. Please enter valid numbers separated by commas.")

    def find_product(self):
        find_name = input("Enter product name: ")
        found = False
        for product in self.product_list:
            if product.name.lower() == find_name.lower():
                print(f"Income of {product.name}: ${product.price:.2f}")
                found = True
                break
        if not found:
            print("Product not found.")

    def calculate_total(self):
        total = sum(product.price for product in self.product_list)
        print(f"Total income from all products: ${total:.2f}")

    def run(self):
        while True:
            print("-" * 30)
            print("0. Exit the Program")
            print("1. Add New Product")
            print("2. Show Product List")
            print("3. Edit Product")
            print("4. Delete Product")
            print("5. Find Product")
            print("6. Calculate Total Income")
            print("-" * 30)
            choice = input("Select option: ")

            if choice == '0':
                self.clear_screen()
                print("Exiting the program.")
                break
            elif choice == '1':
                self.add_product()
            elif choice == '2':
                self.show_product_list()
            elif choice == '3':
                self.edit_product()
            elif choice == '4':
                self.delete_product()
            elif choice == '5':
                self.find_product()
            elif choice == '6':
                self.calculate_total()
            else:
                self.clear_screen()
                print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    product_manager = ProductList()
    product_manager.run()
