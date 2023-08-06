from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='lunarcrushed',
    version='0.1.2',

    description="Generate an API key for LunarCRUSH.",
    long_description=long_description,
    long_description_content_type="text/markdown",

    url='https://github.com/nouun/lunarcrushed',

    author='nouun',
    author_email='me@nouun.dev',

    license='GNU 3.0 or later',

    keywords='api lunarcrush trading crypto bitcoin altcoin',

    packages=find_packages(),

    install_requires=[
        'requests',
    ],
)
