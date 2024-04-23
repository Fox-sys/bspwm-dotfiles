from src.adapters.user_interfaces import InstallInterface
import argparse
import os

print(os.environ.get('PYTHONPATH'))


def main():
    interface = InstallInterface()
    interface.start()


if __name__ == '__main__':
    main()
