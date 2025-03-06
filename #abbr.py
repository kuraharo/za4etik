#abbr
input_string=input()
input_string=" "+input_string #добавляем пробел, чтобы цикл начинался с него
output_string=""
for index in range(0,len(input_string)-1):
    index_next=index+1
    simvol_current=input_string[index]
    simvol_next=input_string[index_next]
    nomer_simvola_next=ord(simvol_next)
    if simvol_current==" " and ((nomer_simvola_next<=ord('z') and nomer_simvola_next>=ord('A')) or (nomer_simvola_next<=ord('я') and nomer_simvola_next>=ord('А'))):
        if nomer_simvola_next<=ord('z') and nomer_simvola_next>=ord('A'): #слово с англ буквы
            if(nomer_simvola_next>=ord("a")):
                nomer_simvola_next-=32
            simvol_next_big=chr(nomer_simvola_next)
            output_string+=simvol_next_big
        else:  #слово с русской буквы
            if(nomer_simvola_next>=ord("а")):
                nomer_simvola_next-=32
            simvol_next_big=chr(nomer_simvola_next)
            output_string+=simvol_next_big
print(output_string)
