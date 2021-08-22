#!/usr/bin/env python3
#-*- coding: utf-8 -*-

from distutils.core import setup

setup(
    name='Discord pp banner generator',
    description='A script to generate a profile picture and a banner that show the same image on Discord',
    author='Victor B',
    author_email='victor.bonnelle@protonmail.com',
    url='https://github.com/victorbnl/discord-pp-banner-generator/',
    packages=[
        'discord_pp_banner_generator'
    ],
    entry_points={
        'console_scripts': [
            'discord_pp_banner_generator = discord_pp_banner_generator.__main__:cli'
        ]
    },
    install_requires=[
        'pillow'
    ]
)
