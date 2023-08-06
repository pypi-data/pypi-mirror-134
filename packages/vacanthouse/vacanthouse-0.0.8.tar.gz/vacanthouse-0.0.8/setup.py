import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="vacanthouse",
    version="0.0.8",
    author="FengtongLi",
    author_email="s1922077@stu.musashino-u.ac.jp",
    description="A package for analysing vacant house rates and population in the United States and Japan.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Lifengtong1/vacancy_rate_and_population_in_JP_and_USA",
    project_urls={
        "Bug Tracker": "https://github.com/Lifengtong1/vacancy_rate_and_population_in_JP_and_USA",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    py_modules=['vacanthouse'],
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    entry_points = {
        'console_scripts': [
            'vacanthouse = vacanthouse:main'
        ]
    },
)