digit_input=input()
dictionary={}


for index in range(len(digit_input)):
    digit_current=digit_input[index]
    if  digit_current in dictionary:
        dictionary[digit_current]+=1
    else:
        dictionary[digit_current]=1

print(dictionary)
for digit in dictionary:
    print("число", digit,"встретилось раз:",dictionary[digit],sep=" ")