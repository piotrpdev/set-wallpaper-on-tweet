# Set Wallpaper on Tweet 🖼️

Checks the recent tweets of x user every x seconds, and if a new image has been tweeted, sets the desktop wallpaper to it.

> Note: Only tested/works on Win10

## How to use 📝

* Get Twitter Developer account

* Create project, app, and get the bearer token

* Set `bearer_token` in `secrets-example.py` and rename the file to `secrets.py`

* Install requirements and run `main.py`

  * (Optional) Add a batch script to `shell:startup` with `[python interpreter path] [path to main.py]` to run the script on startup (use pythonw for no gui)