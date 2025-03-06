string_input=input()
digit=int(input())
string_output=""
index=0
while index+digit<len(string_input)+1:
    string_srez=string_input[index:index+digit]
    string_output=string_output+string_srez[::-1]+string_input[index+digit:index+2*digit]
    index+=2*digit
string_output+=string_input[index:-1]
print(string_output)

