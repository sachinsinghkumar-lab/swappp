#xor for sign detdtion

input("XOR sign detection = n ^ m > 0 means diff signs. press enter")
print("  4 ^ 2=",  4^2,  "  same signs r positive")
print("  4 ^ -2=",  4^-2,  "  diff signs r negative")

n = int(input("entr a number tryu5 or -3): "))
guess = input("will " + str(n) + "  ^  -8 bbe positive or negative?")
input("XOR is negative when signs differ. press enter")
print("  ", n ,"  ^-8 = ", n ^ -8, "  ur guess:", guess)


