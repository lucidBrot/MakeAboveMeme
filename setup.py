from setuptools import setup

setup(
    name='MakeAboveMeme',
    version='0.5.4',
    packages=['mAm',],
    description="Use the commandline to create a simple text-above-image meme in the stlye of 9gag posts",
    long_description=open('readme.txt').read(),
    author = 'Eric Mink aka LucidBrot',
    author_email = 'eric@mink.li',
    url = 'https://github.com/lucidBrot/MakeAboveMeme',
    install_requires=[
        'webkit2png'
    ],
    zip_safe=False,
    scripts=['bin/makeAboveMeme'],
    package_data = {'mAm':['mAm/mam.css', 'mam/mam.html', 'data/*']},
    include_package_data=True
) # docopt is not required because it is self-contained in this distribution
