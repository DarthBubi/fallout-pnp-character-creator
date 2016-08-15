# fallout-pnp-character-creator
A tool to create and edit fallout pen and paper characters.

## Prerequisites

This application requires `python3`. On Debian/Ubuntu based
distribution you need the following packages to run the application:


```
pyqt5-dev
pyqt5-dev-tools
python3-pyqt5

```

## Setup

For using the provided icon pack, you must run first:

```
git submodule init
git submodule update
pyrcc5 -o ./character-creator/oxygen_rc.py ./character-creator/resources/icons/oxygen.qrc
```

Then you can run the application with:

``python3 main.py``
