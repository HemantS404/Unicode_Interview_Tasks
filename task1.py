def b_dict(a, b):                                           #defining function taking 2 inputs
    dict = {}                                               #declaring empty dictonary 
    for i in range(a,b): 
        b_i = bin(i)                                        #bin() converts a number to binary
        if '11' in b_i:                                     #check consecutive 1s exsits in the binary notation of a number 
            dict[i] = True                                  #adding key-value pair in dictonary  
        else:                                               #key is the number and value either True of False
            dict[i] = False                                 
    return dict                                             

if __name__ == '__main__':
    a = int(input("Enter the First no. : "))
    b = int(input("Enter the Second no. : "))
    print(b_dict(a,b))