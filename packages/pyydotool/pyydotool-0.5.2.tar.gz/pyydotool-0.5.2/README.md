# PyYdotool

Python bindings for [`ydotool`](https://github.com/ReimuNotMoe/ydotool)

This project was inspired by [pyxdotool](https://github.com/cphyc/pyxdotool)

All `ydotool` commands are chainable.

# Example
```python
from ydotool import YdoTool
ydo = YdoTool().key("ctrl+alt+f1")
ydo.sleep(2000).type("echo 'foo bar'")
# execution is done here
ydo.exec()
```

# Requirements
Access to `/dev/uinput` device is required. It can be set by adding `udev` rules.<br>
Example tested on Fedora:
#### **`/etc/udev/rules.d/60-uinput.rules`**
```shell
KERNEL=="uinput", SUBSYSTEM=="misc", TAG+="uaccess", OPTIONS+="static_node=uinput"
```

This rules will allow regular user logged in to the machine to access `uinput` device. 