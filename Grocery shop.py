grocery_list =["banana","cherry","apple"]
prices={
"banana":15,
"cherry":30,
"apple":20

}
quantity={
"banana":40,
"cherry":70,
"apple":30
}
while True:
	print("Welcome ITI Grocery shop")
	ch = int(input("0.to exit press 0\n1.Mode For customer press 1\n2.for owner press 2\nEnter your choice : "))
	if ch == 1:	
		print ("Welcome to ITI Customer ")
		c_input = int(input("1.To show our products press 1\n2.To Buy from our products press 2\n3.to print the bill press 3\nEnter your choice : "))
		if c_input == 1:
			print("ITI Grocery list is ")
			print(grocery_list)
			print("ITI Grocery prices list is ")
			print(prices.items())
			print("ITI Grocery quantity list is ")
			print(quantity.items())
		elif c_input==2:
			print ("Buy from our products ")
			print("enter quantity  that you need")
			q_b=int(input("enter quantity of banana"))
			q_c=int(input("enter quantity of cherry"))
			q_a=int(input("enter quantity of apple"))
			quantity["banana"] = 40-q_b
			quantity["cherry"] = 70-q_c
			quantity["apple"] =  30-q_a
			total_b=prices["banana"] = 15*q_b
			total_c=prices["cherry"] = 30*q_c
			total_a=prices["apple"] =  20*q_a
			total=total_a+total_b+total_c
		elif c_input==3:
			print("#############Bill#########")
			print("Item    Quantity    Total")
			print(grocery_list[0] , quantity["banana"]  ,prices["banana"]  )
			print(grocery_list[1] , quantity["cherry"] , prices["cherry"]  )
			print(grocery_list[2] , quantity["apple"]  , prices["apple"]  )
			print("Total")
			print(total)
			print("***********Thank You********")
			print("Hope to see you back soon!")
		else:
			print("\nERROR: Choose only digits from the given option")
	if ch == 2:
		print ("Welcome to ITI OWNER ")
		o_input = int(input("1.To Add new products press 1\n2.To Show Products press 2\n3.To Add Cost press 3\n4.To Change cost press 4\t"))
		if o_input==1:
			print("{'new product',quantity}")
			product_name = input("write product ")
			product_quantity=int(input("product quantity"))
			#quantity1={'product_name',"product_quantity"}
			quantity.update({product_name:product_quantity})
			#quantity.update(quantity1)
		elif o_input==2:
			print("ITI Grocery list is ")
			print(grocery_list)
			print("ITI Grocery prices list is ")
			print(prices.items())
			print("ITI Grocery quantity list is ")
			print(quantity.items())
		elif o_input == 3:
			print("{'new product',price}")
			product_name_= input("write product ")
			product_price=int(input("product price "))
			prices.update({product_name_:product_price})
		elif o_input == 4:
			product_name_1= input("write product ")
			product_price1=int(input("product price "))
			prices[product_name_1]=product_price1
			print("ITI Grocery prices list is ")
			print(prices.items())
	elif ch == 0:
		break
	else:
		print("\nERROR: Choose only digits from the given option")