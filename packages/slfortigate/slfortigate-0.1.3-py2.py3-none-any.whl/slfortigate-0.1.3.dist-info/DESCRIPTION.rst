SL Fortigate Order and Configuration Tool
=========================================

Installation Preconditions
--------------------------

You must have a SoftLayer account; if you were not provided with one, or you cannot use the provided credentials to authenticate at https://control.softlayer.com/, please contact a support person in your group.

Installation
------------

The SL Fortigate tool is a Python module installable from the public PyPI repository, https://pypi.python.org/pypi. If you have a system with an installed, configured copy of the SoftLayer library (https://pypi.python.org/pypi/SoftLayer), you can install the slfortigate package with this command:

  pip install slfortigate

You can access usage information by invoking the command with the help argument, e.g.:

  slfortigate --help

(Note that recent versions of the HTTP client used by the SoftLayer tool may complain about out-of-date SSL native libraries. For more information about this issue, consult https://urllib3.readthedocs.org/en/latest/security.html.)

If you do not have a suitable Linux system or SoftLayer installed and configured, follow the below instructions to provision a system in SoftLayer and configure it.

Setting up a Linux system in SoftLayer
--------------------------------------
Use your SoftLayer credentials to provision a Virtual Server (VS) with the SoftLayer control panel at https://control.softlayer.com/. Please provision a CentOS 7 64bit system. Once provisioned, use SSH to connect to the system and issue the following commands:

  yum install -y epel-release && yum install -y python-pip python-devel gcc openssl-devel libffi-devel && pip install --upgrade pip && pip install slfortigate

Configure the SoftLayer tool
----------------------------
To configure the SoftLayer command line tool, execute:

  slcli config setup

If you need to obtain a SoftLayer API key to complete the CLI configuration procedure, consult http://knowledgelayer.softlayer.com/procedure/generate-api-key.

Once your SoftLayer account is configured you may use the slfortigate tool. To access usage information, invoke slfortigate with the help argument, e.g.:

  slfortigate --help

Copyright
---------

This software is Copyright (c) 2015 IBM, Inc.

See the bundled LICENSE file for more information.



