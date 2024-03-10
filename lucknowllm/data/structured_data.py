import os
import json

class StructuredDataLoader:
    """
    A class for loading structured data from JSON files within a specified directory structure.
    
    This loader is designed to operate within a predefined folder hierarchy, where
    the base directory ('structured_data') contains subdirectories corresponding to different
    categories of structured data (e.g., 'art', 'history'). Each subdirectory may contain multiple
    JSON files, from which data can be loaded individually or in bulk.
    """

    def __init__(self):
        """
        Initializes the data loader by setting up the base path to the 'structured_data' folder.
        
        The base path is constructed relative to the location of this script, allowing for flexible
        use across different environments without the need to hard-code the absolute path.
        """
        # Correctly determine the script's directory for consistent relative path resolution.
        self.base_path = os.path.join(os.path.dirname(__file__), 'Structured_Data')

    def read_json_file(self, path):
        """
        Reads and returns the content of a JSON file located at a given path.
        
        Parameters:
        - path (str): The full path to the JSON file to be read.
        
        Returns:
        - dict: The content of the JSON file, parsed into a dictionary.
        """
        with open(path, 'r', encoding='utf-8') as file:
            return json.load(file)

    def get_data(self, folder_name, file_name=None):
        """
        Fetches and returns the data from JSON files located within a specified subfolder of the 'structured_data' directory.
        
        If a specific file name is provided, only the content of that file is returned. If no file name is provided,
        the function returns the contents of all files within the specified subfolder.
        
        Parameters:
        - folder_name (str): The name of the subfolder within 'structured_data' from which to load files.
        - file_name (str, optional): The name of a specific file to load from the subfolder. If None, all files
          in the subfolder are loaded. Defaults to None.
        
        Returns:
        - list of dict: A list of dictionaries, each containing the file name ('file_name') and its content ('data').
          If a specific file is not found, an appropriate message is printed.
        """
        folder_path = os.path.join(self.base_path, folder_name)
        data = []

        if file_name:
            # Construct the full path to the specified file and load its content if it exists.
            file_path = os.path.join(folder_path, file_name)
            if os.path.exists(file_path):
                data.append({'file_name': file_name, 'data': self.read_json_file(file_path)})
            else:
                print(f"File {file_name} not found in {folder_name}.")
        else:
            # Load the content of all JSON files in the specified subfolder.
            for filename in os.listdir(folder_path):
                file_path = os.path.join(folder_path, filename)
                if os.path.isfile(file_path) and filename.endswith('.json'):
                    data.append({'file_name': filename, 'data': self.read_json_file(file_path)})

        return data


# example use
# loader = StructuredDataLoader()
# # Example: Get data from a specific file
# data = loader.get_data(folder_name='Arts_and_Crafts', file_name= 'Facts.json')
# print(data)
