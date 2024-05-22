
def main():
    print("Constructed/non-constructed is stuff to be included in __init__")
    num_constructed_attr = int(input("Number of attributes to be constructed: "))
    num_other_attr = int(input("Number of non-constructed attributes: "))
    construct_names = [input("Constructed attribute: ").split() for i in range(num_constructed_attr)]
    other_names = [input("Non-constructed attribute: ").split() for i in range(num_other_attr)]
    construct_cap = list(map(convertCapitalize, construct_names)) # List of attribute names to be constructed, in camel case
    construct_under = list(map(convertUnderscored, construct_names)) # List of attribute names to be constructed, in underscored lower case
    other_cap = list(map(convertCapitalize, other_names)) # List of attribute names not constructed, in camel case
    other_under = list(map(convertUnderscored, other_names)) # List of attribute names not constructed, in underscored lower case

    # Print code
    for i in attributeList(construct_under, other_under):
        print(i)
    for i in constructor(construct_cap, construct_under):
        print(i)
    for i in getters(construct_cap, construct_under, other_cap, other_under):
        print(i)
    for i in setters(construct_cap, construct_under, other_cap, other_under):
        print(i)

def attributeList(construct_under, other_under):
    """
    Returns a list of lines to be printed as part of the attribute list
    """
    attribute_list = ['# Attributes']
    for name in construct_under:
        attribute_list.append(f"__{name} = None")
    for name in other_under:
        attribute_list.append(f"__{name} = ")
    return attribute_list

def constructor(construct_cap, construct_under):
    """
    Returns a list of lines that represent the constructor's code
    """
    constructor_list = ['', '# Constructor']
    constructor_list.append(f"def __init__(self, {', '.join(construct_under)}):") # init function code
    for attr in zip(construct_cap, construct_under):
        constructor_list.append(f"    self.set{attr[0]}({attr[1]})") # setter function for each constructed attribute
    return constructor_list
    
def getters(construct_cap, construct_under, other_cap, other_under):
    """
    Returns a list lines that represent the getters' code
    """
    getter_list = ['', '# Getters']
    for attr in zip(construct_cap, construct_under):
        getter_list.append(f"def get{attr[0]}(self):")
        getter_list.append(f"    return self.__{attr[1]}")
    for attr in zip(other_cap, other_under):
        getter_list.append(f"def get{attr[0]}(self):")
        getter_list.append(f"    return self.__{attr[1]}")
    return getter_list

def setters(construct_cap, construct_under, other_cap, other_under):
    """
    Returns a list lines that represent the setters' code
    """
    setter_list = ['', '# Setters']
    for attr in zip(construct_cap, construct_under):
        setter_list.append(f"def set{attr[0]}(self, {attr[1]}):")
        setter_list.append(f"    self.__{attr[1]} = {attr[1]}")
    for attr in zip(other_cap, other_under):
        setter_list.append(f"def set{attr[0]}(self, {attr[1]}):")
        setter_list.append(f"    self.__{attr[1]} = {attr[1]}")
    return setter_list

def convertCapitalize(word_list):
    """
    Input: list of words, returns string of those words converted to camel case.
    """
    cap_word_list = [word.capitalize() for word in word_list]
    return "".join(cap_word_list)

def convertUnderscored(word_list):
    """
    Input: list of words, returns string of those words converted to lower case and separated by underscores.
    """
    under_word_list = [word.lower() for word in word_list]
    return "_".join(under_word_list)

main()