# PybricksPythonTut

Pybricks Python tutorial repo for LEGO SPIKE Prime robots, written for kids and FIRST LEGO League teams.

## Where to start

- **First time**: open `1-hub/` and run a light/display/sound program.
- **Next**: `2-motor/` (motors) → `3-drivebase/` (driving) → `7-sensors/` (sensors).
- **Programming skills**: `4-forloop/`, `5-whileloop/`, `6-ifelse/`, then `9-functions/`.

## Repo map (what each folder teaches)

- **`1-hub/`**: hub LED, display, buttons, and sounds
- **`2-motor/`**: controlling one or more motors (speed, angle, time, stall)
- **`3-drivebase/`**: using `DriveBase` to drive straight/turn/curve repeatably
- **`drivebase/`**: extra drivebase example(s) (may overlap with `3-drivebase/`)
- **`4-forloop/`**: `for` loops and lists
- **`5-whileloop/`**: `while` loops and waiting for conditions
- **`6-ifelse/`**: making decisions with `if / elif / else`
- **`7-sensors/`**: distance/color/force/IMU examples and simple “menus”
- **`9-functions/`**: writing your own reusable functions; **`9-functions/lab/`** has short box-bot follow-ups (~30 min total) tied to [`teaching/functions-intro.html`](teaching/functions-intro.html)
- **`teaching/`**: optional browser lesson pages (no robot required), for example [`teaching/functions-intro.html`](teaching/functions-intro.html) — walkthrough + simulator that pairs with `9-functions/` for in-class use. Tap the page if the browser blocks demo sounds.

## How to run a file

Follow the official Pybricks “Getting Started” steps for setup/firmware and the programming environment:

- **Install Pybricks (one-time setup)**: follow [Installing Pybricks](https://pybricks.com/learn/getting-started/install-pybricks).
- **Learn the editor (Pybricks Code)**: see [Creating and running Pybricks programs](https://pybricks.com/learn/getting-started/pybricks-environment).

Then, for this repo:

1. Open [Pybricks Code](https://code.pybricks.com/)
2. Connect to your hub (Bluetooth; first-time firmware install may require USB depending on your hub/computer)
3. Open any `.py` file from this repo (copy/paste or upload into Pybricks Code)
4. Press **Run** to start the program (and **Stop** to stop it)

If a program uses `print(...)`, look at the **output/console** area in Pybricks Code.

## Notes

- Some filenames use dashes (example: `distance-stoprobot.py`). That’s fine to run, but it’s not meant to be imported as a module.
- Programs are intentionally short so kids can read them and then change one thing at a time.
