import re


def extract_url_from_style(value):
    match = re.search(r'url\("(.*?)"\)', value)
    return match.group(1) if match else value


def convert_arabic_number_to_english(input_string):
    persian_to_english_mapping = {
        '۰': '0',
        '۱': '1',
        '۲': '2',
        '۳': '3',
        '۴': '4',
        '۵': '5',
        '۶': '6',
        '۷': '7',
        '۸': '8',
        '۹': '9',
        '٫': '.',
    }

    return ''.join(persian_to_english_mapping.get(char, char) for char in input_string)


def clean_rated_value(raw_rate):
    raw_rate = convert_arabic_number_to_english(raw_rate)
    # Use regular expression to extract the rating
    match = re.search(r"(\d+(\.\d+)?) out of 5", raw_rate)
    return float(match.group(1)) if match else raw_rate
