# Discord profile picture & banner generator

<strong><img src=".readme/warning.svg" height="42px" alt="⚠ Setting a banner requires nitro"></strong>

A script to generate a profile picture and a banner that show the same image on Discord.

<p align="center">
    <img src=".readme/screenshot.png">
</p>

## Discontinued

As Discord modified their interface, the project doesn’t work anymore. Plus, reproducing its behaviour for current versions would require different configurations for different places − i.e. profile popup, profile page, those on mobile devices… Therefore, the project is now deprecated.

## Installation / Update

### With pip *(recommended)*

```
pip install --upgrade git+https://github.com/victorbnl/discord-pfp-banner-generator.git
```

And make sure your python scripts directory<sup>[<a href="#footnotes-1">1</a>]</sup> is in your path (pip should warn you if it's not anyway).

### Without pip

Clone this repo, install the dependencies with `pip install -r requirements.txt`, and run the following commands in the repo directory, replacing the command `discord_pfp_banner_generator` of the usage section by `python3 discord_pfp_banner_generator`.

## Usage

### Cli

```
discord_pfp_banner_generator image.(png|jpg|anything)
```

Both `banner.png` and `profile-picture.png` are now written in the current directory!

### Module

```python
import discord_pfp_banner_generator

im = Image.load("image.(png|jpg|anything)")
banner, pfp = discord_pfp_banner_generator.process(im)

banner.save("banner.png", "PNG")
pfp.save("pfp.png", "PNG")
```

## Footnotes

1. <span id="footnotes-1"></span>To get your python script paths, run `python3 -c "print(__import__('sysconfig').get_path('scripts', __import__('os').name+'_user'))"` (replace `python3` by `py` on Windows)
