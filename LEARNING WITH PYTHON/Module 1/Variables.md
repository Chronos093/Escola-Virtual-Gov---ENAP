# Variables
  Variables are the same as variables in math, except math variables are often letters, but programming variables could be words.

### Note about variable declaration:
 - Case-sensitive;
 - MUST start with either a letter or underscore; CANNOT start with numbers;
 - CANNOT be the same name as Python Keywords (e.g. calss, finally, etc.);
 - do NOT specify type od information stored in the variable (*Refer to the following codes for an example*);

In []: 

    # Exemple of variable declarations
    width = 10
    	 
    # Notice the "H" is capitalized
    Height = 5
    area = 0
In []: `print(width)`
Out []: 10

In []:

    # Expect an ERROR because the "height" variable is case-sensitive.
    # ERROR CODE: "height" is not defined.
    print(height)
-

    ---------------------------------------------------------------------------
    NameError   Traceback (most recent call last)
    <ipython-input-6-d56756f3e5e3> in <module>()
     2 # ERROR CODE: "height" is not defined.
     3 
    ----> 4  height
    
    NameError: name 'height' is not defined

In []: `print(Height)`
Out []: 5

In []: 

    # Using a python keyword as a variable name
    # ERROR CODE: invalid syntax
    global = 1
    print(global)
.

    File "<ipython-input-8-4909dc42d849>", line 4
	global = 1
           ^
	SyntaxError: invalid syntax

In []:

    # More declarations for different variable types
	# storing a string
	helloMessage = "Hello World!"
	first_name = "John"
	
	# storing a char
	character_example = 'a'
	
	# storing a float
	_newFloat = 1.0
	
	#storing a boolean value
	bool_Condition = True
	
In []: `print(helloMessage)`

Out []: 'Hello World!'

In []:`print(character_example)`

Out []: 'a'

In []:`print(_newFloat)`

Out []: 1.0

In []:`print(bool_Condition)`

Out []: True	
