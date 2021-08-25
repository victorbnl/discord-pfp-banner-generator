#!/usr/bin/env python3
#-*- coding: utf-8 -*-

from distutils.core import setup
import os

setup(
    name='discord-pfp-banner-generator',
    description='A script to generate a profile picture and a banner that show the same image on Discord',
    author='Victor B',
    author_email='victor.bonnelle@protonmail.com',
    url='https://github.com/victorbnl/discord-pfp-banner-generator/',
    packages=[
        'discord_pfp_banner_generator'
    ],
    entry_points={
        'console_scripts': [
            'discord_pfp_banner_generator = discord_pfp_banner_generator.__main__:cli'
        ]
    },
    include_package_data=True,
    data_files=[
        "discord_pfp_banner_generator/positions.yml"
    ],
    install_requires=[
        'pillow',
        'requests',
        'PyYAML'
    ]
)
