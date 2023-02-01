# pow(10, 3) pow(10, 2) pow(10, 1) pow(10, 0)

x = 127
print(1 * pow(10, 2) + 2 * pow(10, 1) + 7 * pow(10, 0))

y = 1035
print(1 * pow(10, 3) + 0 * pow(10, 2) + 3 * pow(10, 1) + 5 * pow(10, 0))

# pow(2, 3) pow(2, 2) pow(2, 1) pow(2, 0)

x = 0b101
print(x)
print(1 * pow(2, 2) + 0 * pow(2, 1) + 1 * pow(2, 0))

y = 0b0110
print(y)
print(0 * pow(2, 3) + 1 * pow(2, 2) + 1 * pow(2, 1) + 0 * pow(2, 0))

z = 0xffff
print(z)
print(format(z, '0>42b'))
print(15 * pow(16, 3) + 15 * pow(16, 2) + 15 * pow(16, 1) + 15 * pow(16, 0))
print(0b000000000000000000000000001111111111111111)
 