immutable_var = "Hello", 12, True, 5.5, "job"
print(immutable_var)
immutable_var[0] = "Hi"
print(immutable_var)
#при выводе данных программа выдает ошибку, т.к. кортеж относится к неизменяемым типам данных.
print()
mutable_list = ["Hello", 12, True, 5.5, "job"]
print(mutable_list)
mutable_list[0] = "Hi"
print(mutable_list)
mutable_list.append(False)
print(mutable_list)
mutable_list.extend(["home", "work"])
print(mutable_list)
mutable_list.remove(True)
print(mutable_list)
print()
print("Hi" in mutable_list)
print(True not in mutable_list)
print(mutable_list[0::2])