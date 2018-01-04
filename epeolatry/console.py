import click

from epeolatry import get_document_parser

@click.command()
@click.argument('file')
def cli(file):
    doc = get_document_parser(file)
    
    print('Mime Type: {}'.format(doc.mime_type))
    print('Text Content:')
    print(doc.to_text())