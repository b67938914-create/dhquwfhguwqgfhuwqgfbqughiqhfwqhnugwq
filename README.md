# Discord KeyAuth Bot

A Discord bot for managing authentication keys with HWID tracking and customer support features.

## Features

- Generate authentication keys for users
- Track key usage and expiration
- HWID (Hardware ID) management
- Customer support interface with buttons
- Key reset functionality with cooldowns

## Commands

- `!genkey @user <duration>` - Generate a key for a user
- `!listkeys` - Update the keys display
- `!deletekey <key>` - Delete a specific key
- `!mykeys` - Show your keys
- `!customerreset <key>` - Reset HWID for your key

## Deployment

This bot is configured to run on Render.com with the following files:
- `bot.py` - Main bot code
- `requirements.txt` - Python dependencies
- `render.yaml` - Render deployment configuration

## Environment Variables

- `BOT_TOKEN` - Your Discord bot token