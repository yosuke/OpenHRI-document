------------------------------------------------------------------
Step2: Basic Usage of RT-SystemEditor and Testing Audio Components
------------------------------------------------------------------

In this step, we will directly connect the audio input and the audio output component and verify that the components are working properly.

Preparation
-----------

1. Download and install eclipse with RT-SystemEditor (please see here for the instructions).

2. Prepare a microphone and a speaker (earphone and headphone) connect to PC.

3. Create rtc.conf file.

  Create a configuration file “rtc.conf” and save to working directory. Content of rtc.conf is as follows

  .. code-block:: guess  

     corba.nameservers: localhost:9876
     naming.formats: %n.rtc

4. Launch the name server.

  Start the name server with port number as specified in rtc.conf file. (In the above example 9876)
  ::
  
  $ rtm-naming 9876

   .. image:: ss_run011.png

5. Launch eclipse with RT-SystemEditor installed.

Basic usage of the RT System Editor
-----------------------------------

In this section, we describes the basic usage of the RT System Editor and test audio components.

1. Launch AudioInput and AudioOutput components.

   .. warning::
   
      If you are using ubuntu 9.10 or later, please use PulseAudioInput and PulseAudioOutput components.
      If you are using version older than 9.10, please use PortAudioInput and PortAudioOutput components.

   ubuntu9.10 or later: enter the following commands on each terminal.
     ::
 
     $ pulseaudioinput

     ::
     
     $ pulseaudiooutput

   older version: enter the following commands on each terminal.
     ::

     $ portaudioinput

     ::
     
     $ portaudiooutput

2. Open the eclipse RT-SystemEditor perspective.

   .. image:: ss_run03.png

   .. image:: ss_run04.png

3. Select "Add name servers" button and register the name servers specified by the rtc.conf file.

   (In above example "localhost:9876")

   .. image:: step2_6.png

   .. image:: step2_7.png

4. Click the icon on the left to open the new editor screen.

   .. image:: ss_step2_3.png

5. From the name service views (left panel) drag and drop the AudioInput (and AudioOutput) component to the editor screen.

   .. image:: ss_run06.png

6. Connected the dataport between the components.

   Click the connector part of the data port.

   .. image:: ss_run09.png

   Drag to the other data port.

   .. image:: ss_run10.png

   When you drop the link, a connection settings dialog will appear. No configuration change is required.

   .. image:: ss_run11.png

   Press OK (connector changes to green color)

   .. image:: ss_run12.png

Activate the component and check the operation
----------------------------------------------

7. Activate all components.

   Press “All Activate” button.

   .. image:: ss_step2_1.png

   AudioInput and AudioOutput activate and change from blue to green.

   .. image:: ss_step2_2.png

8. Verify the operation.

   Verify that sound input entered from the microphone is played from speakers.

In this step we have learned basic usage of the RT System Editor through testing the audio components.

Proceed to :doc:`step3`.
