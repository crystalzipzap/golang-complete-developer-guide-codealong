import os
import re
import json
from typing import List, Dict, Any

class JsonFileParser:
    def __init__(self, directory_path: str):
        self.directory_path = directory_path
        self.json_pattern = r'\{(?:[^{}]*|\{(?:[^{}]*|\{[^{}]*\})*\})*\}'
        self.event_date_count = 0
        self.incomplete_data = ""

    def get_sorted_files(self) -> List[str]:
    """Get sorted list of files in the format ord_aaaa, ord_aaab, etc."""
    files = [f for f in os.listdir(self.directory_path) 
            if os.path.isfile(os.path.join(self.directory_path, f)) 
            and f.startswith('ord_')]
    
    def natural_sort_key(filename: str) -> int:
        """Custom sort key for ord_aaaa format."""
        # Extract the 4-character suffix after 'ord_'
        suffix = filename.split('_')[1]
        # Convert to numeric value for sorting
        value = 0
        for i, char in enumerate(reversed(suffix)):
            # Calculate position value: a=0, b=1, etc.
            # Multiply by power of 26 based on position
            value += (ord(char) - ord('a')) * (26 ** i)
        return value

    return sorted(files, key=natural_sort_key)

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
        total_files = len(files)
        
        print(f"Found {total_files} files to process")
        
        for i, file_name in enumerate(files, 1):
            file_path = os.path.join(self.directory_path, file_name)
            print(f"Processing file {i}/{total_files}: {file_name}")
            
            content = self.read_file_content(file_path)
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
            
            print(f"Current Event_Date count: {self.event_date_count}")

    def get_results(self) -> Dict[str, int]:
        """Return processing results."""
        return {
            "Event_Date_Count": self.event_date_count,
            "Remaining_Data_Length": len(self.incomplete_data)
        }

def main():
    # Directory containing the sliced files
    directory_path = "output_dir"
    
    parser = JsonFileParser(directory_path)
    parser.process_files()
    results = parser.get_results()
    
    print("\nFinal Results:")
    print(f"Total Event_Date occurrences: {results['Event_Date_Count']}")
    print(f"Remaining unparsed data length: {results['Remaining_Data_Length']}")
    
    if results['Remaining_Data_Length'] > 0:
        print("Warning: Some data remained unparsed at the end of processing")

if __name__ == "__main__":
    main()
