In this implementation,
the try block attempts to parse the input fraction into two integers,
and then checks if they satisfy the conditions for a valid fraction.
If any of these operations
  raise a ValueError or a ZeroDivisionError, the corresponding exception is caught in the except block.
The except block prints an error message indicating what went wrong, and then prompts the user again for a new fraction.
The while loop continues until a valid fraction is entered, at which point the function returns the parsed integers.
