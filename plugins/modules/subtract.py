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
module: subtract

short_description: A positive subtraction module

description:
  - Subtracts one number from another, but only if the result is zero or above.


version_added: '0.1.0'

author:
  - Sandra McCann (@samccann)

options:
  minuend:
    description:
      - Minuend - number to subtract from.
    type: int
    required: true

  subtrahend:
    description:
      - subtrahend - number to subtract.
      - must be greater than zero.
    type: int
    required: true
'''

EXAMPLES = r'''
- name: Subtract subtrahend from  minuend
  register: result
  samccann.sample.subtract:
    minuend: 5
    subtrahend: 2

- name: Print the result
  ansible.builtin.debug:
    var: result.quotient
'''

RETURN = r'''
quotient:
  description:
  - The result of subtraction.
  returned: on success
  sample: 3
  type: int
'''

from ansible.module_utils.basic import AnsibleModule


def main():
    # The module accepts arguments declared here.
    argument_spec = {}
    argument_spec.update(
        minuend=dict(type='int', required=True),
        subtrahend=dict(type='int', required=True),
    )

    # Instantiate an object of the AnsibleModule class
    # provided by the Ansible Core.
    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True,
    )

    # Assign passed options to variables
    minuend = module.params['minuend']
    subtrahend = module.params['subtrahend']

    # The work starts here.
    # All interactions with the user happen through
    # interfaces provided by the module object of
    # the AnsibleModule class of Ansible Core.
    # Let's fail when the divisor is zero using the fail_json() method.
    if subtrahend <= 0:
        module.fail_json("Subtraction by zero or a negative number is not allowed!")

    # Do something.
    difference = minuend - subtrahend

    # In our special-case subtraction, we won't allow negative results
    if difference < 0:
        module.fail_json("No negative results allowed!")

    # Exit the module.
    # Users will get the result in its JSON output after execution.
    module.exit_json(changed=False, difference=difference)


if __name__ == '__main__':
    main()
