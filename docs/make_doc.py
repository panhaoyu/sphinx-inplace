"""
This file defines how to build the documentation, including the location of rst directory and files need to be excluded.
"""

import os
import sys
from os import path

from sphinx.application import Sphinx

from sphinx_inplace import RstGenerator
from sphinx_inplace.file_tree import PythonFileTreeNode


def main():
    base = os.path.dirname(os.path.dirname(__file__))

    source_dir = path.join(base, 'docs', 'source')
    rst_root_dir = path.join(base, 'docs', 'build', 'rst')
    path.exists(rst_root_dir) or os.makedirs(rst_root_dir)

    generator = RstGenerator()

    generator.sync_directory(source_dir, rst_root_dir, rm=False)

    # Generate documentations of main directory
    py_dir = os.path.join(base, 'sphinx_inplace')  # python directory
    rst_dir = os.path.join(rst_root_dir, 'sphinx_inplace')  # rst directory
    exclude_dir = [os.path.join(py_dir, p) for p in (
        # The parts that need to be skipped can list here.
        'nothing/nothing.py',
    )]
    node = PythonFileTreeNode(py_dir, exclude_dir)
    generator.generate_python_package_files(node, rst_dir, 'sphinx_inplace')

    # We can generate more directories
    # py_dir = os.path.join(base, 'sphinx_inplace')  # python directory
    # rst_dir = os.path.join(rst_root_dir, 'sphinx_inplace_bak')  # rst directory
    # exclude_dir = [os.path.join(py_dir, p) for p in (
    #     # The parts that need to be skipped can list here.
    #     'nothing/nothing.py',
    # )]
    # node = PythonFileTreeNode(py_dir, exclude_dir)
    # generator.generate_python_package_files(node, rst_dir, 'sphinx_inplace')

    app = Sphinx(
        srcdir=rst_root_dir,
        confdir=rst_root_dir,
        outdir=path.join(path.dirname(__file__), 'build/html'),
        doctreedir=path.join(path.dirname(__file__), 'build/doctrees'),
        buildername='html',
        confoverrides=dict(),
        status=sys.stdout,
        warning=sys.stderr,
        freshenv=False,
        warningiserror=False,
        tags=[],
        verbosity=0,
        parallel=0,
        # parallel=multiprocessing.cpu_count(),
        keep_going=True)
    app.build()


if __name__ == '__main__':
    main()
