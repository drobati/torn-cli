#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
File: cli-torn.py
Author: drobati
Email: derek.robati@gmail.com
Github: https://github.com/drobati
Description: A friendlier cli for torn.
"""

from __future__ import print_function

import click
from datetime import datetime
import json
import re

from torn import (
    User,
    Property
)

def power(user, delta, power_name):
    response = user.bars
    bars = json.loads(response.text)
    power = bars[power_name]
    current, maximum = power["current"], power["maximum"]
    if not delta:
        click.secho("%s:" % power_name.capitalize(), fg="green", bold="True")
        print("%s/%s" % (current, maximum))
    else:
        delta = int(maximum) - int(current)
        click.secho("%s" % (delta), fg="green", bold="True")


@click.group()
@click.argument('apikey')
@click.pass_context
def torn(ctx, apikey):
    ctx.obj = User(apikey)


@torn.command()
@click.option('--seconds/--no-seconds', default=False, 
              help="Return time in epoch format.")
@click.pass_obj
def hospital(user, seconds):
    response = user.icons
    icons = json.loads(response.text)
    try:
        value = icons["icons"]["icon15"]
    except KeyError:
        value = "00:00:00"
    pattern = re.compile(r'(\d*:\d*:\d*)')
    matches = re.search(pattern, value)
    time = matches.groups()[0]
    if not seconds:
        click.secho("Time Left in Hospital:", fg="green", bold="True")
        print(time)
    else:
        times = map(lambda x: int(x), time.split(':'))
        print(times[0] * 3600 + times[1] * 60 + times[2])


@torn.command()
@click.option('--delta/--no-delta', default=False, 
              help="Return health left till full.")
@click.pass_obj
def energy(user, delta):
    power(user, delta, "energy")


@torn.command()
@click.option('--delta/--no-delta', default=False, 
              help="Return health left till full.")
@click.pass_obj
def nerve(user, delta):
    power(user, delta, "nerve")

@torn.command()
@click.pass_obj
def property_time(user):
    profile = json.loads(user.profile.text)
    property_id = profile['property_id']
    prop = Property(user.apikey, property_id)
    property = json.loads(prop.property.text)
    time_left = property['property']['rented']['days_left']
    click.secho("Time Left for Rent:", fg="green", bold="True")
    print(time_left)


if __name__ == "__main__":
    torn()
