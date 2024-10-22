#!/usr/bin/python
# -*- coding: utf-8 -*-

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

# What you define in this section will appear on Galaxy
# and on docs.ansible.com as module documentation
# if it gets included in the Ansible package.
DOCUMENTATION = r'''
---
module: kernel_facts

short_description: facts about the system kernel

description:
  - Returns the system kernel version in a specific format.

version_added: '0.1.0'

author:
  - Sandra McCann (@samccann)

'''

EXAMPLES = r'''
- name: Return OS kernel details
  register: result
  samccann.sample.kernel_facts:


- name: Print the result
  ansible.builtin.debug:
    var: result.kernel
'''

RETURN = r'''
---
kernel:
  description: Linux kernel for a host
  returned: success
  type: str
  sample: Linux-6.10.12-200.fc40.x86_64-x86_64-with-glibc2.39
'''

import platform
from ansible.module_utils.basic import AnsibleModule


def main():
    # The module accepts arguments declared here.
    argument_spec = {}

    # Instantiate an object of the AnsibleModule class
    # provided by the Ansible Core.
    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True,
    )

    # The work starts here.
    # All interactions with the user happen through
    # interfaces provided by the module object of
    # the AnsibleModule class of Ansible Core.
    # Get the kernel details
    kernel_facts = {
        'kernel': None
    }
    kernel_facts['kernel'] = platform.platform()

    # Exit the module.
    # Users will get the result in its JSON output after execution.
    kernel_facts_result = dict(changed=False, ansible_facts=kernel_facts)
    module.exit_json(**kernel_facts_result)


if __name__ == '__main__':
    main()
