import setuptools

with open("README.md", "r") as fh:
  long_description = fh.read()

setuptools.setup(
  name="Addons-Tkinter",  # Replace with your username

  version="0.1",

  author="Omer Yelin",

  author_email="pipforcmd@gmail.com",

  description="Addons-tkinter gives you everything you need for tkinter. Made by the creator of Pip-for-CMD.",

  long_description=long_description,

  long_description_content_type="text/markdown",

  url="https://github.com/OmerYelin/Addons-Tkinter",

  packages=setuptools.find_packages(),

  classifiers=[

    "Programming Language :: Python :: 3",

    "License :: OSI Approved :: MIT License",

    "Operating System :: OS Independent",

  ],

  python_requires='>=3',

)