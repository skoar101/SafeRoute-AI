HEAD
"""
Purpose: Django's CLI utility for management tasks (migrations, server, etc.)
"""
import os
import sys
print("Starting manage.py")   # <-- add this

import traceback               # <-- add this
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
"""
Purpose: Django's CLI utility for management tasks (migrations, server, etc.)
"""
import os
import sys
print("Starting manage.py")   # <-- add this

import traceback               # <-- add this
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


#2f55220dae0bb14c7c90517c68fd70ac27d114b2
