import subprocess
import argparse
import settings
import json


def create_manifest_file(target):
    data = settings.MANIFEST_FILE

    if target == 'firefox':
        data['browser_specific_settings'] = {
            'gecko': {
                'id': 'gmrle@epoc.fr',
                'strict_min_version': '57.0'
            }
        }

    with open('manifest.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)


def switch(target):
    create_manifest_file(target)


def build(target):
    switch(target)

    arguments = [
        'web-ext',
        'build',
        '--overwrite-dest',
        '--ignore-files',
    ]

    arguments.extend(settings.FILES_AND_DIRECTORIES_TO_IGNORE_WHEN_BUILDING)

    subprocess.run(arguments, shell=True)


def run():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('action', choices=['build', 'switch'])
    arg_parser.add_argument('target', choices=['firefox', 'chrome'])

    args = arg_parser.parse_args()

    if args.action == 'build':
        build(args.target)
    elif args.action == 'switch':
        switch(args.target)

if __name__ == '__main__':
    run()
