#!/usr/bin/python3
'''
Instantiates Models and creates an instance of FileStorage
Then reloads the stored instances
'''
from models.engine import file_storage

storage = file_storage.FileStorage()
storage.reload()
