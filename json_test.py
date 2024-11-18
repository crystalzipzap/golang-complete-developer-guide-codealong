import os
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

    def get_sorted_files(self) -> List[str]:
        """Get sorted list of files in the format ord_aaaa format."""
        files = [f for f in os.listdir(self.directory_path) 
                if os.path.isfile(os.path.join(self.directory_path, f)) 
                and f.startswith('ord_')]
        return sorted(files)

    def test_parse_json(self, json_str: str) -> bool:
        """Test if string can be parsed as JSON."""
        try:
            json_obj = json.loads(json_str)
            return True
        except json.JSONDecodeError as e:
            print(f"JSON Parse Error: {str(e)[:100]}")
            return False

    def process_file(self, file_path: str) -> None:
        """Process a single file and print JSON parsing results."""
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                
                # Find all potential JSON objects
                matches = re.finditer(self.json_pattern, content)
                
                for match in matches:
                    json_str = match.group()
                    if self.test_parse_json(json_str):
                        self.json_count += 1
                        if self.json_count % 100 == 0:  # Print every 100th JSON
                            print(f"\nValid JSON #{self.json_count}:")
                            print(json_str[:200] + "..." if len(json_str) > 200 else json_str)
                    else:
                        self.error_count += 1

        except UnicodeDecodeError:
            print(f"Unicode decode error in file: {file_path}")
            with open(file_path, 'r', encoding='latin-1') as file:
                # Repeat the same process with latin-1 encoding
                content = file.read()
                matches = re.finditer(self.json_pattern, content)
                for match in matches:
                    json_str = match.group()
                    if self.test_parse_json(json_str):
                        self.json_count += 1
                    else:
                        self.error_count += 1

    def process_files(self) -> None:
        """Process all files in the directory."""
        files = self.get_sorted_files()
        print(f"Found {len(files)} files to process")

        for file_name in tqdm(files, desc="Processing files"):
            file_path = os.path.join(self.directory_path, file_name)
            print(f"\nProcessing: {file_name}")
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
import os
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

    def get_sorted_files(self) -> List[str]:
        """Get sorted list of files in the format ord_aaaa format."""
        files = [f for f in os.listdir(self.directory_path) 
                if os.path.isfile(os.path.join(self.directory_path, f)) 
                and f.startswith('ord_')]
        return sorted(files)

    def test_parse_json(self, json_str: str) -> bool:
        """Test if string can be parsed as JSON."""
        try:
            json_obj = json.loads(json_str)
            return True
        except json.JSONDecodeError as e:
            print(f"JSON Parse Error: {str(e)[:100]}")
            return False

    def process_file(self, file_path: str) -> None:
        """Process a single file and print JSON parsing results."""
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                
                # Find all potential JSON objects
                matches = re.finditer(self.json_pattern, content)
                
                for match in matches:
                    json_str = match.group()
                    if self.test_parse_json(json_str):
                        self.json_count += 1
                        if self.json_count % 100 == 0:  # Print every 100th JSON
                            print(f"\nValid JSON #{self.json_count}:")
                            print(json_str[:200] + "..." if len(json_str) > 200 else json_str)
                    else:
                        self.error_count += 1

        except UnicodeDecodeError:
            print(f"Unicode decode error in file: {file_path}")
            with open(file_path, 'r', encoding='latin-1') as file:
                # Repeat the same process with latin-1 encoding
                content = file.read()
                matches = re.finditer(self.json_pattern, content)
                for match in matches:
                    json_str = match.group()
                    if self.test_parse_json(json_str):
                        self.json_count += 1
                    else:
                        self.error_count += 1

    def process_files(self) -> None:
        """Process all files in the directory."""
        files = self.get_sorted_files()
        print(f"Found {len(files)} files to process")

        for file_name in tqdm(files, desc="Processing files"):
            file_path = os.path.join(self.directory_path, file_name)
            print(f"\nProcessing: {file_name}")
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
