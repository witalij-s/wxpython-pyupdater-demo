#!/usr/bin/env python
import os
import sys
import logging

from client_config import ClientConfig
from pyupdater.client import Client

import wxpythonupdater
from wxpythonupdater.main import MainWindow

def CheckForUpdates():
    """
    Check for updates.
    Channel options are stable, beta & alpha
    Patches are only created & applied on the stable channel
    """
    CLIENT_CFG = ClientConfig()

    # refresh to get the online manifest for version checking
    client = Client(ClientConfig(), refresh=True)

    #logger.info('Checkung for updates')
    appUpdate = client.update_check(CLIENT_CFG.APP_NAME,
                                    wxpythonupdater.__version__,
                                    channel='stable') # alpha, beta
    if appUpdate:
        if hasattr(sys, "frozen"):
            downloaded = appUpdate.download()
            if downloaded:
                status = 'Extracting update and restarting.'
                appUpdate.extract_restart()
            else:
                status = 'Update download failed.'
        else:
            status = 'Update available but application is not frozen.'
    else:
        status = 'No available updates were found.'

    return status


if __name__ == "__main__":
    status = CheckForUpdates()
    print status
    MainWindow.Run()
