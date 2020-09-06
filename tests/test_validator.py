import unittest
from app.utility.validator import validate_name, validate_id, validate_phone_number


class TestUtility(unittest.TestCase):
    def test_validate_name_with_valid_input(self):
        self.assertEqual(True, validate_name("ดราก้อน"))

    def test_validate_name_with_valid_input_int(self):
        self.assertEqual(False, validate_name("1234"))

    def test_validate_name_with_valid_input_contained_string_of_int(self):
        self.assertEqual(False, validate_name("ดราก้อนDra123"))

    def test_validate_name_with_valid_input_contained_string_of_special_charactor(self):
        self.assertEqual(False, validate_name("Pu!"))

    def test_validate_name_with_valid_input_contained_string_of_special_charactor_more_one(self):
        self.assertEqual(False, validate_name("$หิว!เนี้ย#"))

    def test_validate_name_with_valid_input_contained_not_blank(self):
        self.assertEqual(False, validate_name(""))

    def test_validate_name_with_valid_input_contained_empty_input(self):
        self.assertEqual(False, validate_name("Puen Cho"))


if __name__ == '__main__':
    unittest.main()  # pragma: no cover
