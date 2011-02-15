---------------------------------
Installation procedure for Ubuntu
---------------------------------

Command-line based installation (recommended)
---------------------------------------------

Enter following commands on the terminal::

  $ sudo apt-add-repository ppa:openhri/ppa
  $ sudo apt-get update
  $ sudo apt-get install openhriaudio openhrivoice seatsat

This is it!

Proceed to :doc:`step2`.

GUI based installation
----------------------

OpenHRI software repository can be registered using the Synaptic Package Manager.

1. Open the "Synaptic Package Manager" from "System" > "Systems Management". (Password required)

2. Follow "Setting (S)" > "Open Repository (R)" > "Other Software" (or "Third-party Software") tab.

   .. image:: ss-inst02b.png

   .. image:: ss-inst03b.png

3. Click "APT line:" and add the following address::

     http://ppa.launchpad.net/openhri/ppa/ubuntu lucid main deb

   Click "Add source (A)".

   .. image:: inst1.png

   .. note:: this address is for ubuntu 10. 04. OpenHRI binary packages currently only support ubuntu 10.04.

4. Click "Reload" to download the package information.

   .. image:: inst3.png

Repository registration is finished. Let’s install OpenHRI components.

5. Select the items by using the quick search box. Enter "openhriaudio", "openhrivoice", "seatsat" on the search box.  Use the right-click menu to install.

   Quick search box

   .. image:: inst9.png

   Right click the left check box and choose "install".

   .. image:: inst10.png

   Click the "apply" button to begin the installation.

   .. image:: inst11.png

Component installation now finished. Let's check the behavior of the component.

Proceed to :doc:`step2`.
