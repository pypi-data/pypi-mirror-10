# encoding: utf-8
"""
Created on 11/17/14

@author: Takashi NAGAI
"""

__author__ = 'nagai'

import time
import logging
from random import random
from datetime import datetime as dt
from datadog import initialize
from datadog import api as dd_api
from datadog.dogstatsd import base
from plone import api
from AccessControl.SecurityInfo import ModuleSecurityInfo
try:
    from itertools import imap
except ImportError:
    imap = map
from ngi.notify.datadog import _

logger = logging.getLogger(__name__)
security = ModuleSecurityInfo('ngi.notify.datadog.dd')


class DogStasd4Plone(base.DogStatsd):
    """
    DogStatsd wrapper class
    """

    def _report(self, metric, metric_type, value, tags, sample_rate):
        if sample_rate != 1 and random() > sample_rate:
            return

        payload = [metric, u":", value, u"|", metric_type]
        if sample_rate != 1:
            payload.extend([u"|@", sample_rate])
        if tags:
            payload.extend([u"|#", u",".join(tags)])

        encoded = u"".join(imap(unicode, payload))
        self._send(encoded)


statsd_plone = DogStasd4Plone()


def _get_connect_string():
    """

    :return:
    """
    use_dogstatsd = statsd_host = statsd_port = dd_api_key = dd_app_key = host_name = instance_name = ''
    try:
        use_dogstatsd = api.portal.get_registry_record('ngi.notify.datadog.controlpanel.IDatadog.use_dogstatsd')
        statsd_host = api.portal.get_registry_record('ngi.notify.datadog.controlpanel.IDatadog.statsd_host')
        statsd_port = api.portal.get_registry_record('ngi.notify.datadog.controlpanel.IDatadog.statsd_port')
        dd_api_key = api.portal.get_registry_record('ngi.notify.datadog.controlpanel.IDatadog.api_key')
        dd_app_key = api.portal.get_registry_record('ngi.notify.datadog.controlpanel.IDatadog.application_key')
        host_name = api.portal.get_registry_record('ngi.notify.datadog.controlpanel.IDatadog.host_name')
        instance_name = api.portal.get_registry_record('ngi.notify.datadog.controlpanel.IDatadog.instance_name')
    except:
        logging.warning('ngi.notify.datadog:No registry keys')
    return use_dogstatsd, statsd_host, statsd_port, dd_api_key, dd_app_key, host_name, instance_name


def _dict2list(tags={}):
    return [u"{k}:{v}".format(k=k, v=v) for k, v in tags.items()]


security.declarePublic('metric_datadog')


def metric_datadog(metric_name, value=1.0, tags={}, metric_type=u'gauge'):
    """
    post to Datadog service
    :param metric_name: string
    :param value: float
    :param tags: dict
    :param metric_type: string
    :return:
    """

    use_dogstatsd, statsd_host, statsd_port, dd_api_key, dd_app_key, host_name, instance_name = _get_connect_string()

    if metric_name:
        tags['plone_instance'] = instance_name
        dd_tags = _dict2list(tags)
        if use_dogstatsd:
            initialize(statsd_host=statsd_host, statsd_port=statsd_port)
            if metric_type == u'gauge':
                statsd_plone.gauge(metric=metric_name, value=value, tags=dd_tags)
            elif metric_type == u'counter':
                statsd_plone.increment(metric=metric_name, tags=dd_tags)
            elif metric_type == u'histogram':
                statsd_plone.histogram(metric=metric_name, value=value, tags=dd_tags)
        elif dd_api_key:
            keys = {
                'api_key': dd_api_key,
                'app_key': dd_app_key
            }
            initialize(**keys)
            dd_api.Metric.send(metric=metric_name, points=value, host=host_name, tags=dd_tags, metric_type=metric_type)


security.declarePublic('event_datadog')


def event_datadog(title, text, date_happened='', tags={}):
    """

    :param title:
    :param text:
    :param date_happened:
    :param tags:
    :return:
    """

    use_dogstatsd, statsd_host, statsd_port, dd_api_key, dd_app_key, host_name, instance_name = _get_connect_string()

    if not date_happened:
        now = dt.now()
        date_happened = time.mktime(now.timetuple())

    if title and text:
        tags['plone_instance'] = instance_name
        dd_tags = _dict2list(tags)
        if use_dogstatsd:
            initialize(statsd_host=statsd_host, statsd_port=statsd_port)
            statsd_plone.event(title=title, text=text, date_happened=date_happened, tags=dd_tags)
        elif dd_api_key:
            keys = {
                'api_key': dd_api_key,
                'app_key': dd_app_key
            }
            initialize(**keys)
            dd_api.Event.create(title=title, text=text, date_happened=date_happened, tags=dd_tags, host=host_name)
