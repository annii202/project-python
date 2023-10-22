import os
import unittest
from dataProcessor import read_json_file

class TestDataProcessor(unittest.TestCase):
    def test_read_json_file_success(self):
        current_directory = os.path.dirname(__file__)
        file_path = os.path.join(current_directory, "users.json")

        data = read_json_file(file_path)
       
        self.assertEqual(len(data), 1000)  # Ajustar o número esperado de registros
        self.assertEqual(data[0]['name'], 'Pamela Bray')
        self.assertEqual(data[1]['age'], 30)

    def test_read_json_file_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            read_json_file("non_existent.json")

    def test_read_json_file_invalid_json(self):
        with open("invalid.json", "w") as file:
            file.write("invalid json data")
        with self.assertRaises(ValueError):
            read_json_file("invalid.json")
    def test_avgAgeCountry_empty_json(self):
        # Test when the JSON file is empty.
        with open("empty.json", "w") as file:
            file.write("[]")
        data = read_json_file("empty.json")
    def test_avgCountry_missing_country_values(self):
        current_directory = os.path.dirname(__file__)
        file_path = os.path.join(current_directory, "users.json")
        data = read_json_file(file_path)    
        self.assertNotIn('country', data[0], "A chave 'country' não existe no dicionário.")
        self.assertNotIn('country', data[2], "A chave 'country' não existe no dicionário.")
    def test_avgCountry_null_country_values(self):
        current_directory = os.path.dirname(__file__)
        file_path = os.path.join(current_directory, "users.json")
        data = read_json_file(file_path)    
        self.assertIsNone(data[1]['country'], "A chave 'country' não está preenchida.")
    def test_avgAge_missing_country_values(self):
        current_directory = os.path.dirname(__file__)
        file_path = os.path.join(current_directory, "users.json")
        data = read_json_file(file_path)    
        self.assertNotIn('age', data[3], "A chave 'age' não existe no dicionário.")
    def test_avgAge_null_country_values(self):
        current_directory = os.path.dirname(__file__)
        file_path = os.path.join(current_directory, "users.json")
        data = read_json_file(file_path)    
        self.assertIsNone(data[4]['age'], "A chave 'age' não está preenchida.")
    
if __name__ == '__main__':
    unittest.main()