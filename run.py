import csv
import itertools
import sys
from typing import NoReturn
import yaml

try:
    from yaml import CLoader as YAMLLoader, CDumper as YAMLDumper
except ImportError:
    from yaml import Loader as YAMLLoader, Dumper as YAMLDumper


def main() -> NoReturn:
    separator = '→'
    data = yaml.load(sys.stdin, Loader=YAMLLoader)

    columns = data.keys()
    rows = itertools.product(*data.values())

    writer = csv.writer(sys.stdout)
    writer.writerow(['id', *columns])

    for row_number, row in enumerate(rows, start=1):
        writer.writerow([row_number, *row])


if __name__ == '__main__':
    main()
