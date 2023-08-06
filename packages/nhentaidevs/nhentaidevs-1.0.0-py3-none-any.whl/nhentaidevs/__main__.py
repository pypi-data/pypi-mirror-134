from . import *


@click.command()
@click.argument("code", required=True)
def fetch(code):
    NHentai(code).save_images(debug=True)

fetch()
