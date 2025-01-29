def net_price(list_price,discount=0,tax=0.05):   #can be set when the values reamain constant for all inputs
    return list_price*(1-discount)*(1+tax)

#print(net_price(500,0,0.05))   can be used like this

#Next way
print(net_price(500))