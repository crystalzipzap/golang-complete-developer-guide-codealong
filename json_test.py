import os
import re
import json
from typing import List, Dict, Any
from tqdm import tqdm

class JsonTester:
    def __init__(self, directory_path: str):
        self.directory_path = directory_path
        # Simplified regex pattern to avoid catastrophic backtracking
        self.json_pattern = r'\{[^{}]*(?:\{[^{}]*\}[^{}]*)*\}'
        self.json_count = 0
        self.error_count = 0

    def get_sorted_files(self) -> List[str]:
        """Get sorted list of files in the format ord_aaaa format."""
        files = [f for f in os.listdir(self.directory_path) 
                if os.path.isfile(os.path.join(self.directory_path, f)) 
                and f.startswith('ord_')]
        return sorted(files)

    def process_file(self, file_path: str) -> None:
        """Process a single file and print JSON parsing results."""
        try:
            with open(file_path, 'r', encoding='latin-1') as file:
                content = file.read()
                
                # Find all potential JSON objects
                matches = re.finditer(self.json_pattern, content)
                
                for match in matches:
                    json_str = match.group()
                    try:
                        json_obj = json.loads(json_str)
                        self.json_count += 1
                        if self.json_count % 1000 == 0:
                            print(f"\nProcessed {self.json_count} JSON objects")
                    except json.JSONDecodeError:
                        self.error_count += 1
                        if self.error_count % 100 == 0:
                            print(f"Parse errors: {self.error_count}")

        except Exception as e:
            print(f"Error processing file {file_path}: {str(e)}")

    def process_files(self) -> None:
        """Process all files in directory."""
        files = self.get_sorted_files()
        print(f"Found {len(files)} files to process")
        
        for file_name in tqdm(files):
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
