string_input=input()
digit=int(input())
string_output=""
index=0
delta=2*digit
for index in range(index,len(string_input),delta):
    string_srez=string_input[index:index+digit]
    string_output=string_output+string_srez[::-1]+string_input[index+digit:index+delta]
print(string_output)