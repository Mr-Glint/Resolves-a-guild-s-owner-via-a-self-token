# discord-scripts

![Python](https://img.shields.io/badge/Language-Python-3776AB?style=flat-square)
![Dependencies](https://img.shields.io/badge/Requires-requests-FF6C8C?style=flat-square)
![License](https://img.shields.io/badge/License-For--research--only-lightgrey?style=flat-square)

> Small, focused Python utilities for working with the Discord API.

A collection of independent Python scripts - each one self-contained, quick to configure, and useful for Discord API experiments and testing.

---

## Scripts

| Script | Purpose |
|--------|---------|
| `discord_server_tools.py` | Resolves a guild's owner via a self-token and fetches the owner's public profile (username, avatar, join date). |
| `webhook_test.py` | Minimal webhook tester - posts a JSON message and prints the HTTP status. |

---

## Requirements

- Python **3.8+**
- `requests` for `discord_server_tools.py`
- `urllib` (standard library) for `webhook_test.py` - no extra install needed

---

## Usage

### `webhook_test.py`

```bash
python webhook_test.py
```

Set the `WEBHOOK` constant at the top of the file to your webhook URL first.

### `discord_server_tools.py`

```bash
python discord_server_tools.py
```

Put a token in the `TOKEN` placeholder and set your target `guild_id` inside the script, then run.

---

## Disclaimer

Self-tokens violate the **Discord Terms of Service**. Using them can result in account termination. These scripts are provided for educational and research purposes only - use at your own risk and within the rules of what you are testing.