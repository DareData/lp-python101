# Jupyter notebook

Check which of the built-in functions allows you to:

- Iterate over multiple iterables at the same time and use it to print full names from names and surnames.

  names = ['Jake','Amy','Raymond','Rosa','Charles','Terry']
  surnames = ['Peralta','Santiago','Holt','Diaz','Boyle','Jeffords']

- Get the smallest/largest item in an iterable. Use `numbers = [23e4,14,15.2,2329e-4,4924,2e-1]`
- Check if any element of an iterable is True. Use 

    `list_with_true = [1,4,"ChatGPT",True,13.4]`
    `list_with_true_2 = [1,4,"ChatGPT",False,13.4]`
    `list_without_true = [0,0,"",False,False]`

Notice that Python interprets False, 0 or empty strings as False while the rest of the elements as True.
- Check if all elements of an iterable are True. You can reuse `list_with_true` and `list_with_true_2`.

# Script

### Fibonacci

In the Fibonacci sequence, each number is the sum of the two preceding ones. 

0, 1, 1, 2, 3, 5, 8, 13, 21, 34,...

Create a `fib.py` scrip that asks for an element and uses a function that calculates the Fibonacci number at a given step.

```python
fib(0)             # 0 - first element
fib(1)             # 1 - second element
fib(2)             # 1 - third element
fib(3)             # 2 - fourth element
fib(8)             # 21 - ninth element
```

