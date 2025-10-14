# ==================================
# TEST CASES
# ==================================
from first_forge import filter_primes, draw_square, get_affordable_items, reverse_words, count_vowels
import unittest

class TestForgedIAssessment(unittest.TestCase):

    def test_filter_primes(self):
        self.assertEqual(filter_primes([2, 3, 4, 5, 6, 7, 8]), [4, 6, 8])
        self.assertEqual(filter_primes([10, 11, 12, 13, 14, 15]), [10, 12, 14, 15])
        self.assertEqual(filter_primes([]), [])

    def test_draw_square(self):
        expected_3 = "***\n***\n***"
        expected_5 = "*****\n*****\n*****\n*****\n*****"
        self.assertEqual(draw_square(3), expected_3)
        self.assertEqual(draw_square(5), expected_5)

    def test_get_affordable_items(self):
        data = [
            {"name": "Laptop", "price": 120.0, "in_stock": True, "category": "electronics"},
            {"name": "Book", "price": 15.0, "in_stock": False, "category": "books"},
            {"name": "Phone", "price": 80.0, "in_stock": True, "category": "electronics"}
        ]
        self.assertEqual(get_affordable_items(data), {'Book': 15.0, 'Phone': 80.0})

    def test_reverse_words(self):
        self.assertEqual(reverse_words("The sky is blue"), "blue is sky The")
        self.assertEqual(reverse_words("Forged I"), "I Forged")
        self.assertEqual(reverse_words("Hello"), "Hello")

    def test_count_vowels(self):
        self.assertEqual(count_vowels("forged"), 2)
        self.assertEqual(count_vowels("MENTORSHIP"), 3)
        self.assertEqual(count_vowels("xyz"), 0)

if __name__ == "__main__":
    unittest.main()