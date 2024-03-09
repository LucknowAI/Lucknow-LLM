import os

# Define a dictionary mapping prompt names to their respective file names.
prompts_dict = {'raw_to_structured': 'raw_to_structured.txt'}

def get_prompt(prompt_name):
    """
    Retrieves the content of a prompt based on its name.

    This function looks up the file associated with the given prompt name in the
    prompts_dict dictionary. It constructs a path to the file based on the current
    script's directory to ensure the file is looked up in the same folder as the script.
    Then, it reads the file content and returns it.

    Args:
        prompt_name (str): The name of the prompt to retrieve.

    Returns:
        str: The content of the prompt file.

    Raises:
        KeyError: If the prompt_name is not found in the prompts_dict.
        FileNotFoundError: If the file associated with the prompt_name does not exist.
    """
    # Get the directory of the current script.
    current_folder = os.path.dirname(os.path.abspath(__file__))
    
    # Look up the file name in the prompts dictionary using the provided prompt name.
    prompt_file_name = prompts_dict[prompt_name]

    # Construct the full path to the file within the same directory as the script.
    prompt_file_path = os.path.join(current_folder, prompt_file_name)

    # Open the file, read its contents, and return the content.
    with open(prompt_file_path, 'r') as f:
        prompt_content = f.read()
    return prompt_content

def construct_prompt(prompt_name, content):
    """
    Constructs a full prompt by appending provided content to the prompt specified by name,
    followed by a formatted output section.

    This function first retrieves the prompt text using `get_prompt` based on the given
    prompt name. Then, it appends the provided content and a suffix indicating where
    the output should be appended. This is useful for generating formatted prompts for
    tasks like language modeling or other text processing tasks.

    Args:
        prompt_name (str): The name of the prompt to use as the base.
        content (str): The content to append to the base prompt.

    Returns:
        str: The constructed full prompt text.
    """
    prompt = get_prompt(prompt_name)
    full_prompt = prompt + content + "\n\nOutput: \n"
    return full_prompt


# Example usage
# Assuming 'abcd.txt' exists and contains the text for the prompt.
# try:
#     prompt_text = get_prompt('raw_to_structured')
#     print(prompt_text)
# except KeyError:
#     print("Prompt name not found.")
# except FileNotFoundError:
#     print("Prompt file not found.")
