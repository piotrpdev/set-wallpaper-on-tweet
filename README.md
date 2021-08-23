# Set Wallpaper on Tweet 🖼️

Checks the recent tweets of x user every x seconds, and if a new image has been tweeted, sets the desktop wallpaper to it.

> Note: Only tested/works on Win10

## How to use 📝

* Get Twitter Developer account

* Create project, app, and get the bearer token

* Set `bearer_token` in `secrets-example.py` and rename the file to `secrets.py`

* Install requirements and run `main.py`

  * (Optional) Add a batch script to `shell:startup` with `[python interpreter path] [path to main.py]` to run the script on startup.

### How to run script on startup [*silently*](https://superuser.com/questions/62525/run-a-batch-file-in-a-completely-hidden-way)

* Create a shortcut in `shell:startup` with this "Location of the item":

```cmd
wscript.exe "[Location of this repo]\invisible.vbs" "[Location of this repo]\startup_script.bat"
```

* Set the location of the repo in `startup_script_example.bat` and rename it to `startup_script.bat`

> To shutdown script, use `taskkill /IM pythonw.exe /F`
