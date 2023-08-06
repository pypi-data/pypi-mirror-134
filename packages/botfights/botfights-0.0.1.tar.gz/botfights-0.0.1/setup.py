#!/usr/bin/env python

import setuptools

setuptools.setup(
    name="botfights",
    install_requires=["fire", "requests"],
    packages=setuptools.find_packages("src"),
    package_dir={"": "src"},
    include_package_data=True,
    entry_points={
        "console_scripts": ["fight = botfights:main"],
        "botfights.wordle.guesser": [
            "sample = botfights.wordle.sample_bot:Bot",
            "assisted = botfights.wordle.wordle:Assisted",
        ],
    },
)
