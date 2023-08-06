from setuptools import setup, find_packages
 
# classifiers = [
#   'Development Status :: 5 - Production/Stable',
#   'Intended Audience :: Education',
#   'Operating System :: Microsoft :: Windows :: Windows 10',
#   'License :: OSI Approved :: MIT License',
#   'Programming Language :: Python :: 3.9'
# ]
 
setup(
    name = "kalulatar",
    version = "0.0.1",
    author = "Dylan",
    author_email = "dylansugito@gmail.com",
    description = ("awesome calculator"),
    license = "MIT",
    keywords = "Calculator",
    url = "",
    packages=find_packages(),
    long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Education',
        'Operating System :: Microsoft :: Windows :: Windows 10',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3'
    ],
    install_requires=[]
)