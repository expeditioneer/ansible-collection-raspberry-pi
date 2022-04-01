#!/usr/bin/python

# Copyright: (c) 2022, Dennis Lamm
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import re
from typing import Dict

DOCUMENTATION = r'''
---
module: raspberry_pi_facts

short_description: This module provides facts for Raspberry PI devices 

version_added: "1.0.0"

description: This facts module provides facts for Raspberry PI devices like the Raspberry PI Model

author:
- Dennis Lamm (@expeditioneer)
notes:
- currently only supported for linux (depends on /proc/cpuinfo)
'''

EXAMPLES = r'''
- name: Return ansible_facts
  expeditioneer.raspberry_pi.raspberry_pi_facts:
'''

RETURN = r'''
raspberry_pi:
  description: Discovered facts for the Raspberry PI
  returned: always
  type: complex
  contains:
    compile_flags:
      description: optimal, supported compile flags for the CPU.
      type: str
      returned: always
      sample: '-march=armv8-a+crc -mtune=cortex-a53 -O2 -pipe'
    generation:
      description: Generation of the Raspberry PI.
      type: str
      returned: always
      sample: '4'
    model:
      description: The exact Model of the Raspberry PI
      type: str
      returned: always
      sample: 'Raspberry Pi 3 Model B Rev 1.2'
'''

from ansible.module_utils.basic import AnsibleModule

compile_flags: Dict[str, str] = {
    'Raspberry Pi 3 Model B Rev 1.2': '-march=armv8-a+crc -mtune=cortex-a53 -O2 -pipe',
    'Raspberry Pi 4 Model B Rev 1.4':
        '-march=armv8-a+crc+simd -mtune=cortex-a72 -ftree-vectorize -O2 -pipe -fomit-frame-pointer'
}


# Model and Pi Revision
# see https://elinux.org/RPi_HardwareHistory
def determine_cpu_information(module) -> Dict:
    unnecessary_entries = ['processor']

    rc, out, err = module.run_command('cat /proc/cpuinfo', check_rc=True)

    result: Dict = {}
    for element in out.split('\n'):
        key, *value = element.split(':')
        if key.strip() in unnecessary_entries:
            continue
        if not value:
            result[key.strip()] = ''
        else:
            result[key.strip()] = ' '.join(value).strip()

    return result


def determine_raspberry_pi_model(cpu_information: Dict) -> str:
    try:
        return cpu_information['Model']
    except KeyError:
        return ''


def run_module():
    module_args = dict()

    result = dict(
        changed=False,
        ansible_facts=dict(),
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    if module.check_mode:
        module.exit_json(**result)

    cpu_information = determine_cpu_information(module)

    raspberry_pi_model = determine_raspberry_pi_model(cpu_information)

    raspberry_pi: Dict = {
        'compile_flags': compile_flags.get(raspberry_pi_model),
        'generation': re.search(r'\d+', raspberry_pi_model).group(),
        'model': raspberry_pi_model,
    }

    # manipulate or modify the state as needed (this is going to be the
    # part where your module will do what it needs to do)
    result['ansible_facts'] = {
        'raspberry_pi': raspberry_pi
    }
    # in the event of a successful module execution, you will want to
    # simple AnsibleModule.exit_json(), passing the key/value results
    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
