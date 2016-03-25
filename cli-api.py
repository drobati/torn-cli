#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File: torn.py
Author: Derek Robati
Email: derek.robati@gmail.com
Github: https://github.com/drobati
Description: A CLI to interface to TORN API.
"""

from __future__ import print_function

import click
import json
import re

from torn import (
    User,
    Property,
    InvalidField
)

@click.group()
@click.argument('apikey')
@click.pass_context
def api(ctx, apikey):
    ctx.obj = apikey


@api.command()
@click.argument('field')
@click.pass_obj
def user(apikey, field):
    user = User(apikey)
    try:
        response = getattr(user, field)
        click.secho(field.capitalize() + ': ', fg="green", bold=True)
        value = json.loads(response.text)
        print(json.dumps(
            value,
            sort_keys=True,
            indent=4,
            separators=(',', ': ')
        ))
    except InvalidField:
        print("No selection from:")
        map(lambda x: print(x), user.selections)


@api.command()
@click.argument('property-id')
@click.pass_obj
def property(apikey, property_id):
    prop = Property(apikey, property_id)
    try:
        response = getattr(prop, 'property')
        click.secho('Property: ', fg="green", bold=True)
        value = json.loads(response.text)
        print(json.dumps(
            value,
            sort_keys=True,
            indent=4,
            separators=(',', ': ')
        ))
    except InvalidField:
        print("No selection from:")
        map(lambda x: print(x), prop.selections)


if __name__ == "__main__":
    api()
