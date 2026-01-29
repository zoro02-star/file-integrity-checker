```git clone repo```

```edit code add your webhook (variable name "DISCORD_WEBHOOK_URL" ) in watcher.py```

```create monitor folder in file-integrity-checker folder```

commands :

```python3 baseline_create.py```

```python3 watcher.py```

done!

options:
to run in background

```nohup python3 watcher.py &```

auto run on start

```cron -e```

```@reboot python3 /full/path/to/watcher.py```


