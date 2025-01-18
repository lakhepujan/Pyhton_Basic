#format specifiers : formats the data based on flag inserted
#syntax:{value:flag}
# types:    
#.(number)f=round to that many decimal places
# :(number)=allocate spaces    
#:03=allocate and zero pad that many spaces
#:<=align left 
#:>=align right   
#:^=align center  
#:+=display plus sign before the value    
#:= =place sign to leftmost position
#:=insert a space before positive numbers     
#:,=thousand separator


price1=3000.14367
price2=-2200.034
price3=3010.67

print(f"Price1 Rs={price1:+,.2f}")
print(f"Price2 Rs={price2:+,.2f}")
print(f"Price3 Rs={price3:+,.2f}")