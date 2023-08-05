#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import typer
import sys
from pathlib import Path


# Detect if called from pypi installed package or via cloned github repo (development)
try:
    from centralcli import cli, utils
except (ImportError, ModuleNotFoundError) as e:
    pkg_dir = Path(__file__).absolute().parent
    if pkg_dir.name == "centralcli":
        sys.path.insert(0, str(pkg_dir.parent))
        from centralcli import cli, utils
    else:
        print(pkg_dir.parts)
        raise e

app = typer.Typer()

tty = utils.tty


# TODO add cache for webhooks
@app.command(short_help="Test WebHook")
def webhook(
    wid: str = typer.Argument(..., help="WebHook ID",),
    default: bool = typer.Option(False, "-d", is_flag=True, help="Use default central account", show_default=False,),
    debug: bool = typer.Option(False, "--debug", envvar="ARUBACLI_DEBUG", help="Enable Additional Debug Logging",),
    account: str = typer.Option("central_info",
                                envvar="ARUBACLI_ACCOUNT",
                                help="The Aruba Central Account to use (must be defined in the config)",),
):
    resp = cli.central.request(cli.central.test_webhook, wid)

    cli.display_results(resp, tablefmt="rich", title="WebHook Test Results")


@app.callback()
def callback():
    """
    Perform Tests
    """
    pass


if __name__ == "__main__":
    app()
