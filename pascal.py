dgt=input()
digit=int(dgt)
output=[None]*(digit+1)
def fact(n):
    output=1
    for index in range(2,n+1):
        output=output*index
    return output 

def binom(k,n):   #k сверху
    return fact(n)/(fact(n-k)*fact(k))
            

for index in range(digit+1):
    output[index]=int(binom(index,digit))

print(output)