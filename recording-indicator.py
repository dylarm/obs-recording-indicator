import obspython as obs

VERSION = "v0.0.2a"


class _G:
    def __init__(self, source_name=None):
        self.source_name = source_name

    def set_visible_all(self, visible):
        scenes = obs.obs_frontend_get_scenes()
        for scene in scenes:
            scene_test = obs.obs_scene_from_source(scene)
            in_scene = obs.obs_scene_find_source(scene_test, self.source_name)
            if in_scene:
                obs.obs_sceneitem_set_visible(in_scene, visible)
        obs.source_list_release(scenes)


g = _G()


def make_visible():
    g.set_visible_all(True)


def make_invisible():
    g.set_visible_all(False)


def script_update(settings):
    g.source_name = obs.obs_data_get_string(settings, "source")


def script_properties():
    props = obs.obs_properties_create()
    p = obs.obs_properties_add_list(
        props,
        "source",
        "Source",
        obs.OBS_COMBO_TYPE_EDITABLE,
        obs.OBS_COMBO_FORMAT_STRING,
    )
    sources = obs.obs_enum_sources()
    if sources is not None:
        for source in sources:
            source_id = obs.obs_source_get_unversioned_id(source)
            name = obs.obs_source_get_name(source)
            obs.obs_property_list_add_string(p, name, source_id)
        obs.source_list_release(sources)
    return props


def script_description():
    return f"Show a source only when recording \n{VERSION}"


def on_event(event):
    if event == obs.OBS_FRONTEND_EVENT_RECORDING_STARTED:
        # Make source visible
        make_visible()
    elif event == obs.OBS_FRONTEND_EVENT_RECORDING_STOPPED:
        # Make source invisible again
        make_invisible()


def script_load(settings):
    obs.obs_frontend_add_event_callback(on_event)
