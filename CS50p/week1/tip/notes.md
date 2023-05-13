## Explanation:

- `dollars_to_float` function takes a string d as input and removes the leading "$" symbol by calling strip method on d with "$" as the argument. The result is then converted to float using the float function.
- `percent_to_float` function takes a string p as input and removes the trailing "%" symbol in a similar manner. Then it divides the result by 100 to convert the percentage to its equivalent decimal representation.