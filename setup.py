from setuptools import setup, find_packages
import os

long_description = 'Twitter Tap Timeframe is a python tool that connects to the Twitter API and issues calls to the search or the streaming endpoint using a query that the user has entered. It also stores tweets into TimeFrames.'
if os.path.exists('README.rst'):
    long_description = open('README.md').read()

CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'Intended Audience :: Science/Research',
    'License :: OSI Approved :: MIT License',
    'Topic :: Communications :: Chat',
    'Topic :: Internet',
    'Topic :: Database'
]

dist = setup(
    name='twitter-tap-timeframe',
    version='0.1',
    author='Javi Palanca',
    description='Collect tweets to a mongoDB using either the Twitter search API or the streaming API. Stores tweets into timeframes',
    long_description=long_description,
    author_email='jpalanca@gmail.com',
    url='https://github.com/javipalanca/twitter-tap-timeframe',
    license='MIT',
    install_requires=['pymongo','twython','six'],
    classifiers=CLASSIFIERS,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    entry_points={
        'console_scripts': [
         'tap-timeframe = twitter_tap_timeframe.tap:main',
        ],
    }
)
