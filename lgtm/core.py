import click


@click.command()
def cli():
    """LGTM 이미지 생성 도구"""
    lgtm()
    click.echo('lgtm')


def lgtm():
    pass