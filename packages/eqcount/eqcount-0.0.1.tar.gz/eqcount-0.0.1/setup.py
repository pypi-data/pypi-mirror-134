from setuptools import setup
from codecs import open
from os import path
package_name = "eqcount"
root_dir = path.abspath(path.dirname(__file__))
# requiwements.txtの中身を読み込む
def _requirements():
    return [name.rstrip() for name in open(path.join(root_dir, 'requirements.txt')).readlines()]
# README.mdをlong_discriptionにするために読み込む
with open('README.md', encoding='utf-8') as f:
    long_description = f.read()
setup(
    name=package_name,
    version='0.0.1',
    description='このライブラリで地震の可視化が可能になります',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Yuki-max/earthquake',
    author='Yuki-max',
    author_email='yuki65763933@gmail.com',
    license='MIT',
    keywords='',
    packages=[package_name],
    install_requires=_requirements(),
    classifiers=[
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)