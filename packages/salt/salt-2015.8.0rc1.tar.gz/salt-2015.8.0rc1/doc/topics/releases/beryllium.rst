=======================================
Salt Release Notes - Codename Beryllium
=======================================

Core Changes
============

- Add system version info to ``versions_report``, which appears in both ``salt
  --versions-report`` and ``salt '*' test.versions_report``. Also added is an
  alias ``test.versions`` to ``test.versions_report``. (:issue:`21906`)

- Add colorized console logging support.  This is activated by using
  ``%(colorlevel)s``, ``%(colorname)s``, ``%(colorprocess)s``, ``%(colormsg)s``
  in ``log_fmt_console`` in the config file for any of ``salt-master``,
  ``salt-minion``, and ``salt-cloud``.

Salt Cloud Changes
==================

- Modified the Linode Salt Cloud driver to use Linode's native API instead of
  depending on apache-libcloud or linode-python.

JBoss 7 State
=============

Remove unused argument ``timeout`` in jboss7.status.

Pkgrepo State
=============

Deprecate ``enabled`` argument in ``pkgrepo.managed`` in favor of ``disabled``.

Archive Module
==============

In the ``archive.tar`` and ``archive.cmd_unzip`` module functions, remove the
arbitrary prefixing of the options string with ``-``.  An options string
beginning with a ``--long-option``, would have uncharacteristically needed its
first ``-`` removed under the former scheme.

Also, tar will parse its options differently if short options are used with or
without a preceding ``-``, so it is better to not confuse the user into
thinking they're using the non- ``-`` format, when really they are using the
with- ``-`` format.

Win System Module
=================

The unit of the ``timeout`` parameter in the ``system.halt``,
``system.poweroff``, ``system.reboot``,  and ``system.shutdown`` functions has
been changed from seconds to minutes in order to be consistent with the linux
timeout setting. (:issue:`24411`)  Optionally, the unit can be reverted to
seconds by specifying ``in_seconds=True``.

Deprecations
============

- The ``digital_ocean.py`` Salt Cloud driver was removed in favor of the
``digital_ocean_v2.py`` driver as DigitalOcean has removed support for APIv1.
The ``digital_ocean_v2.py`` was renamed to ``digital_ocean.py`` and supports
DigitalOcean's APIv2.

- The ``vsphere.py`` Salt Cloud driver has been deprecated in favor of the
``vmware.py`` driver.

- The ``openstack.py`` Salt Cloud driver has been deprecated in favor of the
``nova.py`` driver.

- The use of ``provider`` in Salt Cloud provider files to define cloud drivers
has been deprecated in favor of useing ``driver``. Both terms will work until
the Nitrogen release of Salt. Example provider file:

.. code-block:: yaml

    my-ec2-cloud-config:
      id: 'HJGRYCILJLKJYG'
      key: 'kdjgfsgm;woormgl/aserigjksjdhasdfgn'
      private_key: /etc/salt/my_test_key.pem
      keyname: my_test_key
      securitygroup: default
      driver: ec2
