  .. _ref_guide_wsl:


ANSYS on WSL and docker 
########################

This guide shows you how to use Ansys products, more specifically PyMAPDL, in the Windows Subsystem for Linux (WSL).
WSL is a compatibility layer for running Linux binary executables natively on Windows 10, Windows 11, and Windows Server 2019 
(`Wikipedia-WSL <https://en.wikipedia.org/wiki/Windows_Subsystem_for_Linux>`_).

This guide walks you through the installation of WSL in Windows, and shows how to use it together with ANSYS, PyMAPDL and docker.

For more information about WSL please visit `What is the Windows Subsystem for Linux? <https://docs.microsoft.com/en-us/windows/wsl/about>`_. 

.. warning:: **Disclaimer:** This guide is still in Alpha state. Please proceed with caution. 


.. warning:: This guide hasn't been tested with a VPN connection.


Running ANSYS in WSL 
*********************

Install WSL2
=============

Follow the instructions in the official Microsoft website `Install WSL <https://docs.microsoft.com/en-us/windows/wsl/install/>`_ .

It is recommended you use WSL2 over WSL1. 

Install CentOS7 WSL Distribution
=================================

This is the recommended distribution to work with PyANSYS.

You can install it using an unofficial WSL distribution from `<https://github.com/wsldl-pg/CentWSL/>`_ .

.. note:: 

    It seems the above project has been discontinued.
    A more updated CentOS distribution can be found in `<https://github.com/mishamosher/CentOS-WSL/>`_ , however it has not been tested yet.


You can use Ubuntu if you wish to do so, but it has not been tested yet.


Install ANSYS in WSL CentOS7
=============================

Prerequisites
--------------
If you are using CentOS 7, before installing ANSYS you need to install some required libraries:

.. code:: bash
   
   yum install openssl openssh-clients mesa-libGL mesa-libGLU motif libgfortran


In case of Ubuntu, please follow the specific instructions in `Running MAPDL: Ubuntu <https://mapdldocs.pyansys.com/getting_started/running_mapdl.html#ubuntu/>`_ .


Install ANSYS
--------------

To install ANSYS in WSL Linux, you need to follow the next steps.

1. Download ANSYS Structures image from customer portal (`Current Release <https://download.ansys.com/Current%20Release>`_). 
   If you are using windows to download it, you can later copy it from it to WSL (recommended).

2. Decompress the source code file (tar.gz) by using 

   .. code:: bash
   
       tar xvzf STRUCTURES_2021R2_LINX64.tgz


3. Install ANSYS by going into the uncompressed folder and type:

   .. code:: bash
   
       ./INSTALL -silent -install_dir /usr/ansys_inc/ -mechapdl

   where: 

   - ``-silent`` : Initiates a silent installation (No GUI).

   - ``-install_dir /path/`` : Specifies the directory to which the product or license
     manager is to be installed. 
     If you want to install to the default location, you can omit the ``-install_dir`` argument. 
     The default location is ``/ansys_inc`` if the symbolic link is set; otherwise, it will default to ``/usr/ansys_inc``.

   - ``-<product_flag>`` : Specifies one or more products to install specific products. 
     If you omit the -product_flag argument, all products will be installed. 
     See the list of valid product_flags in the Chapter 6 in *ANSYS Inc. Installation Guides* PDF. 
     In this case, only mechanical (`-mechapdl`) is needed.

You could install it directly in ``/ansys_inc`` if you wish, or in ``/usr/ansys_inc`` and then create a symbolic link using:

.. code:: bash

    ln -s /usr/ansys_inc /ansys_inc

