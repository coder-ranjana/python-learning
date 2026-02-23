# returns the key according to value

student = {
    "name" : "Ranjana Rauniayr",
    "subject" : {
        "math" : 95,
        "chem" : 80,
        "engl" : 95,
        "phy" : 75

    }
}
print(student.get("name"))
print(student["name"])