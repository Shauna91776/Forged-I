
# ==================================
# QUESTION 1: FILTER OUT PRIME NUMBERS
# ==================================

def filter_primes(numbers):
    """
    Takes a list of integers and returns a new list
    with all prime numbers removed.

    Example:
    --------
    >>> filter_primes([2, 3, 4, 5, 6, 7, 8])
    [4, 6, 8]

    Notes:
    ------
    - A prime number is a number greater than 1 that has no divisors other than 1 and itself.
    - Use loop logic to determine primality (no external libraries).
    """
    pass  # TODO: implement function logic here


# ==================================
# QUESTION 2: DRAW A SQUARE
# ==================================

def draw_square(size):
    """
    Draws a square using asterisks ('*') and returns it as a string.

    Example:
    --------
    >>> print(draw_square(3))
    ***
    ***
    ***

    Notes:
    ------
    - Each row should contain exactly `size` number of asterisks.
    - Use '\n' to separate rows.
    - Do not print inside the function; just return the final string.
    """
    pass  # TODO: implement function logic here


# ==================================
# QUESTION 3: AFFORDABLE ITEMS
# ==================================

def get_affordable_items(data):
    """
    Takes a list of dictionaries representing store items and
    returns a dictionary of items that are affordable (price < 100).

    Example:
    --------
    >>> data = [
    ... {"name": "Laptop", "price": 120.0, "in_stock": True, "category": "electronics"},
    ... {"name": "Book", "price": 15.0, "in_stock": False, "category": "books"},
    ... {"name": "Phone", "price": 80.0, "in_stock": True, "category": "electronics"}
    ... ]
    >>> get_affordable_items(data)
    {'Book': 15.0, 'Phone': 80.0}

    Notes:
    ------
    - Only include items with a price below R100.
    - Return a dictionary where the key = item name, value = price.
    """
    pass  # TODO: implement function logic here


# ==================================
# BONUS QUESTIONS (Intermediate Practice)
# ==================================

def reverse_words(sentence):
    """
    Takes a sentence string and returns it with the word order reversed.

    Example:
    --------
    >>> reverse_words("The sky is blue")
    'blue is sky The'
    """
    pass  # TODO: implement function logic here


def count_vowels(word):
    """
    Counts and returns the number of vowels in a given word.

    Example:
    --------
    >>> count_vowels("forged")
    2

    Notes:
    ------
    - Vowels are: a, e, i, o, u
    - The function should be case-insensitive.
    """
    pass  # TODO: implement function logic here

