from setuptools import setup


setup(
    name='slacker-asyncio',
    version='0.8.7',
    packages=['slacker'],
    description='Slack API client',
    author='gfreezy',
    author_email='gfreezy@gmail.com',
    url='http://github.com/gfreezy/slacker-asyncio/',
    install_requires=['aiohttp==0.21.6'],
    license='http://www.apache.org/licenses/LICENSE-2.0',
    test_suite='tests',
    classifiers=(
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ),
    keywords='slack api asyncio'
)
