"""
"""

# Created on 2015.04.15
#
# Author: Giovanni Cannata
#
# Copyright 2015 Giovanni Cannata
#
# This file is part of sldap3.
#
# sldap3 is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# sldap3 is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with sldap3 in the COPYING and COPYING.LESSER files.
# If not, see <http://www.gnu.org/licenses/>.

import logging
from time import sleep
import sys
from sldap3 import EXEC_THREAD, EXEC_PROCESS

logging.basicConfig(
    filename='c:\\Temp\\sldap3.log',
    level=logging.DEBUG,
    format='[sldap3-service] %(levelname)-7.7s %(message)s'
)

try:
    import win32serviceutil
    import win32service
    import win32event
    import servicemanager
except ImportError:
    logging.error('pywin32 package missing')
    sys.exit(1)

sys.stderr = open('C:\\Temp\\pyasn1.log', 'a')  # patch for pyasn1 without access to stderr

try:
    import pyasn1
except ImportError:
    logging.error('pyasn1 package missing')
    sys.exit(2)

try:
    import ldap3
except ImportError:
    logging.error('ldap3 package missing')
    sys.exit(3)

try:
    from asyncio import BaseEventLoop
except ImportError:
    try:
        import trollius as asyncio
        from trollius import From, Return
    except:
        logging.error('trollius package missing')
        sys.exit(4)

try:
    import sldap3
except ImportError:
    logging.error('sldap3 package missing')
    sys.exit(5)


class Sldap3Service (win32serviceutil.ServiceFramework):
    _svc_name_ = 'sldap3'
    _svc_display_name_ = 'sldap3 - LDAP Server'
    _svc_description_ = 'A strictly RFC 4511 conforming LDAP V3 pure Python server'

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.stop_event = win32event.CreateEvent(None, 0, 0, None)
        self.instances = list()
        self.stop_requested = False

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.stop_event)
        logging.info('stopping sldap3 service...')
        self.stop_requested = True

    def SvcDoRun(self):
        logging.info('running sldap3 service...')
        servicemanager.LogMsg(
            servicemanager.EVENTLOG_INFORMATION_TYPE,
            servicemanager.PYS_SERVICE_STARTED,
            (self._svc_name_, '')
        )
        self.run()
        logging.info('ending sldap3 service...')

    def run(self):
        logging.info('executing sldap3 service...')

        logging.info('instantiating sldap3 daemon')
        self.instances = []
        user_backend = sldap3.JsonUserBackend('/root/sldap3/test/localhost-users.json')
        user_backend.add_user('giovanni', 'admin', 'password')
        user_backend.add_user('beatrice', 'user', 'password')
        user_backend.store()

        dsa1 = sldap3.Instance(
            sldap3.Dsa('DSA1',
                       '0.0.0.0',
                       cert_file='/root/sldap3/test/server-cert.pem',
                       key_file='/root/sldap3/test/server-key.pem',
                       user_backend=user_backend),
            name='MixedInstance',
            executor=EXEC_THREAD)
        dsa2 = sldap3.Instance(
            sldap3.Dsa('DSA2',
                       '0.0.0.0',
                       port=1389,
                       user_backend=user_backend),
            name='UnsecureInstance',
            executor=EXEC_THREAD)

        self.instances.append(dsa1)
        self.instances.append(dsa2)

        for instance in self.instances:  # start each instance in a new thread
            instance.start()

        logging.info('sldap3 daemon instantiation complete')

        while not self.stop_requested:  # wait for stop signal
            sleep(3)

        for instance in self.instances:  # wait for all instances to end
            instance.stop()

        logging.info('sldap3 service stopped')

if __name__ == '__main__':
    win32serviceutil.HandleCommandLine(Sldap3Service)
