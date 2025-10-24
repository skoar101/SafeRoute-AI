#!/usr/bin/env python
"""
Purpose: Django's CLI utility for management tasks (migrations, server, etc.)
"""
import os
import sys

import traceback
try:
    from django.core.management import execute_from_command_line
except Exception as e:
    print("Error importing Django:", e)
    traceback.print_exc()

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'saferouteai.settings')
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()
