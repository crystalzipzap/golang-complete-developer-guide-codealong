import os
import re
import json
from typing import List, Dict, Any

class JsonFileParser:
    def __init__(self, directory_path: str):
        self.directory_path = directory_path
        # Regex pattern for JSON objects
        self.json_pattern = r'\{(?:[^{}]*|\{(?:[^{}]*|\{[^{}]*\})*\})*\}'
        self.event_date_count = 0
        self.incomplete_data = ""

    def get_sorted_files(self) -> List[str]:
        """Get sorted list of files from directory."""
        files = [f for f in os.listdir(self.directory_path) if os.path.isfile(os.path.join(self.directory_path, f))]
        # Sort files numerically
        return sorted(files, key=lambda x: int(''.join(filter(str.isdigit, x))))

    def read_file_content(self, file_path: str) -> str:
        """Read file content with proper encoding."""
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                return file.read()
        except UnicodeDecodeError:
            # Fallback to latin-1 if utf-8 fails
            with open(file_path, 'r', encoding='latin-1') as file:
                return file.read()

    def parse_json_object(self, json_str: str) -> Dict[str, Any]:
        """Parse JSON string and count Event_Date occurrences."""
        try:
            json_obj = json.loads(json_str)
            # Count Event_Date occurrences recursively
            self.count_event_dates(json_obj)
            return json_obj
        except json.JSONDecodeError:
            return None

    def count_event_dates(self, obj: Any) -> None:
        """Recursively count occurrences of Event_Date in JSON object."""
        if isinstance(obj, dict):
            for key, value in obj.items():
                if key == "Event_Date":
                    self.event_date_count += 1
                self.count_event_dates(value)
        elif isinstance(obj, list):
            for item in obj:
                self.count_event_dates(item)

    def process_files(self) -> None:
        """Process all files in the directory."""
        files = self.get_sorted_files()
        
        for file_name in files:
            file_path = os.path.join(self.directory_path, file_name)
            content = self.read_file_content(file_path)
            
            # Append any incomplete data from previous file
            content = self.incomplete_data + content
            
            # Find all JSON objects
            json_objects = re.finditer(self.json_pattern, content)
            
            last_end = 0
            for match in json_objects:
                json_str = match.group()
                parsed_obj = self.parse_json_object(json_str)
                last_end = match.end()
            
            # Store incomplete data for next iteration
            self.incomplete_data = content[last_end:]

    def get_results(self) -> Dict[str, int]:
        """Return processing results."""
        return {
            "Event_Date_Count": self.event_date_count
        }

def main():
    # Directory containing the sliced files
    directory_path = "output_dir"
    
    parser = JsonFileParser(directory_path)
    parser.process_files()
    results = parser.get_results()
    
    print(f"Total Event_Date occurrences: {results['Event_Date_Count']}")

if __name__ == "__main__":
    main()
