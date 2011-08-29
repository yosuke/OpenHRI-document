--------------------------
Usage of  World Simulators
--------------------------

OpenHRI has a virtual simulation environments to test human robot interaction function without using real robot.

In this chapter we explain the usage of the world simulators.

   .. image:: blocksworld.png

Install
-------

Windows platform
================

1. Install OpenHRIWorlds package

  Download and run the installer from following URL:
  
  http://openhri.net/getinstaller.php
  
  The installer will show the current available packages. Select "OpenHRIWorlds" package.

2. Install OpenHRPSDK
  
  Download and run the "OpenHRP SDK Windows" installer available from following URL:
  
  http://openrtp.info/openhrp3/jp/download.html

Ubuntu platform
===============

Ubuntu version is currently not available.


BlocksWorld Simulator
---------------------

In BlocksWorld simulator, we can examine the scenario of handling boxes using Mitsubishi Heavy Industries PA10 arm robot.

Running the simulation
======================

1. Run OpenHRP

  Open the explorer and double click the "GrxUI.exe" in "C:\\Program Files (x86)\\OpenHRPSDK\\GrxUI" folder.

  .. note:: We recommend to create a shortcut of GrxUI.exe on the desktop for later use.

2. Run BlocksWorld simulator

  Choose "BlocksWorld" from "Start Menu > OpenHRI > worlds".

Please confirm multiple blocks and PA10 arm will show up on the view panel of OpenHRP (the robot should perform single pick-and-place demonstrative movement).

.. note:: When the BlocksWorld simulator fails to run

  It may happen that the BlocksWorld simulator fails to run (we are still investigating the reason yet). In that case, please follow the next procedure:

  1. Load sample OpenHRP project.
       Select "GrxUI > Read Project" from the menu. Load "PA10Sample" from "C:\\Program Files (x86)\\OpenHRPSDK\\share\\OpenHRP-3.1\\sample\\project".

  2. Run OpenHRP simulation once.
        Press "Start" button to run the simulation (you can stop any time).

  3. Clear the OpenHRP view.
        Select "GrxUI > New Project" from the menu.

  4. Run the BlocksWorld simulator.
        Now, run the BlocksWorld simulator again and check the behavior.


Function of the BlocksWorld Component
=====================================

BlocksWorld simulator provides OpenRTM port interface to communicate with the other component.

PA10 arm of the BlocksWorld simulator can be controlled by sending following text commands to the "command" port:

grasp
  Grasp hand to pick object.

release
  Release hand to place object.

moveHandToBox [name]
  Move hand above the block specified by the [name]. You can specify "box1", "box2" and "box3".

moveHandXY [X] [Y]
  Move hand to [X][Y] meters relative to the current position.

Test Script
===========

Here, we show the example of controlling PA10 arm using voice commands.

1. Speech recognition grammar:

  .. literalinclude:: blocksworld-en.grxml
     :language: xml

2. Dialogue script:

  .. literalinclude:: blocksworld-en.seatml
     :language: xml

Load each files to Julius component and SEAT component. And connect "command" port of SEAT component to "command" port of BlocksWorld component.
