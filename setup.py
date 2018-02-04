from setuptools import setup

setup(
    name='MakeAboveMeme',
    version='0.4',
    packages=['mAm',],
    description="Use the commandline to create a simple text-above-image meme in the stlye of 9gag posts",
    long_description=open('README.md').read(),
    author = 'Eric Mink aka LucidBrot',
    author_email = 'eric@mink.li',
    url = 'https://github.com/lucidBrot/MakeAboveMeme',
    install_requires=[
        'webkit2png'
    ],
    zip_safe=False
) # docopt is not required because it is self-contained in this distribution
