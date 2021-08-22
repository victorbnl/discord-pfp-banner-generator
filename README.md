# Discord profile picture & banner generator

A script to generate a profile picture and a banner that show the same image on Discord

<p align="center">
    <img src=".readme/screenshot.png">
</p>

## Installation

```
pip install --upgrade git+https://github.com/victorbnl/discord-pfp-banner-generator.git
```

And make sure your python scripts directory is in your path (pip should warn you if it's not anyway).

## Usage

<strong><img src="https://user-images.githubusercontent.com/39555268/130364433-8e2d0fda-2ec6-4233-b7f9-ab57fd50ad1d.png" height="42px" alt="⚠ Setting a banner requires nitro"></strong>

### Cli

```
discord_pfp_banner_generator image.(png|jpg|anything)
```

Both `banner.png` and `pp.png` are now written in the current directory!

### Module

```python
import discord_pfp_banner_generator

im = Image.load("image.(png|jpg|anything)")
banner, pfp = discord_pfp_banner_generator.process(im)

banner.save("banner.png", "PNG")
pfp.save("pfp.png", "PNG")
```
