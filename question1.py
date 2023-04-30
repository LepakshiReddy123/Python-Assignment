 /* Q1 :Description: create a small command-line program in python to calculate the total invoice amount for below purchases-
    Book-introduction to Python Programming:Rs 499.0
    Book-Python libraries cookbook:Rs 855.00
    Book-DataScience in python:Rs 645.00
    
    Taxes and Additional charges are described as details-
    GST:12%
    Delivary Charges:Rs 250.00 */
	
---------Code----------------------	
	
book1=int(input("Enter count of books required (Introduction to python programming) : "))
book2=int(input("Enter count of books required (Python Libraries Cookbooks) : "))
book3=int(input("Enter count of books required (Data Science in Python) : "))
amount=(float)(book1*499.00+book2*855.00+book3*645.00)
gst =(float)(amount+(amount*(12/100)))
total_amount=(float)(gst+250.00)
print("Total invoice amount is : ",total_amount)





------------OUTPUT------------------

Enter count of books required (Introduction to python programming) : 2
Enter count of books required (Python Libraries Cookbooks) : 3
Enter count of books required (Data Science in Python) : 4
Total invoice amount is :  7130.16