# Define a dictionary mapping prompt names to their respective file names.
prompts_dict = {'raw_to_structured': 'raw_to_structured.txt'}

def get_prompt(prompt_name):
    """
    Retrieves the content of a prompt based on its name.

    This function looks up the file associated with the given prompt name in the
    prompts_dict dictionary, reads the file content, and returns it.

    Args:
        prompt_name (str): The name of the prompt to retrieve.

    Returns:
        str: The content of the prompt file.

    Raises:
        KeyError: If the prompt_name is not found in the prompts_dict.
        FileNotFoundError: If the file associated with the prompt_name does not exist.
    """
    # Look up the file name in the prompts dictionary using the provided prompt name.
    prompt_file = prompts_dict[prompt_name]

    # Open the file, read its contents, and return the content.
    with open(prompt_file, 'r') as f:
        prompt_content = f.read()
    return prompt_content

# Example usage
# Assuming 'abcd.txt' exists and contains the text for the prompt.
# try:
#     prompt_text = get_prompt('raw_to_structured')
#     print(prompt_text)
# except KeyError:
#     print("Prompt name not found.")
# except FileNotFoundError:
#     print("Prompt file not found.")
