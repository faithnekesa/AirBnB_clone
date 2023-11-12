#!/usr/bin/python3
"""Unique FileStorage instance of the project application"""
from models.engine.file_storage import FileStorage

"""Variable storage instance of FileStorage"""
storage = FileStorage()
storage.reload()
