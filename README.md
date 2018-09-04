![DARMA](https://github.com/darma-tasking/darma-frontend/blob/devel/logo.png)

# DARMA (Distributed, Asynchronous, Resilient Models for Applications) 

#### Copyright (c) 2017, Sandia National Laboratories
Sandia National Laboratories is a multimission laboratory managed and operated
by National Technology and Engineering Solutions of Sandia, LLC., a wholly 
owned subsidiary of Honeywell International, Inc., for the U.S. Department of 
Energy's National Nuclear Security Administration under contract DE-NA0003525.

---

DARMA (Distributed, Asynchronous, Resilient Models for Applications) is a
data-effects programming model for extracting concurrency automatically
from C++ applications using metaprogramming. The model is designed for those
interested in both on-node tasking (MPI+X) or for distributed memory tasking.

The DARMA packages are not yet part of the main Spack repository and
are in flux. However, this repository can be downloaded and added to your
local Spack manager. To do so just download the Git repo and run:

````
spack repo add ${path_to_repo}
````

Once Spack has been made aware of the DARMA spack packages, you can run:

````
spack install darma-futures
````

To install the DARMA futures header library and MPI backend.
Note, DARMA requires C++14 support. As such, we require GCC >= 5, Clang >= 3.6,
and ICC >= 18. Once installed, DARMA applications can build against the installed CMake package. 


[![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)

Under the terms of Contract DE-NA0003525 with Sandia Corporation, 
the U.S. Government retains certain rights in this software.

