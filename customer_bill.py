Customer_name=input("Enter a customer name :")
Product1_name=input (" Enter a product 1 name : ") 
Product1_price=float(input(" Enter a product 1 price :"))
Product2_name=input (" Enter a product 2 name : ")           
Product2_price=float(input (" Enter a product 2 price : ")) 
Product3_name=input (" Enter a product 3 name : ") 
Product3_price=float (input (" Enter a product 3 price : ")) 
total_price = Product1_price + Product2_price + Product3_price
  
First_character=Customer_name[0]
Last_character=Customer_name [-1]
                 
Product1_name = Product1_name.upper()
Product2_name = Product2_name.upper()
Product3_name = Product3_name.upper()
                                                                        
print(f"\n\t _______CUSTOMER BILL______")
print (f"\t Customer name : {Customer_name}")                                                                      
print (f"\t First character : {First_character}") 
print (f"\t Last character : {Last_character}")                                                                         
print(f"\t Product1 :  {Product1_name} - ₹{Product1_price}")
print(f"\t Product2:  {Product2_name} - ₹{Product2_price}") 
print(f"\t Product3 :  {Product3_name} - ₹{Product3_price}") 
print(f"\t Total price : ₹{total_price}  ")                                                             
 
                                                                         
 
  
 
                                                                        
                                                                       
