import os
import codecs
from setuptools import setup


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return codecs.open(file_path, encoding='utf-8').read()


setup(
    name='pytest-mock-server',
    version='0.3.0',
    author='Andrey Ermilov',
    author_email='andrerm@ya.ru',
    maintainer='Andrey Ermilov',
    maintainer_email='andrerm@ya.ru',
    license='MIT',
    url='https://github.com/AndreyErmilov/pytest-mock-server',
    description='Mock server plugin for pytest',
    long_description=read('README.rst'),
    py_modules=['pytest_mock_server'],
    python_requires='>=3.0',
    install_requires=['pytest>=3.5.0', 'flask>=1.0'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Pytest',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
    ],
    entry_points={
        'pytest11': [
            'mock-server = pytest_mock_server',
        ],
    },
)
