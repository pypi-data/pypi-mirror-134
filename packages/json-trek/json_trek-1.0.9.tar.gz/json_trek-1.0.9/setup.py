from setuptools import setup, find_packages

with open("README.md") as readme:
    long_description = readme.read()

setup(
    name="json_trek",
    version="1.0.9",
    description="Generate fake JSON user data and lorem ipsum with a Star Trek theme.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Keegan Good",
    author_email="keegood8@gmail.com",
    packages=find_packages(),
    package_data={'': ['json/*.json']},
    include_package_data=True,
    py_modules=['main'],
    python_requires=">=3.6",
    install_requires=[
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Topic :: Utilities",
        "Operating System :: OS Independent",
    ],
    license='MIT',
    project_urls={
        'Source': 'https://github.com/perennialAutodidact/json_trek'
    },
)
