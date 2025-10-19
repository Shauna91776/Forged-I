
# ==================================
# QUESTION 1: FILTER OUT PRIME NUMBERS
# ==================================

def filter_primes(numbers):
    # non_prime
    #for i range(2,i+1):
    # if i == 2:
         #numbers.remove(i)
    #elif i % i !=0
    #non-prime.append(i)
    #if i % 2 != 0
    #elif i % 3 != 0
    # 5678
    
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
    #pass  # TODO: implement function logic here

    for num in numbers:
        non_prime = []
        if num >1:
            for i in range(2, num):
                if num % i  == 0:
                    non_prime.append(num)
                    break
    return non_prime
        

print(filter_primes([2, 3, 4, 5, 6, 7, 8]))


# ==================================
# QUESTION 2: DRAW A SQUARE
# ==================================

def draw_square(size):
    #for i in number: 
    #return n * "*"
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
    #pass  # TODO: implement function logic here
 
    total = ""
    for i in range(size):
        row = size * "*" + '\n'
        total += row
        
    return total
        
#print(draw_square(3))
    


# ==================================
# QUESTION 3: AFFORDABLE ITEMS
# ==================================

def get_affordable_items(data):
    
    data = [
        {"name": "Laptop", "price": 120.0, "in_stock": True, "category": "electronics"},
        {"name": "Book", "price": 15.0, "in_stock": False, "category": "books"},
        {"name": "Phone", "price": 80.0, "in_stock": True, "category": "electronics"}
        ]
    #for price in data[price]:
    #if price < 100:
         #affordable.append(data[name], data[price])
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
    #pass  # TODO: implement function logic here
    affordable = {}
    for price in data[price]:
        if price < 100:
            return data["name"], data["price"]

data = [
     {"name": "Laptop", "price": 120.0, "in_stock": True, "category": "electronics"},
     {"name": "Book", "price": 15.0, "in_stock": False, "category": "books"},
     {"name": "Phone", "price": 80.0, "in_stock": True, "category": "electronics"}
     ]
#print(get_affordable_items(data))
        
        
            


# ==================================
# BONUS QUESTIONS (Intermediate Practice)
# ==================================

def reverse_words(sentence):
    # split, reverse [:: -1], .joint(" ")
    """
    Takes a sentence string and returns it with the word order reversed.

    Example:
    --------
    >>> reverse_words("The sky is blue")
    'blue is sky The'
    """
   # pass  # TODO: implement function logic here
    split_sentence = sentence.split(" ")
    reverse_sentence = split_sentence[::-1]
    joined_sentence = " ".join(reverse_sentence)
    return joined_sentence

#print(reverse_words("The sky is blue"))
   


def count_vowels(word):
    #vowel =[]
    #for char in words.lower():
    #if char in vowels:
    #return f"Vowles are: {char}"
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
    #pass  # TODO: implement function logic here
    vowel_counter = 0
    vowels = ["a", "e", "i", "o", "u"]
    for char in word.lower():
        if char in vowels:
            vowel_counter += 1
    return vowel_counter

#print(count_vowels("ShaunaLIze"))
    

