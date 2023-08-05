==============
jailconf_tools
==============

**jailconf_tools** is a python package which includes a lot of tools to use with the new jail format on a freebsd host.

Howto
-----

This is an example of howto use jailconf parser :

::

    #!/usr/bin/env python
    import sys
    from jailconf_tools.parser import get_jails_config


    def main():
        """Main function"""

        try:
            print(get_jails_config())
        except:
            return 1
        else:
            return 0

    if __name__ == "__main__":
        sys.exit(main())

This peace of code returns a python dict which contains all jails definition.
