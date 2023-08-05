from setuptools import setup, find_packages


VERSION = '0.0.1'
DESCRIPTION = 'Run shell commands'
LONG_DESCRIPTION = '''
                    Run shell commands without Popen 
                   '''

# Setting up
setup(
    name="magic_run_cmd",
    version=VERSION,
    author="magedavee (Daniel Davee)",
    author_email="<daniel.v.davee@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['pysimplelog'],
    keywords=['python', 'bash'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)