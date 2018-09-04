##############################################################################
# Copyright (c) 2013-2017, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/spack/spack
# Please also see the NOTICE and LICENSE files for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################

from spack import *

class DarmaSerialization(CMakePackage):
    """A serialization library for migrating data between processes
       in DARMA programs
    """

    homepage = "https://github.com/DARMA-tasking"
    url      = "https://github.com/DARMA-tasking/darma-serialization"

    version('1.0',
        git='https://github.com/DARMA-tasking/darma-serialization',
        branch='devel')

    depends_on('darma-utility@1.0')

    def cmake_args(self):
      import os
      spec = self.spec
      if self.compiler.name == "clang":
        if self.compiler.version < Version("3.6"):
          raise Exception("DARMA requires Clang version >= 3.6")
      elif self.compiler.name == "gcc":
        if self.compiler.version < Version("5"):
          raise Exception("DARMA requires GCC version >= 5")
      else:
        raise Exception("Incompatible compiler: need GCC >= 5, Clang >= 3.9")

      utilityPath=os.path.join(spec['darma-utility'].prefix, "cmake")
      args = [
        '-DDarmaUtility_DIR=%s' % utilityPath
      ]
      return args


