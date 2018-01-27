#!/usr/bin/python

print '.subckt mult32 a[31:0] b[31:0] p[31:0]'
print ''

# Generate partial products
print '* Partial products'
for i in range(0, 31):
    print 'Xpp{} b[{}]#{} a[{}:0] pp{}[{}:0] and2' .format(i, i, 32-i, 31-i, i, 31-i)
print 'Xpp31 b[31] a[0] pp31[0] and2'
print ''

# Sum partial products
print '* Sum of partial products'

print '.connect pp0[0] p[0]'
print ''

print 'Xfa10 pp0[1] pp1[0] 0 p[1] co1[0] full_adder'
print ''

for i in range(2, 32):      # i is product column index
    for j in range(0, i-1): # j is full_adder row index for column
        if (j == 0):
            print 'Xfa{}{} pp{}[{}] pp{}[{}] co{}[{}] sum{}[{}] co{}[{}] full_adder'.format(i, j, 0, i, j+1, i-1-j, i-1, j, i, j, i, j)
        else:    
            print 'Xfa{}{} sum{}[{}] pp{}[{}] co{}[{}] sum{}[{}] co{}[{}] full_adder'.format(i, j, i, j-1, j+1, i-1-j, i-1, j, i, j, i, j)

    print 'Xfa{}{} sum{}[{}] pp{}[{}] 0 p[{}] co{}[{}] full_adder'.format(i, i-1, i, i-2, i, 0, i, i, i-1) #j=i-1
    print ''

print '.ends'
