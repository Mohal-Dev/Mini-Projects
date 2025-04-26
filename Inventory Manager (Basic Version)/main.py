import csv
import os

print("Welcome to the Product Management System")

# Load existing products from CSV
def load_products_from_csv():
    Product = {}
    if os.path.exists('products.csv'):
        with open('products.csv', mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    price = float(row['Price'])
                    quantity = int(row['Quantity'])
                    Product[row['Product Name']] = {
                        'price': price,
                        'quantity': quantity
                    }
                except ValueError:
                    print(f"Error in reading product: {row}")
    return Product

# Save all products to CSV
def save_products_to_csv(Product):
    with open('products.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Product Name', 'Price', 'Quantity'])
        for name, values in Product.items():
            writer.writerow([name, values['price'], values['quantity']])

# Add new product
def add_product(Product):
    product_name = input("Enter product name: ").strip()
    if product_name in Product:
        print(" Product already exists")
    else:
        try:
            product_price = float(input("Enter product price: "))
            product_quantity = int(input("Enter product quantity: "))
            Product[product_name] = {"price": product_price, "quantity": product_quantity}
            print("Product added successfully")
            save_products_to_csv(Product)
        except ValueError:
            print("Invalid input. Price must be a number and quantity must be an integer.")
    return Product

# Show all products
def show_product_list(Product):
    if not Product:
        print(" No products available")
    else:
        print("\n Product List:")
        for name, values in Product.items():
            print(f"- {name}: Price = {values['price']}, Quantity = {values['quantity']}")

#  Search a product
def search_product(Product):
    name = input("Enter product name to search: ").strip()
    if name in Product:
        p = Product[name]
        print(f"{name}: Price = {p['price']}, Quantity = {p['quantity']}")
    else:
        print(" Product not found")

# Update a product
def update_product(Product):
    name = input("Enter product name to update: ").strip()
    if name in Product:
        try:
            new_price = float(input("Enter new price: "))
            new_quantity = int(input("Enter new quantity: "))
            Product[name] = {'price': new_price, 'quantity': new_quantity}
            print(" Product updated successfully")
            save_products_to_csv(Product)
        except ValueError:
            print(" Invalid input.")
    else:
        print(" Product not found")

# 🗑 Delete a product
def delete_product(Product):
    name = input("Enter product name to delete: ").strip()
    if name in Product:
        del Product[name]
        print("🗑 Product deleted successfully")
        save_products_to_csv(Product)
    else:
        print(" Product not found")

#  Exit program
def exit_program():
    print("\n\tThank you for using the Product Management System!")
    print("\n\tGoodbye!\n")
    exit()

#  Main loop
if __name__ == "__main__":
    Product = load_products_from_csv()
    while True:
        print("\n   ____Menu____:")
        print("1. Add Product")
        print("2. Show Product List")
        print("3. Search Product")
        print("4. Update Product")
        print("5. Delete Product")
        print("6. Exit")
        choice = input("Enter your choice : ").strip()

        if choice == '1':
            Product = add_product(Product)
        elif choice == '2':
            show_product_list(Product)
        elif choice == '3':
            search_product(Product)
        elif choice == '4':
            update_product(Product)
        elif choice == '5':
            delete_product(Product)
        elif choice == '6':
            exit_program()
        else:
            print(" Invalid choice, please try again")