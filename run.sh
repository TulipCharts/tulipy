#!/bin/bash
set -e

prj_home=$( cd "$( dirname $0 )" && pwd )
cd ${prj_home}

export PATH=/opt/gcc-5.4.0/bin:$PATH
export LD_LIBRARY_PATH=/opt/gcc-5.4.0/lib64:$LD_LIBRARY_PATH

export PATH=/opt/anaconda3/bin:$PATH

$*