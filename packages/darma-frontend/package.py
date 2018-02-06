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

class DarmaFrontend(CMakePackage):
  """A header library implementing the DARMA data effects
     programming model.  This should be coupled to one of 
     the backends for development and testing
  """

  homepage = "https://github.com/DARMA-tasking"
  url      = "https://github.com/DARMA-tasking/darma-frontend"


  version('0.6',
        git='https://github.com/DARMA-tasking/darma-frontend',
        branch='master')

  #version('0.6.0', 'b7086e97c4e8f72fd8619082865909f10d3d3bd1')

  # No dependencies header-only library
  # depends_on()

  def cmake_args(self):
    if self.compiler.name == "clang":
      if self.compiler.version < Version("3.6"):
        raise Exception("DARMA requires Clang version >= 3.6")
    elif self.compiler.name == "gcc":
      if self.compiler.version < Version("5"):
        raise Exception("DARMA requires GCC version >= 5")
    else:
      raise Exception("Incompatible compiler: need GCC >= 5, Clang >= 3.9")
    spec = self.spec
    return []

