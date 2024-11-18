import os
import re
import json
from typing import List, Dict, Any
from tqdm import tqdm

class JsonTester:
    def __init__(self, directory_path: str):
        self.directory_path = directory_path
        # Optimized regex pattern to avoid backtracking
        self.json_pattern = r'\{(?:[^{}]|(?R))*\}'
        self.event_date_count = 0
        self.error_count = 0

    def get_sorted_files(self) -> List[str]:
        """Get sorted list of files in the format ord_00001.erf to ord_79554.erf."""
        files = [f for f in os.listdir(self.directory_path) 
                if os.path.isfile(os.path.join(self.directory_path, f)) 
                and f.startswith('ord_') and f.endswith('.erf')]
        
        def natural_sort_key(filename: str) -> int:
            return int(filename.split('_')[1].split('.')[0])
        
        return sorted(files, key=natural_sort_key)

    def process_file(self, file_path: str) -> None:
        """Process a single file and count Event_Date occurrences."""
        try:
            with open(file_path, 'r', encoding='latin-1') as file:
                content = file.read()
                
                # Find all JSON objects in the file
                matches = re.finditer(self.json_pattern, content, re.VERBOSE)
                
                for match in matches:
                    json_str = match.group()
                    try:
                        json_obj = json.loads(json_str)
                        self.count_event_date(json_obj)
                    except json.JSONDecodeError:
                        self.error_count += 1

        except Exception as e:
            print(f"Error processing file {file_path}: {str(e)}")

    def count_event_date(self, obj: Any) -> None:
        """Recursively count occurrences of Event_Date in JSON object."""
        if isinstance(obj, dict):
            for key, value in obj.items():
                if key == "Event_Date":
                    self.event_date_count += 1
                self.count_event_date(value)
        elif isinstance(obj, list):
            for item in obj:
                self.count_event_date(item)

    def process_files(self) -> None:
        """Process all files in directory."""
        files = self.get_sorted_files()
        print(f"Found {len(files)} files to process")
        
        for file_name in tqdm(files):
            file_path = os.path.join(self.directory_path, file_name)
            self.process_file(file_path)

    def get_results(self) -> Dict[str, int]:
        """Return processing results."""
        return {
            "Event_Date_Count": self.event_date_count,
            "Error_Count": self.error_count
        }

def main():
    directory_path = "output_dir"
    tester = JsonTester(directory_path)
    tester.process_files()
    results = tester.get_results()
    
    print("\nFinal Results:")
    print(f"Total Event_Date occurrences: {results['Event_Date_Count']}")
    print(f"Total parsing errors: {results['Error_Count']}")

if __name__ == "__main__":
    main()
