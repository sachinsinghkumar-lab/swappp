#swapping BUT without a third variable


input("xor swap -  exchange two values without a third variable. press enter:")
print("before : a= 5, b = 9")
a, b = 5 , 9
a^= b ; b ^= a ; a^= b
print("after : a= ", a, " b = ", b)

n = int(input("enter a number (try 3 or 7 or 9:)   "))
guess = input("after xor swap of " + str(n) + " with 5, what is the new value of n?  ")
a, b = n, 8 
a^= b ; b ^= a ; a^= b
input("XOR swap exchanges the valuies. press enter")
print(" n became:", a, "  ur guess:", guess,)
