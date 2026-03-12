#Figure out a way to store 9 & 9.0 as separate value in the set.(you can take help of built-in date types)
values = {9, 9.0}
print(values)

values = {
    ("float", 9.0),
    ("int", 9)

}
print(values)