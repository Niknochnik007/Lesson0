immutable_var = (1, 2, 3, "b", "s")
print(immutable_var)
immutable_var.append(d)
print(immutable_var)
# кортеж нельзя изменить, можно только создать копию и добавить в него элемент

mutable_list = [1, 2, 3, "P", "N"]
print(mutable_list)
mutable_list.append(9)
print(mutable_list)