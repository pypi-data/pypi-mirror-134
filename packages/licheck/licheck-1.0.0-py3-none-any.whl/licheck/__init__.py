#
# __init__.py
#
# Copyright (C) 2021-2022 Franco Masotti (franco DoT masotti {-A-T-} tutanota DoT com)
#
# This file is part of licheck.
#
# licheck is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# licheck is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with licheck.  If not, see <http://www.gnu.org/licenses/>.
#
"""Python discovery file."""

from .api import (build_command, check_cache_structure,
                  check_configuration_structure, check_data_object_structure,
                  check_dependencies_files_data_structure, check_licenses,
                  create_cache_output, create_data_object,
                  create_dependencies_files_data_structure,
                  get_binary_and_program, get_data, is_sha512_checksum,
                  pipeline, prepare_print, print_errors, read_cache_file,
                  read_configuration_file, read_remote_files, read_yaml_file,
                  save_cache, transform_cache_to_data_object, write_cache)
from .cli import CliInterface
from .exceptions import (BinaryDoesNotExist, IncoherentData,
                         IncoherentProgrammingLanguageValue, InvalidCache,
                         InvalidCommonDataStructure, InvalidConfiguration,
                         InvalidOutput, NotAChecksum)
