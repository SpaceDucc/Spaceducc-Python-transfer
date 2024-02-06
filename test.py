var1 = [10]
var2 = [20]

def testfunc(a,b) :
    a[0] = a[0] + 10 
    b[0] = b[0] + 20

testfunc(var1,var2)
print(var1[0])
print(var2[0])