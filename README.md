# Ansible Collection for Raspberry PI

The Ansible Raspberry PI collection includes a variety of Ansible content to help automate the management of Raspberry 
PI Systems.

## Python version compatibility
This collection requires Python 3.6 or greater.

## Included content

### Modules
Name | Description
--- | ---
[expeditioneer.raspberry_pi.raspberry_pi_facts](https://github.com/expeditioneer/ansible-collection-raspberry-pi/blob/main/docs/raspberry_pi_facts.rst)|Gather facts about the raspberry pi

## Installing this collection

You can install the AWS collection with the Ansible Galaxy CLI:

    ansible-galaxy collection install expeditioneer.raspberry_pi

You can also include it in a `requirements.yml` file and install it with `ansible-galaxy collection install -r requirements.yml`, using the format:

```yaml
---
collections:
  - name: expeditioneer.raspberry_pi
```

A specific version of the collection can be installed by using the `version` keyword in the `requirements.yml` file:

```yaml
---
collections:
  - name: expeditioneer.raspberry_pi
    version: 1.0.0
```

## LICENSING

All content in this procject is licensed under the [GPL-3.0 License](LICENSE)
