alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

string_input= raw_input("Enter a string: ")
shift_input= int(input("Enter in a value to shift by: "))
shift_input=shift_input%26
input_length= len(string_input)



string_output=""

for i in range(input_length):
    character= string_input[i]
    location_of_character= alphabet.find(character)
    new_location = location_of_character+shift_input
    
    if new_location >=26:
        new_location-=26
    
    
    
    string_output+= alphabet[new_location]

print("Encrypted text is: "+string_output)