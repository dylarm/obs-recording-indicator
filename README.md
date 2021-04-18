# OBS Recording Indicator
An in-stream source toggle for if recording is active or not in OBS Studio

If recording is active, then the specified source is visible.
If recording is not active, then the source is not visible.

## Instructions
If you are using Windows, make sure to have Python 3.6 installed and OBS Studio configured to use it.

1. Download the [latest release](https://github.com/dylarm/obs-recording-indicator/releases/latest)
2. Extract/unzip the archive so you can access `recording-indicator.py`
3. In OBS Studio, go to Tools &#8594; Scripts
4. Click the "+" button to add `recording-indicator.py`

## Current limitations
* Source must be manually added (and positioned) to each scene it will be used it (this may or may not be a limitation?)

## Ideas / Goals / Roadmap
* Have a(n optional) source for when recording is paused
* Have a(n optional) source for when not recording
* Allow the creation/deletion of "default" sources for recording/paused/not recording
    * Maybe a custom location as well? (ambitious)
