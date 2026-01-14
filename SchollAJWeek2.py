#prints a decimal system number in binary and hex
x=31
print(x, bin(x), hex(x))
#when x = 1.825 I get a float error, because there is a decimal in the number
#changes x to equal 18
x=18
#makes variables equal to a binary or hex number
y=0b1011
z=0xA3
#prints binary and hex variables in decimal
print(y,z)
#adds all my variables together as 1 variable
w=x+y+z
#tells me the sum off my variables
print('the sum is ' , w)
#variables to test compression
o_size = 240
d_size = 25
c_t_size = 148
#calculates percentage of compression
compression = (1 - ((c_t_size + d_size) / o_size))*100
#round the percentage to 3 decimal places
compression=round(compression, 3)
#prints variables and there names
print('  Compressed text size; ' + str(c_t_size))
print('       Dictionary size; ' + str(d_size))
print('         Original size; ' + str(o_size))
print('Percent of compression; ' + str(compression)+'%')
#asks user for an input within a range
num=int(input('Enter a number between -128 and 127: '))
#defines the number of bits
num_bits=8
#tells you your input is invalid
if num<-128 or num>127:
    print('invalid number')
elif num>-1:
    #prints positive binary
    print('The number is:',bin(num))
else:
    #prints negative decimals as a twos complement
    bin_num=bin((1<<num_bits) + num)
    print('The binary number is ' + str(bin_num))
