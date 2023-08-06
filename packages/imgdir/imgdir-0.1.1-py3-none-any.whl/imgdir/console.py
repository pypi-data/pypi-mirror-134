

def run():
    import argparse
    import os
    import shutil
    from datetime import datetime

    parser = argparse.ArgumentParser()
    parser.add_argument('file', metavar='imagefile', type=str)
    args = parser.parse_args()

    timestamp = os.path.getmtime(args.file)
    date = datetime.fromtimestamp(timestamp)
    isoweek = date.isocalendar()
    target_directory = f'{isoweek.year}-{isoweek.week}'
    os.makedirs(target_directory, exist_ok=True)
    try:
        shutil.move(args.file, target_directory)
    except shutil.Error as e:
        print(e)
