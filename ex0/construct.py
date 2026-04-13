# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  construct.py                                      :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: klucchin <klucchin@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/04/11 12:43:22 by klucchin        #+#    #+#               #
#  Updated: 2026/04/13 14:24:10 by klucchin        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import sys
import os


def is_virtual_env() -> bool:
    return (
        hasattr(sys, 'base_prefix') and sys.prefix != sys.base_prefix
    ) or hasattr(sys, 'real_prefix')


def get_venv_name() -> str:
    return os.path.basename(sys.prefix)


def main() -> None:
    in_venv = is_virtual_env()

    python_path = sys.executable

    if not in_venv:
        print("MATRIX STATUS: You're still plugged in")
        print(f"Current Python: {python_path}")
        print("Virtual Environment: None detected")
        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.\n")

        print("To enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate  # On Unix")
        print("matrix_env\\Scripts\\activate    # On Windows")
        print("Then run this program again.")

    else:
        venv_name = get_venv_name()
        env_path = sys.prefix

        python_version = f"python{sys.version_info.major}."
        f"{sys.version_info.minor}"
        site_packages = os.path.join(
            env_path, "lib", python_version, "site-packages")

        print("MATRIX STATUS: Welcome to the construct")
        print(f"Current Python: {python_path}")
        print(f"Virtual Environment: {venv_name}")
        print(f"Environment Path: {env_path}")
        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting")
        print("the global system.\n")

        print("Package installation path:")
        print(site_packages)


if __name__ == "__main__":
    main()
