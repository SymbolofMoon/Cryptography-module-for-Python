alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ"

string_input= raw_input("Enter a string: ")

input_length= len(string_input)



string_output=""

for i in range(input_length):
    character= string_input[i]
    location_of_character= alphabet.find(character)
    new_location = location_of_character+13
    
    if new_location >=26:
        new_location-=26
    
    
    
    string_output+= alphabet[new_location]

print("Encrypted text is: "+string_output)