import os

from jinja2 import (
    Environment,
    PackageLoader,
    select_autoescape
)


class FileGenerator:
    def __init__(self, project_name: str):
        self.proj_name = project_name
    
    def generate_file(
        self,
        fp: str,
        content: str,
        *,
        use_name: bool = True
    ):
        if use_name is True:
            fp = self.proj_name + (fp if fp.startswith("/") else f"/{fp}")
        with open(fp, "w+", encoding="utf-8") as _file:
            _file.write(content)

def generate_boilerplate(name: str):
    # jinja is primarily used for HTML template rendering,
    # however, it's also the cleanest option as of now to generate,
    # proprietory boilerplate for webx.
    env = Environment(
        loader=PackageLoader("webx.core.management.boilerplate", package_path="."),
        autoescape=select_autoescape()
    )
    generator = FileGenerator(name)

    # Create an initial project directory.
    os.mkdir(f"./{name}")

    # Create the manage.py file.
    manage_template = env.get_template("manage.template")
    manage_rendered = manage_template.render()
    generator.generate_file("manage.py", manage_rendered, use_name=False)

    # Just 'render' the application file, with no extra arguments, and create it.
    application_template = env.get_template("project/application.template")
    application_rendered = application_template.render(project_name=name)
    generator.generate_file("application.py", application_rendered)

    # Render settings
    settings_template = env.get_template("project/settings.template")
    _key = os.urandom(16).hex()
    settings_rendered = settings_template.render(project_name=name, secret_key=_key)
    generator.generate_file("settings.py", settings_rendered)

    # Render routes
    routes_template = env.get_template("project/routes.template")
    routes_rendered = routes_template.render()
    generator.generate_file("routes.py", routes_rendered)

    # Render views
    views_template = env.get_template("project/views.template")
    views_rendered = views_template.render()
    generator.generate_file("views.py", views_rendered)