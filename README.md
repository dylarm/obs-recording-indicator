# obs-recording-indicator
An in-stream source toggle for if recording is active or not

If recording is active, then the specified source is visible.
If recording is not active, then the source is not visible.

## Current limitations
* Source visibility is only changed _after_ a scene transition. Depending on the transition, this can be strange
* Source must be manually added (and positioned) to each scene it will be used it (this may or may not be a limitation?)
