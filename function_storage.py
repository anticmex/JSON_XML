def line_description(line):
    return line.find("description").text.split(" ")

def get_sorted_set(element, dictionary):
    if len(element) > 6:
        if element.lower() in dictionary:
            dictionary[element.lower()] += 1
        else:
            dictionary[element.lower()] = 1
    return dictionary

def watch_result(dictionary, import_set):
    counter = 0
    for n, repeated_counter in enumerate(import_set):
        for key, val in dictionary.items():
            if repeated_counter == val and counter < 10:
                print(f'Слово "{key}" встречается в тексте - {repeated_counter} раз.')
                counter += 1