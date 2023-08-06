# std
from os.path import isfile

# internal
from packages.terraform_install.terraform_install.constants import TERRAFORM_PATH


def is_terraform_installed() -> bool:
    return isfile(TERRAFORM_PATH)
