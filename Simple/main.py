import random
import doctest
from uuid import uuid4

def create_dict_list():
    """
    Creates a dict list of random IDs and ages

    >>> len(create_dict_list())
    10

    """
    random.seed()
    dict_list = []
    for i in range(10):
        dict_list.append({
            'id': str(uuid4()),
            'edad': random.randint(1, 100)
        })
    
    return dict_list


def print_dict_list_id_age(dict_list):
    """
    Sorts a dict list of random IDs and ages by age (from highest to lowest), and prints the max and min ages
    """
    print(max(dict_list, key=lambda person: person['edad'])['id'])
    print(min(dict_list, key=lambda person: person['edad'])['id'])
    sorted_dict_list = sorted(dict_list, key=lambda person: person['edad'], reverse=True)
    return sorted_dict_list

if __name__ == "__main__":
    doctest.testmod()
