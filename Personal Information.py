orang = {"name": "Namjoon", "gender": "Male", "age": "27", "address": "Seoul, South Korea", "phone": "1234"}

info = input("Please state the information that you want: ")
result = orang.get(info, "The information is not available")

print(result)
