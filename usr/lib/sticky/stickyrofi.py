#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import stickycli
from types import SimpleNamespace


def step_1_called_by_rofi():
    for group in stickycli.call_dbus_with(command='group list'):
        print(group)


def step_2_option_chosen(group_name):
    for group in stickycli.call_dbus_with(command='group list'):
        if group == group_name:
            stickycli.call_dbus_with(command='group change', group_name=group_name)
            sys.exit(0)

    else:
        print(f'Group {group_name} not found...')
        sys.exit(1)


def main():
    if len(sys.argv) == 1:
        step_1_called_by_rofi()
    else:
        step_2_option_chosen(sys.argv[1])

if __name__ == '__main__':
    main()
