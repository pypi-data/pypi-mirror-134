from . import *


@click.command()
@click.argument("code", required=True)
def commander(code):
    if str(code) == 'init':
        print('Initializing....')
        return
    
    NHentai(code).save_images(debug=True)

commander()
