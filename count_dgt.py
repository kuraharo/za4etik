digit_input=input()
dictionary={"0":0,"1":0,"2":0,"3":0,"4":0,"5":0, "6":0,"7":0,"8":0,"9":0}


for index in range(len(digit_input)):
    digit_current=digit_input[index]
    dictionary[digit_current]+=1
for index in range(0,10):
    print("число", index,"встретилось раз:",dictionary[str(index)],sep=" ")