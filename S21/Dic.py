d = {"name":"Fateme", "Age":18, "Avg":17.95}

#print(d["name"])
# print(d[0])


# d2 = dict(name="Fateme", age = 18, avg = 17.95)
# print(d2["avg"])
# print(d2.get("name"))

# print(d)

# d["name"] = "Zahra"

# print(d)

# del d["name"]

# print(d)

# d["Name"] = "Ali"

# print(d)
# value = d.pop("Name")
# print(d)
# print(value)


for key in d:
    print(key)

print()

for value in d.values():
    print(value)


for key, value in d.items():
    print(f"{key}:{value}")