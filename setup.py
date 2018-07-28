from setuptools import setup


setup(
    name='slacker-asyncio',
    version='0.9.61',
    packages=['slacker'],
    description='Slack API asyncio client based on os\'s slacker',
    author='gfreezy',
    author_email='gfreezy@gmail.com',
    url='http://github.com/gfreezy/slacker-asyncio/',
    install_requires=['aiohttp ~= 3.3'],
    license='http://www.apache.org/licenses/LICENSE-2.0',
    test_suite='tests',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='slack api asyncio'
)
