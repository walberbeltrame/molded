import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name="thoaded",  
     version="0.0.8",
     py_modules=["thoaded"],
     author="Walber Antonio Ramos Beltrame",
     author_email="walber.beltrame@gmail.com",
     description="The source for a library for simple and fast design pattern that extends model, view and controller for asynchronous events in supported modern programming languages.",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://walberbeltrame.github.io/thoaded/",
     license="MIT",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )