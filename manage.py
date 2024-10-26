#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "syndio.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    # Get the port from the environment variable, defaulting to 8000 if not set
    port = os.getenv("DJANGO_PORT", "8000")

    # Check if the user is attempting to run the server and include the port
    if len(sys.argv) == 1 or (len(sys.argv) >= 2 and sys.argv[1] == "runserver"):
        sys.argv = ["manage.py", "runserver", f"127.0.0.1:{port}"]

    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
