import os
import sys

import launch
import launch_ros.actions
from .await_commands.launch import get_launch_actions as get_await_commands_launch_actions


def get_launch_actions():
    launch_actions = []
    launch_actions += get_await_commands_launch_actions()
    return launch_actions


def generate_launch_description():
    ld = launch.LaunchDescription(get_launch_actions())
    return ld


if __name__ == '__main__':
    generate_launch_description()
