# Conditional Statements

## IF Conditions
Important Notices:

- Order of the conditions matter!

  - If more than one conditions are satified, then the actions associated with the first satifying condition will execute and skip the remainig conditions and codes;

- "elif" == "else if"

  - "elif" denotes the same meaning as "else if"
- At least one condition MUST be provided for both if and elif clauses, else ERROR!
- Parentheses fot if and elif is optinoal. Your code will work with of wthout the ().

## Switch Cases
Python does NOT have an implementation for the switch cases, but one way to implement the switch case is with the dictionary, a data structure that stores the key-value pair.

- The switch conditions are stored as keys in the dictionary, and actions stored as the value.

  - If there is a series of actions for each case, then consider writing a function for each case and use the function calls as the value.

- The default condition is manually listed as a key-value un the get().  