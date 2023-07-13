"""
Helper Module to make directory to save output file.

"""
from __future__ import annotations

import os
from itertools import zip_longest
from os.path import dirname


def make_output_directory(prompt_id: str | None):
    # define save directory
    project_root = dirname(dirname(dirname(dirname(__file__))))      # larger than model directory. 아마 DataBase의 위치가 될 것!!
    
    chart_save_dir = os.path.join(project_root, "output", prompt_id)

    if not os.path.exists(chart_save_dir):
        os.makedirs(chart_save_dir)