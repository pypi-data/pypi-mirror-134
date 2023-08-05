from setuptools import setup

readme = open("./README.md", "r")


setup(
    name='nekoimg',
    packages=['nekoimg'],  # this must be the same as the name above
    version='0.5',
    description='This shows you a random neko image',
    long_description='For more info of the project go to see The github!\nhttps://github.com/Cl1ckerr/nekoimg',
    long_description_content_type='text/markdown',
    author='Cl1cker',
    author_email='tji85047@gmail.com',
    # use the URL to the github repo
    url='https://github.com/Cl1ckerr/nekoimg',
    install_requires=['requests', 'pyautogui', 'requests'],
    download_url='https://github.com/Cl1ckerr/nekoimg/tarball/0.4',
    keywords=['webbrowser', 'random', 'neko'],
    classifiers=[ ],
    license='MIT',
    include_package_data=True
)
