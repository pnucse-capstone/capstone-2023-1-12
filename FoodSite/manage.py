#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'foodsite.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

    # import os   
    # from django.conf import settings
    # import pandas as pd

    # # 지정된 상대 경로의 data.xlsx 파일을 읽어서 DataFrame으로 가져옴
    # file_name = 'data/data.xlsx'
    # file_path = os.path.join(settings.BASE_DIR, file_name)

    # data = pd.read_excel(file_path)

    # for index, row in data.iterrows():
    #     print(index, row['개방서비스명'])
    #     if index > 10:
    #         break