# coding=utf-8
from __future__ import absolute_import
import codecs
import sys
import os
import base64
import re
import datetime
import subprocess
from smtpd import SMTPServer
from django.core.management.base import BaseCommand
from django.utils.encoding import force_unicode
from dj_utils.settings import UTILS_EMAIL_DEBUG_PATH, UTILS_EMAIL_DEBUG_IN_CONSOLE, UTILS_EMAIL_DEBUG_IN_FILES


class DebuggingServer(SMTPServer):
    def __init__(self, *args, **kwargs):
        SMTPServer.__init__(self, *args, **kwargs)
        sys.stdout = codecs.getwriter('utf8')(sys.stdout)
        sys.stderr = codecs.getwriter('utf8')(sys.stderr)

    @staticmethod
    def _get_subject(data):
        subject_re = re.compile(ur'^Subject: (.+)$', re.IGNORECASE | re.U)
        base64_re = re.compile(ur'^=\?(.+)\?b\?(.+)\?=$', re.IGNORECASE | re.U)
        for line in data.split('\n'):
            m = subject_re.match(line)
            if m:
                subject = m.group(1).strip()
                m = base64_re.match(subject)
                if m:
                    charset, content = m.groups()
                    subject = force_unicode(base64.b64decode(content))
                return subject
        return ''

    @staticmethod
    def _get_fn(fn_base, n=None):
        if n is None:
            return os.path.join(UTILS_EMAIL_DEBUG_PATH, u'{}.eml'.format(fn_base)).replace('\\', '/')
        else:
            return os.path.join(UTILS_EMAIL_DEBUG_PATH, u'{}_{}.eml'.format(fn_base, n)).replace('\\', '/')

    def process_message(self, peer, mailfrom, rcpttos, data):
        try:
            if UTILS_EMAIL_DEBUG_IN_FILES:
                if not os.path.exists(UTILS_EMAIL_DEBUG_PATH):
                    os.makedirs(UTILS_EMAIL_DEBUG_PATH)
                fn_base = u'{}_{}_{}_{}'.format(
                    u'_'.join(rcpttos),
                    self._get_subject(data),
                    mailfrom,
                    datetime.datetime.now().strftime(u'%Y-%m-%d_%H-%M-%S')
                )
                fn_base = re.sub(ur'[:\*\?"<>\| ]+', '_', fn_base, re.U)
                fn = self._get_fn(fn_base)
                n = 1
                while os.path.exists(fn):
                    fn = self._get_fn(fn_base, n)
                    n += 1
                f = codecs.open(fn, 'w', encoding='utf-8')
            inheaders = 1
            for line in data.split('\n'):
                if inheaders and not line:
                    if UTILS_EMAIL_DEBUG_IN_FILES:
                        f.write(u'X-Peer: {}\n'.format(force_unicode(peer[0])))
                    if UTILS_EMAIL_DEBUG_IN_CONSOLE:
                        print u'X-Peer: {}'.format(force_unicode(peer[0]))
                    inheaders = 0
                line = force_unicode(line)
                if UTILS_EMAIL_DEBUG_IN_FILES:
                    f.write(u'{}\n'.format(line))
                if UTILS_EMAIL_DEBUG_IN_CONSOLE:
                    print line
        except Exception, e:
            print 'DebuggingServer error: {}'.format(force_unicode(e))


class Command(BaseCommand):
    help = 'Run debug smtp server'

    def handle(self, *args, **options):
        subprocess.call([
            sys.executable,
            '-m', 'smtpd', '-n', '-c', 'dj_utils.management.commands.debug_email_server.DebuggingServer',
            'localhost:10250'
        ])
