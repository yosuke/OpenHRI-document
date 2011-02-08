-----------------------------
Step4: Creating Dialog System
-----------------------------

Let’s create a simple dialog system by combining speech recognition component and the dialog manager component.

Preparation
-----------

1. Preparation of the speech recognition components

  We have to provide a speech recognition grammar to run the speech recognition component.

  Create the following two text data.

  sample-en.xml

  .. literalinclude:: sample-en.xml

  sample-lex-en.xml

  .. literalinclude:: sample-lex-en.xml


2. Dialog Manager component preparation

  Create the following text data.

  sample-en.seatml
  
  .. literalinclude:: sample-en.seatml	   


3. Prepare the setting file rtc.conf

  You may copy the setting used in :doc:`step2`.

Test procedures
---------------

1. Start the SEAT and Julius components.

  ::
  
  $ juliusrtc sample-en.xml

  ::

  $ seat sample-en.seatml

  Make sure the component is displayed in Eclipse name service view.

  .. image:: step4_11.png

2. Drag and drop SEAT and Julius components to the editor panel.

3. Connect between the components.

  * Remove the link between ConsoleIn component and Festival component.
  * Create a link between AudioInput output port and Julius input port.
  * Create a link between Julius “result” output port and SEAT input port.
  * Create a link between SEAT output port and Festival input port.

  Make sure that everything is connected!

  .. image:: step4_10.png

4. Activate and verify the behavior.

  Press "All Activate" button.

  Check to receive the response by speaking "Hello" or "Goodbye" in front of the microphone.

  .. note:: If it does not work:

     Check the following points.

     Check environmental noises
       Check whether you have the background or ambient noise. If you want to recognize the  noisy environments, consider using headset microphone or directional microphones.

     Adjust audio input volume
       Speech recognition will show low performance when the audio volume is too large or too small (if you see the warnings such as "Warning: strip to..." in the terminal where you have launched julius component, audio volume  may not appropriate). Adjust size of volume by looking at the volume meter.

Proceed to :doc:`step5`.
