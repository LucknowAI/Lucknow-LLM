import re

def clean_text(text):
    """
    Cleans the input text by removing newline characters and reducing all instances of multiple
    spaces to a single space.
    
    Parameters:
    - text (str): The input text to be cleaned.
    
    Returns:
    - str: The cleaned text with newline characters removed and multiple spaces reduced to a single space.
    """
    # Use regex to replace one or more whitespace characters (including spaces, tabs, and newlines)
    # with a single space, and then strip leading and trailing whitespace from the result.
    cleaned_text = re.sub(r'\s+', ' ', text).strip()
    return cleaned_text

def split_into_segments(sentence, limit = 200, backtrack_limit = 100):
    """
    Splits a long sentence into multiple smaller segments based on specified limits, ensuring
    segments end with complete sentences where possible.
    
    Parameters:
    - sentence (str): The long sentence to split.
    - limit (int): The approximate limit for the number of words in each segment.
    - backtrack_limit (int): The maximum number of words to backtrack in an effort to end a segment with complete sentences.
    
    Returns:
    - list: A list of sentence segments.
    """
    segments = []
    # Clean the sentence to remove excessive whitespace and newline characters.
    remaining_sentence = clean_text(sentence)
    
    while remaining_sentence:
        # Generate a segment that respects the limit and attempts to end with complete sentences.
        segment = limit_to_approx_words(remaining_sentence, limit, backtrack_limit)
        segments.append(segment)
        # Update the remaining sentence by removing the processed segment and leading spaces.
        remaining_sentence = remaining_sentence[len(segment):].lstrip()
        
        # If there's no remaining sentence to process, exit the loop.
        if not remaining_sentence:
            break
    return segments

def limit_to_approx_words(sentence, limit=200, backtrack_limit=100):
    """
    Truncates a sentence to a specified limit of words, attempting to end with a full stop, question mark,
    or exclamation point within a backtrack limit if possible.
    
    Parameters:
    - sentence (str): The sentence to truncate.
    - limit (int, optional): The maximum number of words desired in the truncated sentence. Defaults to 200.
    - backtrack_limit (int, optional): The maximum number of words to backtrack through to find a suitable
      ending punctuation. Defaults to 100.
    
    Returns:
    - str: The truncated sentence, ideally ending with a complete sentence.
    """
    words = sentence.split()
    if len(words) <= limit:
        return sentence
    
    # Join words up to the limit, then strip to remove any leading or trailing whitespace.
    limited_text = " ".join(words[:limit]).strip()
    # Attempt to find a sentence-ending punctuation within the backtrack limit.
    for i in range(limit - 1, max(0, limit - backtrack_limit), -1):
        if words[i][-1] in ".!?":
            # Return the text up to and including the punctuation.
            return " ".join(words[:i + 1])
    
    # If no suitable punctuation is found, return the text up to the word limit.
    return limited_text




# uses example
# long_sentence_example = """When Asaf-ud-Daula, the fourth Nawab of Awadh (state rulers of the area now known as Uttar Pradesh), shifted the state capital from Faizabad to Lucknow in 1775, it led to a cultural renaissance. An exodus of architects and craftsmen landed there from Delhi, and many other poets, artists and learned men from all around made Lucknow their home. It is said that artisans from as far as the Uzbekistan capital Tashkent, and masons from Isfahan in Iran, were brought to Lucknow by the Persian Nawabs.
# One of the important crafts of Uttar Pradesh is Chikankari, which entails delicate and traditional hand embroidery. This form of handicrafts is mainly practiced in Lucknow. It is done on fabrics like chiffon, muslin, organza, organdie and silk. Chikan saris and Kurtas which are the perfect summer wear. 
# """
    
# split_sentences = split_into_segments(long_sentence_example)
