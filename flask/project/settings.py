# -*- coding: utf-8 -*-
import os

REPO_NAME = "stellar-tutorials"  # Used for FREEZER_BASE_URL
DEBUG = True

APP_DIR = os.path.dirname(os.path.abspath(__file__))  # Assumes the app is located in the same directory where this file resides

def parent_dir(path):
  '''Return the parent of a directory.'''
  return os.path.abspath(os.path.join(path, os.pardir))

PROJECT_ROOT = parent_dir(APP_DIR)
FREEZER_DESTINATION = PROJECT_ROOT  # In order to deploy to Github pages, you must build the static files to the project root

# FREEZER_BASE_URL = "http://localhost/{}".format(REPO_NAME)  # This is a repo page (not a user page), so we must set the BASE_URL to the correct url as per GH Pages' standards
FREEZER_BASE_URL = "https://github.com/{}".format(REPO_NAME)  # This is a repo page (not a user page), so we must set the BASE_URL to the correct url as per GH Pages' standards

FREEZER_REMOVE_EXTRA_FILES = False  # IMPORTANT: If this is True, all app files will be deleted when you run the freezer
FLATPAGES_MARKDOWN_EXTENSIONS = ['codehilite']
FLATPAGES_ROOT = os.path.join(APP_DIR, 'pages')
FLATPAGES_EXTENSION = '.md'
