#!/usr/bin/env python

from setuptools import setup
from pip.req import parse_requirements
import uuid

install_reqs = parse_requirements('./requirements.txt', session=uuid.uuid1())

setup(name='slack_webhooks',
      version='1.0.1',
      description='Webhook helper for Slack',
      author='Jeff Rand',
      author_email='jeffreyrand@gmail.com',
      install_requires=[str(ir.req) for ir in install_reqs],
      url='https://github.com/jeffrand/slack-webhooks',
      packages=['slack_webhooks'],
)
