from distutils.core import setup
setup(
    name='MCx32_Enhance',         # How you named your package folder (MyLib)
    packages=['MCx32_Enhance'],   # Chose the same as "name"
    version='0.2',      # Start with a small number and increase it with every change you make
    # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    license='MIT',
    # Give a short description about your library
    description='A solution to resize minecraft textures from x16 to x32. Assists with the conversion of assets between modpacks/resourcepacks.',
    author='James Kelsey',                   # Type in your name
    author_email='jamesmskelsey@gmail.com',      # Type in your E-Mail
    # Provide either the link to your github or to your website
    url='https://github.com/jamesmskelsey/MCx32_Enhance',
    # I explain this later on
    download_url='https://github.com/jamesmskelsey/MCx32_Enhance/archive/refs/tags/v_02.tar.gz',
    # Keywords that define your package best
    keywords=['MINECRAFT', 'TEXTURES', 'CONVERT'],
    install_requires=[            # I get to this in a second
        'Pillow',
    ],
    classifiers=[
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Development Status :: 3 - Alpha',
        # Define that your audience are developers
        'Intended Audience :: Developers',
        'Topic :: Games/Entertainment :: Role-Playing',
        'License :: OSI Approved :: MIT License',   # Again, pick a license
        # Specify which pyhton versions that you want to support
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
)
