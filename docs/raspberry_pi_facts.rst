.. _expeditioneer.raspberry_pi.raspberry_pi_facts:


*********************************************
expeditioneer.raspberry_pi.raspberry_pi_facts
*********************************************

**Provides additional facts from the Raspberry PI**

Version added: 1.0.0

.. contents::
    :local:
    :depth: 1

Requirements
------------
The below requirements are needed on the host that executes this module.

- python >= 3.6

Example
-------

.. code-block:: yaml

    - name: set Raspberry PI specific facts
      expeditioneer.raspberry_pi.raspberry_pi_facts:


Provided Facts
--------------

.. raw:: html

    <table border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="2">Key</th>
            <th width="100%">Description</th>
        </tr>
        <tr>
        </tr>
            <td colspan="2"><b>raspberry_pi</b><br>complex</td>
            <td>discoverd facts for the Raspberry PI</td>
        <tr>
        <tr>
            <td></td>
            <td><b>compile_flags</b><br>string</td>
            <td>optimal, supported compile flags for the CPU<br><br><b>Sample:</b><br>-march=armv8-a+crc -mtune=cortex-a53 -O2 -pipe</td>
        </tr>
        <tr>
            <td></td>
            <td><b>generation</b><br>string</td>
            <td>Generation of the Raspberry PI<br><br><b>Sample:</b><br>3</td>
        </tr>
        <tr>
            <td></td>
            <td><b>model</b><br>string</td>
            <td><br>The exact Model of the Raspberry PI<br><br><b>Sample:</b><br>Raspberry Pi 3 Model B Rev 1.2</td>
        </tr>
    </table>

Status
------

Authors
~~~~~~~

- Dennis Lamm (@expeditioneer)
