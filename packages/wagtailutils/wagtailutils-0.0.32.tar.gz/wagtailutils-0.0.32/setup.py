import setuptools

setuptools.setup(
    name="wagtailutils",
    version="0.0.32",
    author="Amir Mubarak, Nayan Biswas, Utsob Roy",
    author_email="amir@co.design, nayan@co.design, roy@co.design",
    description="A Wagtail Utility Package",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "wagtailmenus",
        "djangorestframework",
        "django-json-widget",
    ],
)
