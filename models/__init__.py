#!/usr/bin/python3
"""Creates unique instance of  FileStorage for the project"""
from models.engine.file_storage import FileStorage

"""Variable storage for FileStorage instance"""
storage = FileStorage()
storage.reload()
