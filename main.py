"""Scheduled Task View — List scheduled tasks, last run, and next run, and export the table."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='scheduled_task_view',
        description='List scheduled tasks, last run, and next run, and export the table.',
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('Scheduled Task View')
    print('Task Scheduler as a table.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
