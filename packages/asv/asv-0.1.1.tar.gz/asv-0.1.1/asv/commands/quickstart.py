# -*- coding: utf-8 -*-
# Licensed under a 3-clause BSD style license - see LICENSE.rst

from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import os
import shutil

from . import Command
from ..console import log


class Quickstart(Command):
    @classmethod
    def setup_arguments(cls, subparsers):
        parser = subparsers.add_parser(
            "quickstart", help="Create a new benchmarking suite",
            description="Creates a new bechmarking suite")

        parser.add_argument(
            "--dest", "-d", default=".",
            help="The destination directory for the new benchmarking "
            "suite")

        parser.set_defaults(func=cls.run_from_args)

        return parser

    @classmethod
    def run_from_args(cls, args):
        return cls.run(dest=args.dest)

    @classmethod
    def run(cls, dest="."):
        template_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), '..', 'template')
        for entry in os.listdir(template_path):
            path = os.path.join(template_path, entry)
            dest_path = os.path.join(dest, entry)
            if os.path.exists(dest_path):
                log.info("Template content already exists.")
                log.info("Edit asv.conf.json to continue.")
                return 1

        for entry in os.listdir(template_path):
            path = os.path.join(template_path, entry)
            dest_path = os.path.join(dest, entry)
            if os.path.isdir(path):
                shutil.copytree(path, os.path.join(dest, entry))
            elif os.path.isfile(path):
                shutil.copyfile(path, os.path.join(dest, entry))

        log.info("Edit asv.conf.json to get started.")
