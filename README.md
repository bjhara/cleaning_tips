# Cleaning Tips

A silly little utility to help us clean the house. Uses the excellent service
ntfy.sh to send notifications.

Uses UV to manage the Python project. To get started run:

```
uv sync
source .venv/bin/activate # or .venv\Scripts\activate for PowerShell
echo 'some-topic-name-for-ntfy' > .topic
uv run main.py
```

It is supposed to be run by cron or similar service.
