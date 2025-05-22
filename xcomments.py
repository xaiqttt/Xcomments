#!/usr/bin/env python3
import re
import argparse
import os
from pyfiglet import figlet_format
from shutil import copyfile

def remove_comments(content, file_type):
    if file_type == 'html':
        return re.sub(r'<!--.*?-->', '', content, flags=re.DOTALL)

    elif file_type == 'css':
        return re.sub(r'/\*.*?\*/', '', content, flags=re.DOTALL)

    elif file_type == 'js':
        content = re.sub(r'/\*.*?\*/', '', content, flags=re.DOTALL)
        return re.sub(r'//.*', '', content)

    elif file_type in ['python', 'bash']:
        return re.sub(r'#.*', '', content)

    elif file_type in ['c', 'cpp', 'java']:
        content = re.sub(r'/\*.*?\*/', '', content, flags=re.DOTALL)
        return re.sub(r'//.*', '', content)

    elif file_type == 'php':
        content = re.sub(r'/\*.*?\*/', '', content, flags=re.DOTALL)
        content = re.sub(r'//.*', '', content)
        return re.sub(r'#.*', '', content)

    elif file_type == 'hybrid':
        content = re.sub(r'<!--.*?-->', '', content, flags=re.DOTALL)
        content = re.sub(
            r'(<style[^>]*>)(.*?)(</style>)',
            lambda m: m.group(1) + re.sub(r'/\*.*?\*/', '', m.group(2), flags=re.DOTALL) + m.group(3),
            content, flags=re.DOTALL | re.IGNORECASE
        )
        content = re.sub(
            r'(<script[^>]*>)(.*?)(</script>)',
            lambda m: m.group(1) +
                      re.sub(r'/\*.*?\*/', '', re.sub(r'//.*', '', m.group(2)), flags=re.DOTALL) +
                      m.group(3),
            content, flags=re.DOTALL | re.IGNORECASE
        )
        return content

    else:
        raise ValueError("Unsupported file type.")

def main():
    print(figlet_format("Xcomments"))

    parser = argparse.ArgumentParser(
        description="Xcomments - Remove all comments from source code files.",
        epilog="Example: Xcomments -fp myfile.js -ft js --backup"
    )
    parser.add_argument('-fp', '--file-path', required=True, help='Path to the file')
    parser.add_argument('-ft', '--file-type', required=True,
                        choices=['html', 'css', 'js', 'python', 'bash', 'c', 'cpp', 'java', 'php', 'hybrid'],
                        help='File type')
    parser.add_argument('--backup', action='store_true', help='Create a backup of the file')

    args = parser.parse_args()
    path = args.file_path
    file_type = args.file_type.lower()

    if not os.path.isfile(path):
        print("File not found.")
        return

    try:
        if args.backup:
            backup_path = path + '.bak'
            copyfile(path, backup_path)
            print(f"Backup created: {backup_path}")

        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()

        cleaned = remove_comments(content, file_type)

        with open(path, 'w', encoding='utf-8') as f:
            f.write(cleaned)

        print("Comments removed successfully.")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
