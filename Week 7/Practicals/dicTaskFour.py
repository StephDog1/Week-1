staff = {"Pete", "Kelly", "Jon", "Paul", "Sally", "Sue"}
directors = {"Kelly", "Rupert", "Cyril", "Jon"}

external = directors - staff
staff_or_external = directors ^ staff
common = staff & directors
union = staff | directors

print(external)
print(staff_or_external)
print(common)
print(union)