#how to represent binary numbers inpyhton
#you can use 0b follower by the binary number
#however it is still an integer
#by adding 0b python startsreading it as one one one insteaed of one hundred eleven
ownerPermission = 0b111 #0b means what ever number after the 0b is a binary number
print(ownerPermission)

filepermission = 0b111101001
#now the owner can read, write and execute
#group an read and execute
#others can execute only


mask = 0b000111000
print((filepermission & mask)>>3)
# 111101001  original
# 000111000  mask
#---------- &  bitwise operator (AND)
# 000101000
#>> 3   is the shifter to shift it to right 3 times ----> 000000101
#to extract the decimal number of the group permission

print(filepermission | mask)
print(bin(filepermission | mask))
# 111101001  original
# 000111000  mask
#---------- |  bitwise operator(OR)
# 111111001

message = 0b01001010 #my content is 'J'
key = 0b00101100 #encryption key is ','
encrypted_message = message ^ key
print(bin(encrypted_message))

decypted_message = encrypted_message^key
print(bin(decypted_message))
# 01001010  original
# 00101100  mask
#---------- ^  bitwise operator (XOR)
# 01100110
#XOR is used for encryption


#ones complement (1s complement)
givrnNumber = 5
#5 0101
#1s complement flip all the digit from 1 to 0 and 0 to 1
#->1010
#2s complement = 1s complement + 1
print(~givrnNumber)  #1s complement
print(~givrnNumber + 1)  #2s complement to get -5
print(-givrnNumber) #1s complement to get -5  unary -
print(+givrnNumber)  #unary +   to convert negative number to positive number

# 0, 1, 2, 3, 4, 5, 6, 7, 8, 9,  A, B,  C,  D,  E,   F, 10, 11, 12
# 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18

hexadecimal = 0XF
print(hexadecimal)
print(hex(hexadecimal))

# 0, 1, 2, 3, 4, 5, 6, 7, 10, 11, 12, 13, 14, 15, 16, 17, 20
# 0, 1, 2, 3, 4, 5, 6, 7,  8,  9, 10, 11, 12, 13, 14, 15, 16
octalnumber = 0o10
print(octalnumber)
print(oct(octalnumber))
