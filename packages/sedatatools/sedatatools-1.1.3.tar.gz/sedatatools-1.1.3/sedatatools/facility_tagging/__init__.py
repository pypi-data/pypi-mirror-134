from typing import Literal
import re


def climate_controled_tagging(description_text: str) -> bool:
    """
        Checks the list of words in a check_list and adds a column (indicator) with boolean values.
        :param pricing: dataframe containing pricing data for one week
        :param indicator: name of the column
        :param check_list: list of possible cases where indicator column should be 1
        :return: dataframe containing pricing data for one week and added column (indicator)
        """

    terms = ['climate', 'air condition', 'air cool', 'humid', 'heat', 'central air', 'dehumidified']
    negation_terms = [f'{a} {b}' for a in ['no', 'not'] for b in terms]

    for neg_term in negation_terms:
        if neg_term in description_text.lower():
            return False

    for term in terms:
        if term in description_text.lower():
            return True

    return False


def size_category_tagging(size_text: str) -> Literal["Small", "Medium", "Large"]:
    """
    Categorizes size into small, medium or large based on the area
    :param size_text: string consisting of pricing data
    :return: size category (small, medium or large)
    """

    # checks the format (feet by feet, or a x b, etc.)
    if bool(re.match("[0-9]+.?[0-9]? (foot|feet) by [0-9]+.?[0-9]? f+", size_text)) or bool(
            re.match(r"[0-9]+.?[0-9]?'\s*x\s*[0-9]+.?[0-9]?'", size_text)):
        tmp_dimensions = re.findall("[0-9]+.?[0-9]?", size_text)[:2]
        tmp_dimensions = [d.strip() for d in tmp_dimensions]
        tmp_dimensions = [d.replace("'", "") for d in tmp_dimensions]
    elif bool(re.match(r"[0-9]+.?[0-9]?\s*x\s*[0-9]+.?[0-9]?", size_text)):
        tmp_dimensions = re.split(r'x| \s*', size_text.replace(" x ", "x"))[:2]

    size_sq_ft = float(tmp_dimensions[0]) * float(tmp_dimensions[1])

    if size_sq_ft < 100:
        return "Small"
    elif 100 <= size_sq_ft < 200:
        return "Medium"
    elif 200 <= size_sq_ft < 100000:
        return "Large"
    else:
        raise ValueError(
            f"Something is wrong with the square footage, it's either to big or some other invalid value: {size_sq_ft}")


def properly_format_size(size_text: str) -> str:
    """
    Categorizes size into small, medium or large based on the area
    :param size_text: dataframe consisting of pricing data for one week
    :return: description formatted in a n'xn' format
    """
    """
    Processes the name column (column containing storage unit size) into length and width
    :param pricing: dataframe consisting of pricing data for one week
    :return: length and width of a storage unit
    """

    # checks the format (feet by feet, or a x b, etc.)
    if bool(re.match("[0-9]+.?[0-9]? (foot|feet) by [0-9]+.?[0-9]? f+", size_text)) or bool(
            re.match(r"[0-9]+.?[0-9]?'\s*x\s*[0-9]+.?[0-9]?'", size_text)):
        tmp_dimensions = re.findall("[0-9]+.?[0-9]?", size_text)[:2]
        tmp_dimensions = [d.strip() for d in tmp_dimensions]
        tmp_dimensions = [d.replace("'", "") for d in tmp_dimensions]
    elif bool(re.match(r"[0-9]+.?[0-9]?\s*x\s*[0-9]+.?[0-9]?", size_text)):
        tmp_dimensions = re.split(r'x| \s*', size_text.replace(" x ", "x"))[:2]
    else:
        return 'Unknown'

    return f"{tmp_dimensions[0]}'x{tmp_dimensions[1]}'"


def elevator_access_tagging(description_text: str) -> str:
    terms = ['elevator', 'lift']
    negation_terms = [f'{a} {b}' for a in ['no', 'not'] for b in terms]

    for neg_term in negation_terms:
        if neg_term in description_text.lower():
            return False

    for term in terms:
        if term in description_text.lower():
            return True

    return False


def ground_floor_tagging(description_text: str) -> str:
    terms = ['1st floor', 'ground level']
    negation_terms = [f'{a} {b}' for a in ['no', 'not'] for b in terms]

    for neg_term in negation_terms:
        if neg_term in description_text.lower():
            return False

    for term in terms:
        if term in description_text.lower():
            return True

    return False


def drive_up_tagging(description_text: str) -> bool:
    terms = ['drive-up', 'drive up', 'covered loading area/indoor access', 'loading bay access']
    negation_terms = [f'{a} {b}' for a in ['no', 'not'] for b in terms]

    for neg_term in negation_terms:
        if neg_term in description_text.lower():
            return False

    for term in terms:
        if term in description_text.lower():
            return True

    return False


def check_special_case_tagging(description_text: str) -> str:
    """
    Flags every storage unit considered a special case (e.g. storage has no dimensions, wine/vehicle storage, etc.)
    :param pricing: dataframe consisting of pricing data for one week
    :return: special case type or nan for regular storage units
    """
    vehicles = ['boat', 'motorcycle', 'car', 'vehicle', 'parking']

    if isinstance(description_text, float):
        raise TypeError('Input must be text description.')
    elif "wine" in description_text.lower():
        return "Wine Storage"
    elif "parking" in description_text.lower() or "RV" in description_text or any(
            v in description_text.lower() for v in vehicles):
        return "Vehicle Storage"
    elif "locker" in description_text.lower():
        return "Locker"
    elif "mailbox" in description_text.lower():
        return "Mailbox"

    return ''
