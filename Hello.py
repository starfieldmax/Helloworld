# print("Hello, World!")

#a = "Hello"
 # for loop demo
#for i in a:
    # print(i)


bags = int(input("Enter the total bags = "))
net_weight = int(input("Enter the net weigth = "))
price = int(input("Enter the price per bag = "))
soot = 1.5 * bags
print(soot)
net_final_weight = net_weight - soot
a = float(net_final_weight) / 75
print(a)
patti = float(a) * price
print(patti)



