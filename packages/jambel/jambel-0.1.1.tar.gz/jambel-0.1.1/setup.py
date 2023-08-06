from setuptools import setup
import os

setup(
    name='jambel',
    version='0.1.1',
    py_modules=['jambel'],
    url='http://github.com/jambit/python-jambel',
    license='MIT',
    author='Sebastian Rahlf',
    author_email='sebastian.rahlf@jambit.com',
    description="Interface to jambit's project traffic lights.",
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.rst')).read(),
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'jambel = jambel:main',
        ]
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: Other/Proprietary License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ]
)
