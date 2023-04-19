## write a program to invert keys and values

ini_dict = {101: "akshat", 201: "ball"}
print(ini_dict)
inv_dict = {value: key for key, value in ini_dict.items()}

print(inv_dict)