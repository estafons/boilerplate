import click
import jinja2
from boilerplate.helpers import find_jinja_template, find_yaml_file, read_values_from_yaml

@click.group()
@click.version_option()
def main():
    """
    CLI entrypoint.
    """
    pass


@main.command()
@click.option(
    "--template-path", type=click.Path(exists=True), help="Path to the input template"
)
@click.option("--output", type=click.Path(), help="Path to the output file")
def create(template_path, output):
    """
    Create a new file from a template.
    """
    template_file = find_jinja_template(template_path)
    values_file = find_yaml_file(template_path)

    with open(template_file) as f:
        template = jinja2.Template(f.read())
    with open(output, "w") as o:
        o.write(template.render(**read_values_from_yaml(values_file)))
