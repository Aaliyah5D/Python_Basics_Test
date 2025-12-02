

def add(num1, num2):
    return num1 + num2
    pass  # Implement addition

def subtract(num1, num2):
    return  num2- num1
    pass  # Implement subtraction

def multiply(num1, num2):
    return num1 * num2
    pass  # Implement multiplication

def divide(num1, num2):
    return num2 / num1
    pass  # Implement division with zero division check

def fizz_buzz(number):
   for i in range(1, number + 1):
       if i % 3 == 0 and i % 5 == 0:
           print("FizzBuzz")
       elif i % 3 == 0: 
           print("Fizz")
       elif i % 5 == 0: 
           print("Buzz")
       else: 
           print(i)
           
       
    pass  # Implement FizzBuzz logic

def fibonacci(n):
     if n == 0:
        return 0 
    if n == 1:
        return 1 
    return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(6))
    pass  # Implement Fibonacci sequence logic
        
def triangle(n):
    for i in range(6, 0, -1): 
        for j in range(0, 1, -1): 
            print("*" , end=' ')
        print(" ")
    pass  # Implement triangle generation logic

def return_list_stats(numbers):
    """Given the list 'numbers', use the relevant functions to return a
        dictionary of statics for the list. This dictionary must have
        the following keys:
            unique_numbers : a set containing unique numbers from the list 'numbers',
            max : largest number in the list 'numbers',
            min : smallest number in the list 'numbers',
            average : average of the numbers in the list 'numbers',
            even_pairs : a list of tuples that have neighboring pairs 
                that sum up to an even number in the list 'numbers',
            odd_pairs : a list of tuples that have neighboring pairs 
                that sum up to an even number in the list 'numbers',
            even_numbers : a tuple of all the even numbers in the list
                'numbers',
            odd_numbers : a tuple of all the odd numbers in the list 
                'numbers',
            number_of_even_numbers : the total number of even numbers in the 
                list 'numbers',
            number_of_odd_numbers : the total number of even numbers in the list
                 'numbers'
    """

    def return_list_stats(numbers):
    """Return a dictionary of statistics for the list 'numbers'."""
    
    # 1. Unique numbers
    unique_numbers = set(numbers)

    # 2. Maximum and minimum
    max_number = max(numbers)
    min_number = min(numbers)

    # 3. Average
    average = sum(numbers) / len(numbers)

    # 4. Neighboring even-sum and odd-sum pairs
    even_pairs = []
    odd_pairs = []

    for i in range(len(numbers) - 1):
        pair = (numbers[i], numbers[i + 1])
        if (numbers[i] + numbers[i + 1]) % 2 == 0:
            even_pairs.append(pair)
        else:
            odd_pairs.append(pair)

    # 5. Even and odd numbers
    even_numbers = tuple(num for num in numbers if num % 2 == 0)
    odd_numbers = tuple(num for num in numbers if num % 2 != 0)

    # 6. Counts
    number_of_even_numbers = len(even_numbers)
    number_of_odd_numbers = len(odd_numbers)

    # Return the dictionary
    return {
        "unique_numbers": unique_numbers,
        "max": max_number,
        "min": min_number,
        "average": average,
        "even_pairs": even_pairs,
        "odd_pairs": odd_pairs,
        "even_numbers": even_numbers,
        "odd_numbers": odd_numbers,
        "number_of_even_numbers": number_of_even_numbers,
        "number_of_odd_numbers": number_of_odd_numbers
    }

    pass

# TODO: (Bonus) Implement the pascal_triangle function below
def pascal_triangle(n):
    """
    Generates Pascal's triangle and returns the final row as a list.

    Parameters:
    n (int): The row number of Pascal's triangle to generate (0-based index).

    Returns:
    list: The final row of Pascal's triangle as a list.

    Formula for Pascal's Triangle:
    Each element in Pascal's triangle can be calculated using the following formula:

    C(n, k) = n! / (k! * (n-k)!)

    Where:
    - n is the row number (0-based index)
    - k is the column number (0-based index)
    - C(n, k) represents the value at row n and column k in Pascal's triangle
    - n! represents the factorial of n

    To generate a row of Pascal's triangle, iterate over the columns from 0 to n.
    Calculate each element using the formula and store them in a list to form the row.
    Repeat this process for each row up to the desired row number.

    Example:
     * Input: n = 6
     * Output:
     *           1
     *         1   1
     *       1   2   1
     *     1   3   3   1
     *   1   4   6   4   1
     * 1   5  10   10  5   1
    """
    import math

def pascal_triangle(n):
    """
    Generates Pascal's triangle and returns the final row as a list.
    """
    row = []  # this will store the nth row

    # iterate over each column k from 0 to n
    for k in range(n + 1):
        # compute combination C(n, k)
        value = math.factorial(n) // (math.factorial(k) * math.factorial(n - k))
        row.append(value)

    return row

    pass
