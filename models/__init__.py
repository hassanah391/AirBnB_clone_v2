#!/usr/bin/python3
"""init file for package"""
from engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
