from jinja2 import (
    Environment,
    PackageLoader,
    select_autoescape
)

from webx.config.settings import settings


class RefresheableEngine:
    """
    This class holds a Jinja2 environment within it.
    Also has the ability to re-create environments based on settings changes.
    """
    def __init__(self):
        templates_dir = settings.get("TEMPLATES_DIRECTORY")
        project_name = settings.get("PROJECT_NAME")
        assert project_name is not None, "PROJECT_NAME has not been set in your settings file."

        self._environment = Environment(
            loader=PackageLoader(project_name, package_path=templates_dir),
            autoescape=select_autoescape()
        )

    def _refresh(self):
        _temp_engine = RefresheableEngine()
        self._environment = _temp_engine._environment
        return _temp_engine