"""
moalerts

A library for interacting with the MO Alerts database.

Basic usage:
   import moalerts

   moalerts.start(dbname='', user='', password='', host='', port='')
   moalerts.list_alerts()
   >>> [
   >>>   {...}
   >>> ]

   moalerts.add_alert(...)
"""

from .core import (
  start, add_alerts_from_df, add_alert,
  add_alarm, list_alerts, list_alarms
)