import os
import shutil


def submit():
    os.system('python setup.py sdist bdist_wheel')
    os.system('twine upload dist/*')
    shutil.rmtree('dist')
    shutil.rmtree('build')
    shutil.rmtree('sphinx_inplace.egg-info')


if __name__ == '__main__':
    submit()
