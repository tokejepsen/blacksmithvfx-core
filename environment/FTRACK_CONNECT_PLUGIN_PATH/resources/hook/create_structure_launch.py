import os

import ftrack_api
import lucidity


def modify_launch(event):
    """Return directories and files to create."""

    templates = lucidity.discover_templates()
    for entity in event["data"].get("entities", []):
        valid_templates = templates[0].get_valid_templates(
            entity, templates
        )

        for template in valid_templates:

            try:
                path = os.path.abspath(
                    template.format(entity)
                ).replace("\\", "/")
            except lucidity.error.FormatError:
                continue
            else:

                if os.path.exists(path):
                    continue

                if hasattr(template, "source"):
                    if not os.path.exists(path):
                        event["data"]["files"].append((template.source, path))
                else:
                    if not os.path.exists(path):
                        event["data"]["directories"].append(path)

    return event


def register(session, **kw):
    '''Register event listener.'''

    # Validate that session is an instance of ftrack_api.Session. If not,
    # assume that register is being called from an incompatible API
    # and return without doing anything.
    if not isinstance(session, ftrack_api.Session):
        # Exit to avoid registering this plugin again.
        return

    # Register the event handler
    session.event_hub.subscribe('topic=create_structure.launch', modify_launch)
