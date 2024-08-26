z = ['1,2,3,4,','Alice','Bob']
z.sort

print("Hello there!\nHow are you?\nl\'m doing fine")

multi_line = """Hello there!
How are you? 
i'm fine."""
print(multi_line)

spam = 'Hello World'
spam.strip()
spam.lstrip("Hello")
spam.rstrip("World")

a = ','.join(['cats','rats','bats'])
print(a)
a =''.join(['My','name','is','Simon'])
print(a)
a = 'ABC'.join(['My','name','is','Simon'])
print(a)
a ='My name is Simon'.split()
print(a)
a = 'MyABCnameABCisABCSimon'.split('ABC')
print(a)
a = 'My name is Simon'.split('m')
print(a)