# fallout-pnp-character-creator
A tool to create and edit fallout pen and paper characters.

## Prerequisites

This application requires `python3` in this case 3.4 because `pyqt` 
depends on this. You need the following packages to run the application:

```
pyqt5
```

## Setup

For using the provided icon pack, you must run first:

``pyrcc5 -o ./character-creator/oxygen_rc.py 
./character-creator/resources/icons/oxygen.qrc``

Then you can start the application with:

``python3 main.py``
