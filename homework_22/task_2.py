def find_max_object(passed_objects):
    max_object = max(passed_objects, key=passed_objects.get)
    objects_list = []
    objects_list.append(max_object)
    for object in passed_objects:
        if object != max_object and passed_objects[object] == passed_objects[max_object]:
            objects_list.append(object)
    
    return objects_list[0] if len(objects_list) == 1 else objects_list

def handle_data(data_file_path):
    products_amounts = []   
    products_prices = []
    most_sold_products = {}
    persons_that_spent_most = {}
    persons_with_most_products = {}
    with open(data_file_path, "r") as data:
        for each_product in data:
            person, product, amount, price = each_product.strip().split(",")
            products_amounts.append(int(amount))
            products_prices.append(float(price))
            
            persons_with_most_products[person] = int(amount)
            persons_that_spent_most[person] = int(amount) * float(price)
            most_sold_products[product] = int(amount)
    
    person_that_spent_most = find_max_object(persons_that_spent_most)
    product_sold_mostly = find_max_object(most_sold_products)
    person_with_max_product_amount = find_max_object(persons_with_most_products)
    average_amount_of_products = sum(products_amounts) / len(products_amounts)
    average_price_of_products = sum(products_prices) / len(products_prices) 
    
    return (
        person_with_max_product_amount, # a
        person_that_spent_most, # b
        average_price_of_products, # c
        average_amount_of_products, # d
        product_sold_mostly # e
    )
    
def print_results(a, b, c, d, e):
    print("Person/Persons with the maximum amounts of products bought: ", a)
    print("Person/Persons, which have spent the most on products: ", b)
    print("The average price of a given products: ", c)
    print("The average amount of a given products: ", d)
    print("Product/Products, which have been sold mostly: ", e)
    
def main():
    data_file_path = "homework_22/Assets/data.txt"

    a, b, c, d, e = handle_data(data_file_path=data_file_path)
    print_results(a, b, c, d, e)
    
    
if __name__ == "__main__":
    main()
