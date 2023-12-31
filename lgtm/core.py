import click


@click.command()
@click.option("--message", "-m", default="LGTM",
              show_default=True, help="이미지에 추가할 문자열")
@click.argument("keyword")
def cli(keyword, message):
    """LGTM 이미지 생성 도구"""
    lgtm(keyword, message)
    click.echo('lgtm')


def lgtm(keyword, message):
    pass
