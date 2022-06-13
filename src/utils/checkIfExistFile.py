from pathlib import Path

def checkIfExistFile(filePath):
    fileObj = Path(filePath)
    return fileObj.is_file()