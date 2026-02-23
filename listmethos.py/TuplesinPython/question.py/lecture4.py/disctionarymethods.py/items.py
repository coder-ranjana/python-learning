# returns all (key, val) pairs as tuples
student = {
  "name" : "Ranjana Rauniayr",
  "subject" : {
   "math" : 80,
   "chem" : 90,
   "phy" : 75,
   "engl" :95
  }
 }
pairs = list(student.items())
print(pairs[0])