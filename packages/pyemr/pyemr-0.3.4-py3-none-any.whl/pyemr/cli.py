# pylint: disable=R0201,C0413
"""Command Line Interface"""
import argparse
import sys


def remove_submodules(package_name):
    """

    Args:
      package_name: name of package to remove from sys.modules

    """
    modules = []
    for module in sys.modules:
        if module.startswith(package_name):
            modules.append(module)

    for module in modules:
        del sys.modules[module]


def append_additional_site_packages():
    """ """
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--additional_site_package_paths",
        type=str,
        help="Site packages to pass to pass to the enviroment.",
        default="",
    )
    args, unknown = parser.parse_known_args()
    site_packages = args.additional_site_package_paths.strip().split(",")
    for path in site_packages:
        if path not in sys.path:
            sys.path.append(path)


try:  # noqa  # isort: skip
    import fire

    from pyemr.main import Cli

    cli = Cli()
except:  # noqa  # isort: skip
    remove_submodules("pyemr")
    remove_submodules("fire")
    # if import fails then add additional site packages
    print(
        "Pyemr couldn't be imported. "
        "Appending additional site packages to search path.",
    )
    append_additional_site_packages()

    import fire

    from pyemr.main import Cli as Cli2

    cli = Cli2()


def main():
    """ """
    fire.Fire(cli)


if __name__ == "__main__":
    main()
