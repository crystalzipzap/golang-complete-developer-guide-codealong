=import os
import re
import json
from typing import List, Dict, Any
from tqdm import tqdm

class JsonTester:
    def __init__(self, directory_path: str):
        self.directory_path = directory_path
        self.json_pattern = r'\{(?:[^{}]*|\{(?:[^{}]*|\{[^{}]*\})*\})*\}'
        self.json_count = 0
        self.error_count = 0
        # List of encodings to try
        self.encodings = ['utf-8', 'latin-1', 'cp1252', 'iso-8859-1']

    def read_file_with_fallback(self, file_path: str) -> str:
        """Try multiple encodings to read the file."""
        content = None
        successful_encoding = None

        for encoding in self.encodings:
            try:
                with open(file_path, 'r', encoding=encoding) as file:
                    content = file.read()
                successful_encoding = encoding
                break
            except UnicodeDecodeError:
                continue
            except Exception as e:
                print(f"Unexpected error reading file {file_path}: {str(e)}")
                continue

        if content is None:
            print(f"Failed to read file {file_path} with any encoding")
            return ""

        print(f"Successfully read file with encoding: {successful_encoding}")
        return content

    def test_parse_json(self, json_str: str, file_name: str) -> bool:
        """Test if string can be parsed as JSON."""
        try:
            json_obj = json.loads(json_str)
            return True
        except json.JSONDecodeError as e:
            print(f"JSON Parse Error in {file_name}: {str(e)[:100]}")
            return False

    def process_file(self, file_path: str) -> None:
        """Process a single file and print JSON parsing results."""
        file_name = os.path.basename(file_path)
        content = self.read_file_with_fallback(file_path)
        
        if not content:
            print(f"Skipping empty file: {file_name}")
            return

        # Find all potential JSON objects
        matches = re.finditer(self.json_pattern, content)
        
        for match in matches:
            json_str = match.group()
            if self.test_parse_json(json_str, file_name):
                self.json_count += 1
                if self.json_count % 1000 == 0:  # Print every 1000th JSON
                    print(f"\nValid JSON #{self.json_count} in {file_name}")
            else:
                self.error_count += 1

    def process_files(self) -> None:
        """Process all files in the directory."""
        files = sorted([f for f in os.listdir(self.directory_path) 
                if os.path.isfile(os.path.join(self.directory_path, f)) 
                and f.startswith('ord_')])
        
        print(f"Found {len(files)} files to process")

        for file_name in tqdm(files, desc="Processing files"):
            file_path = os.path.join(self.directory_path, file_name)
            file_size = os.path.getsize(file_path)
            print(f"\nProcessing: {file_name} (Size: {file_size/1024/1024:.2f} MB)")
            
            self.process_file(file_path)
            print(f"Current counts - Valid JSONs: {self.json_count}, Errors: {self.error_count}")

def main():
    directory_path = "output_dir"
    tester = JsonTester(directory_path)
    tester.process_files()
    
    print("\nFinal Results:")
    print(f"Total valid JSON objects found: {tester.json_count}")
    print(f"Total parsing errors: {tester.error_count}")

if __name__ == "__main__":
    main()