By default, PyMAPDL expects ANSYS executable being in ``/usr/ansys_inc``, so whether you install it there or not, it is recommended you link that directory, using symbolic link, to your ANSYS installation directory (``/*/ansys_inc``).


Post installation setup
========================

Opening ports
--------------

**Theory:** 
You should open the ports ``1055`` and ``2325`` for the license server communication in `Windows Firewall Advanced`.
You can see the steps in `How to open port in Windows 10 Firewall <https://answers.microsoft.com/en-us/windows/forum/all/how-to-open-port-in-windows-10-firewall/f38f67c8-23e8-459d-9552-c1b94cca579a/>`_ . 

**Reality:**
This works if you want to run a docker image using WSL Linux image to host that docker image.
The docker image will successfully communicate with the Windows License Server using these ports if using ``'-p'`` flag when running the docker image and if having those ports open.
See `Running ANSYS in a local docker`_ .


If you wish to run ANSYS in the CentOS7 image and use the Windows License Server, opening the ports might not work properly, since Windows firewall seems to block all traffic coming from WSL. 
It is recommended (for security purposes), you still try to open ``1055`` and ``2325`` ports in the firewall and check if your ANSYS installation can communicate with Windows Hosts.
If you are having problems after setting the firewall rules, you might have to disable Windows Firewall for the WSL ethernet virtual interface.
This might pose some unknown side effects and security risk so use it with caution.
See `Disabling Firewall on WSL Ethernet`_


Setting up an environmental variable in WSL that points to Windows Host License Server
---------------------------------------------------------------------------------------

Windows host IP is given in the WSL file ``/etc/hosts`` before the name ``host.docker.internal``.


.. note:: This ``host.docker.internal`` definition might not be available if docker is not installed. 


**Example /etc/hosts/ file**

.. code-block:: bash
   :emphasize-lines: 7

   # This file was automatically generated by WSL. To stop automatic generation of this file, add the following entry to /etc/wsl.conf:
   # [network]
   # generateHosts = false
   127.0.0.1       localhost
   127.0.1.1       AAPDDqVK5WqNLve.win.ansys.com   AAPDDqVK5WqNLve

   192.168.0.12    host.docker.internal
   192.168.0.12    gateway.docker.internal
   127.0.0.1       kubernetes.docker.internal

   # The following lines are desirable for IPv6 capable hosts
   ::1     ip6-localhost ip6-loopback
   fe00::0 ip6-localnet
   ff00::0 ip6-mcastprefix
   ff02::1 ip6-allnodes
   ff02::2 ip6-allrouters

You can add the next lines to you WSL ``~/.bashrc`` file to create an environment variable with that IP:

.. code:: bash

    winhostIP=$(grep -m 1 host.docker.internal /etc/hosts | awk '{print $1}')
    export ANSYSLMD_LICENSE_FILE=1055@$winhostIP


Running ANSYS in a local docker
********************************

To run a docker image, you need to follow all the previous steps detailed in `Running ANSYS in WSL`_ .

Additionally, to run a docker PyMAPDL image, use the next command:

.. code:: pwsh

    docker run -e ANSYSLMD_LICENSE_FILE=1055@host.docker.internal --restart always --name mapdl -p 50053:50052 docker.pkg.github.com/pyansys/pymapdl/mapdl -smp > log.txt

Successive runs should restart the container or just delete it and rerun it using:

.. code:: pwsh

    docker stop mapdl
    docker container prune

    docker run -e ANSYSLMD_LICENSE_FILE=1055@host.docker.internal --restart always --name mapdl -p 50053:50052 docker.pkg.github.com/pyansys/pymapdl/mapdl -smp > log.txt


This will create a log file (``log.txt``) in your current directory location.


.. note:: Please make sure your ports (``50053``) are open in your firewall.

It is recommended to do a script file (batch ``'.bat'`` or powershell ``'.ps'`` files) to run the above commands, all at once.

Please do notice that we are mapping the iWSL nternal gRPC port (``50052``) to a different Windows host port (``50053``) to avoid ports conflicts.

This image is ready to be connected to from WSL or Windows Host but the port and IP should be specified as:

.. code:: python

    from ansys.mapdl.core import launch_mapdl

    mapdl = launch_mapdl(ip='127.0.0.1', port=50053, start_instance=False) 

Or:

.. code:: python 

    from ansys.mapdl.core import Mapdl
    
    mapdl = Mapdl(ip='127.0.0.1', port=50053)


You can also specified them using environment variables which are read when launching the MAPDL instance.

.. code:: bash

    export PYMAPDL_START_INSTANCE=False
    export PYMAPDL_PORT=50053
    export PYMAPDL_IP=127.0.0.1


Launch docker with UPF capabilities:
======================================

In case you want to specify a custom Python UPF routine, you need to have the environment variables ``ANS_USER_PATH`` and ``ANS_USE_UPF`` defined. 
The former should be equal to the path where the UPF routines are located, and the latter should be equal to ``TRUE``.

In the WSL you can do this using:

.. code:: bash

    export ANS_USER_PATH=/home/user/UPFs # Use your own path to your UPF files.
    export ANS_USE_UPF=TRUE

Then you can run the docker image using:

.. code:: bash

    docker run -e ANSYSLMD_LICENSE_FILE=1055@host.docker.internal -e ANS_USER_PATH='/ansys_jobs/upf' -e ANS_USE_UPF='TRUE' --restart always --name mapdl -p 50053:50052 docker.pkg.github.com/pyansys/pymapdl/mapdl -smp  1>log.txt

.. warning:: The use of UPFs with docker images or PyMAPDL is still in Alpha state.


Notes
======

The specified IP (``127.0.0.1``) in `Running ANSYS in a local docker`_ is the IP of WSL CentOS from the WSL perspective.
Whereas the Windows host IP is (normally) ``127.0.1.1``.
Docker build the images (PyMAPDL images) using the WSL distribution as base. 
Hence we have a PyMAPDL running on a Linux WSL distribution which is running on a Windows host.
Since the docker image shares resources with WSL, it does also share the internal IP with the WSL distribution.


Other useful stuff
*******************


Other ANSYS installation flags
===============================


``-licserverinfo``
-------------------

Obtained from:

.. code:: bash
    
    ./INSTALL --help

Or:

.. code:: bash

    cat ./INSTALL

and inspecting the last lines of the ``INSTALL`` file.

- ``-licserverinfo`` : Specifies information to be used by the client for the license server. 
  Valid only in conjunction with a silent installation (INSTALL). 
  
  The format is:

  + For single license server:

    .. code:: bash

        -licserverinfo LI_port_number:FLEXlm_port_number:hostname
    
    Example:
    
    .. code:: bash

        ./INSTALL -silent -install_dir /ansys_inc/ -mechapdl -licserverinfo 2325:1055:winhostIP

  + Three license servers:

    .. code:: bash

        -licserverinfo LI_port_number:FLEXlm_port_number:hostname1,hostname2,hostname3
    
    Example:
    
    .. code:: bash

        ./INSTALL -silent -install_dir /ansys_inc/ -mechapdl -licserverinfo 2325:1055:abc,def,xyz

``-lang``
-----------                  
Specifies a language to use for the products installation.


``-productfile``
------------------
You can specify an options file that lists the products you want to install.
To do so, you must provide a full path to a file containing desired products.


Regarding IPs in WSL and Windows host
======================================

Theory:
--------

You should be able to access Windows host using IP specified in ``/etc/hosts`` which normally is ``127.0.1.1``. This means that the local WSL IP is ``127.0.1.1``.

Reality
--------

It is almost impossible to use ``127.0.1.1`` for connecting to the Windows host. However it is possible to use ``host.docker.internal`` hostname in the same file (``/etc/hosts``).
This is an IP which is randomly allocated, which is an issue when you define the License Server. However if you update the ``.bashrc`` as mentioned before, this issue is solved.



Disabling Firewall on WSL Ethernet
===================================

.. code:: pwsh

    Set-NetFirewallProfile -DisabledInterfaceAliases "vEthernet (WSL)"

This will show a notification, but this not:

.. code:: pwsh

    powershell.exe -Command "Set-NetFirewallProfile -DisabledInterfaceAliases \"vEthernet (WSL)\""


Link: `<https://github.com/cascadium/wsl-windows-toolbar-launcher#firewall-rules/>`_

Windows 10 Port forwarding
===========================


Link ports between WSL and Windows:
------------------------------------

.. code:: pwsh

    netsh interface portproxy add v4tov4 listenport=1055 listenaddress=0.0.0.0 connectport=1055 connectaddress=XXX.XX.XX.XX


PowerShell command to view all forwards
----------------------------------------

.. code:: pwsh

    netsh interface portproxy show v4tov4


Delete port forwarding
-----------------------

.. code:: pwsh

    netsh interface portproxy delete v4tov4 listenport=1055 listenaddres=0.0.0.0 protocol=tcp


Reset windows network adapters
===============================

.. code:: pwsh

    netsh int ip reset all
    netsh winhttp reset proxy
    ipconfig /flushdns
    netsh winsock reset


Restart WSL service
====================

.. code:: pwsh

    Get-Service LxssManager | Restart-Service

Kill all the processes with given name
=======================================

.. code:: pwsh

   Get-Process "ANSYS212" | Stop-Process


Install xvfb in CentOS7
========================

It is needed if we want to replicate the CI/CD behaviour (See ``.ci`` folder).

.. code:: bash

   yum install xorg-x11-server-Xvfb


Notes
******

- The PyMAPDL does only work for shared-memory parallel (SMP) when running it in WSL, hence this flag (``-smp``) should be included.

- Remember there are some incompatibilities between VPN and INTEL MPI. In that case use ``-mpi msmpi`` flag when calling mapdl.

