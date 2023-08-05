import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="smtp_mailer_nerdler",
    version="0.0.2",
    author="Nerdler",
    author_email="pip@nerdler.tech",
    description="SMTP Mailer classes",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nerdlertech/smtp_mailer",
    project_urls={
        "Bug Tracker": "https://github.com/nerdlertech/smtp_mailer/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.9",
)