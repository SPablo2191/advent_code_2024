def read_document(file_name : str) -> list[str]:
    """get the data from a file and return it as a list of strings
    how to use it:
    import sys
    sys.path.append("..") 
    from utils import read_document
    Keyword arguments:
    file_name -- string containing the name of the file to read
    Return: list of lines from the file
    """
    
    with open(file_name, "r") as f:
        return f.readlines()
    
