# Serial Port Change

## Introduction

We've all been there; you have a bunch of USB-serial adapters and you have to figure out which serial port it is. Traditionally, I've done this by opening Device Manager, try to remember all the ports connected, unplug the device, and look for changes. There has to be a better way, so `Serial Port Change` to the rescue!

## What it Does

This utility is simplicity itself. It is a command line tool that extracts a set of serial ports, then periodically looks for changes. If a port is added, it will return:

```
New serial port detected: COM12
```

If a port is removed, it will return:

```
Serial port removed: COM12
```

This process will end when the user types CTRL-C.

## How to Run

There are a few ways to run the project. You can install it with Pip:

```sh
$ pip install serial-port-change
```

Then run it with the script (assuming the Python scripts path is in your global path)

```sh
$ serial_port_change
```

If you have [Astral `uv`](https://docs.astral.sh/uv/) installed, you can also run it (without directly installing it) using `uvx` like:

```sh
uvx serial_port_change
```

## Modifying

The project is built using the `uv` package manager, although it could be easily recasted to Poetry or some other package manager. There are also files to set up the project using PyCharm, although this isn't  required.

## Questions

If anyone has any questions, contact me at dbwalker0min@gmail.com.
