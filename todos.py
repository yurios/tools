#!/usr/bin/env python3

import subprocess
import sys
from typing import List


def get_added_lines(branch: str) -> List[str]:
    try:
        git_command = ['git', 'diff', branch]
        diff_output = subprocess.check_output(git_command, universal_newlines=True)
        diff_lines = diff_output.split('\n')
        for line in diff_lines:
            if not line.startswith('+'):
                continue
            yield line
    except subprocess.CalledProcessError as e:
        print(f"Error running git diff: {e}")


def get_todos(branch: str, todo_type: str) -> List[str]:
    added_lines = get_added_lines(branch)
    todo_type_lower = todo_type.lower()
    for added_line in added_lines:
        added_line_lower = added_line.lower()
        if todo_type_lower not in added_line_lower:
            continue
        todo_index = added_line_lower.index(todo_type_lower)
        yield added_line[todo_index:]


def get_arg(index: int, default: str) -> str:
    if len(sys.argv) > index:
        return sys.argv[index]
    return default


def main():
    branch = get_arg(1, 'origin/master')
    todo_type = get_arg(2, 'todo')
    all_todos = [todo for todo in get_todos(branch, todo_type)]
    all_todos.sort()
    for todo in all_todos:
        print(todo)


if __name__ == "__main__":
    main()
