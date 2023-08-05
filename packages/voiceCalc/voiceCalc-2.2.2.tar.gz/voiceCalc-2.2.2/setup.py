import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="voiceCalc", # Replace with your own username
    version="2.2.2",
    author="Deo Krishna",
    author_email="deo2k09@gmail.com",
    description="A simple calculator but controlled by voice.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['SpeechRecognition','pyaudio','VCIBD2'],
    python_requires='>=3.10',
)