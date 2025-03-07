#abbr
input_string=input()
matrix_strings_without_space=input_string.split(' ')
output_string=""
for item in matrix_strings_without_space:
    first_simvol=item[0]
    if first_simvol.isalpha():
        output_string=output_string+first_simvol.capitalize()
print(output_string)