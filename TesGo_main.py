from pymongo import MongoClient

host = "localhost"
port = 27017
client = MongoClient(host, port)
mydb = client["library"]
shop_collection = mydb["Shopping"]

#functions------------------------------------------------------------------------------------

#Search for a single item in the database
def single_search():
	itemname = input("What do you want to search for?: ")
	myquery = { "name": itemname}

	doc = shop_collection.find_one(myquery)

	if doc is not None:
		print(doc)
	else:
		print("Item not found:", itemname )

#add an item to the database-----------------------------------------------	
def add_item():
	Item_name = input("What is the item name?: ")
	Item_type = input("What is the item type?: ")
	Item_price = input("what is the item price?: ")
	Item_stock = input("How many is there?: ")
	food = {"name": Item_name, "type": Item_type, "Price": Item_price, "stock": Item_stock}
	new_id = shop_collection.insert_one(food)
	print("Insrted food with id %s" % new_id.inserted_id)

#search for multiple items in the database
def multi_search():
	first_attribute = input("which item do you want to search for?: ")
	myquery = { "type" : first_attribute }
	all_food = shop_collection.find(myquery)

	for groceries in all_food:
		print(groceries)
	if all_food.retrieved == 0:
		print("second_attribute not found")
	else:
		print(" %s items found in groceries" % all_food.retrieved)

#update stock of a specific item in the database
def update_stock():
	change = input("What do you want to change?:  ")
	stock_type = input("Which stock are you updating?:  ")
	new_stock = input("What is the new  amount?: ")
	myquery = { change : stock_type}
	newvalues = { "$set": { change: new_stock }}

	result = shop_collection.update_many(myquery, newvalues)
	print( "%d documents matched, %d documents updated"
		%(result.matched_count, result.modified_count))

#delete stock of a specific item in the database
def delete_stock():
	deleted_food = input("What do you want to delete?:")
	results = shop_collection.delete_many({"type": "fruit"})
	print("\nDeleted food %d" %(results.deleted_count))

def staff_details():
	staff_first_name = input("Staff first name: ")
	staff_second_name = input("Staff second name: ")
	staff_role = input("Staff role: ")
	staff_salary = input("staff salary: ")
	staff = {"first name": staff_first_name, "second name": staff_second_name, "role": staff_role, "salary": staff_salary}
	new_id = shop_collection.insert_one(staff)
	print("Inserted staff with id %s" % new_id.inserted_id)

def staff_single_search():
	staffname = input("What do you want to search for?: ")
	myquery = { "staff_first_name": staffname}

	doc = shop_collection.find_one(myquery)

	if doc is not None:
		print(doc)
	else:
		print("Item not found:", sta )




#Program begins here -------------------------------------------------------------------------
print("	Welcome to TesGo")

while True: 
	print("""

	What would you like to do?

	1. Add item
	2. Multi Search
	3. Single Search
	4. Update Stock
	5. Delete Stock
	""")
#input options-----------------------------------------------------------------------------------
	option = int(input("Please enter an option: "))
	if option == 1:
		add_item()

	elif option == 2:
		multi_search()

	elif option == 3:
		single_search()

	elif option == 4:
		update_stock()

	elif option == 5:
		delete_stock()


	

