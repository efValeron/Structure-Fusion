import os
from tkinter import filedialog as fd

import pyperclip


def read_file(path: str) -> str:
  try:
    with open(path) as file:
      return file.read()
  except Exception as e:
    return f'Cannot open {path}! Skipping due to error: {e}'


def format_file_content(file_name: str, content: str) -> str:
  header = f'{" ↓ " + os.path.basename(file_name) + " ↓ ":=^40}'
  footer = f'{" ↑ " + os.path.basename(file_name) + " ↑ ":=^40}'
  return '\n'.join([header, content, footer])


def main() -> None:
  root_dir = fd.askdirectory()

  ignored_files = set()
  ignored_directories = set()

  file_paths = [
    os.path.join(root_dir, file_name)
    for file_name in os.listdir(root_dir)
    if file_name not in ignored_files
       and file_name not in ignored_directories
       and os.path.isfile(os.path.join(root_dir, file_name))
  ]

  contents = [read_file(file_path) for file_path in file_paths if read_file(file_path)]

  formatted_contents = [
    format_file_content(file_name, content)
    for file_name, content in zip(file_paths, contents)
  ]

  final_content = '\n\n'.join(formatted_contents)

  pyperclip.copy(final_content)


if __name__ == '__main__':
  main()
