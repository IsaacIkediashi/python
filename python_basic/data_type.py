x = 5 #------------------------------------ number
x = 'Hello World' #------------------------ string
x = 20.5 #--------------------------------- float
x = 1j #----------------------------------- complex
x = ["apple","banana","cherry"] #---------- list
x = ("apple","banana","cherry") #---------- tuple
x = range(6) #----------------------------- range
x = {"name":"John","age":36} #------------- dict
x = {"apple","banana","cherry"} #---------- set
x = frozenset({"apple","banana","cherry"}) #------ frozenset
x = True #---- ----------------------------- bool
x = b"Hello" #------------------------------ bytes
x = bytearray(5) #-------------------------- bytearray
x = memoryview(bytes(6)) #------------------ memoryview

#------ setting the specific data type
integer = int(5) #------------------------------------ number
string = str('Hello World') #------------------------ string
float = float(20.5) #--------------------------------- float
complex = complex(1j) #----------------------------------- complex
list = list(("apple","banana","cherry")) #---------- list
tuple = tuple(("apple","banana","cherry")) #---------- tuple
range = range(6) #----------------------------- range
dict = dict({"name":"John","age":36}) #------------- dict
set = set(("apple","banana","cherry")) #---------- set
frozenset = frozenset(("apple","banana","cherry")) #------ frozenset
bool = bool(5) #---- ----------------------------- bool
bytes = bytes(5) #------------------------------ bytes


#------ To verify the type of an object, we use the type() function
u = 1 #int
v = 2.0 #float
w = 1j #complex

print(type(u)) #------ outputs <class 'int'>
print(type(v)) #------ outputs <class 'float'>
print(type(w)) #------ outputs  <class 'complex'>
 

 
 

