----------------------------------------
Step3: Testing Voice Synthesis Component
----------------------------------------

Here we will learn how to use text-to-speech component.

Preparation
-----------

1. Preparation of test components

  Test component will output a text data in some period. Please create a test program as follows.

  .. literalinclude:: ConsoleIn.py

  We will call this component “ConsoleIn component” hereafter..

2. Prepare the rtc.conf

  You may copy the setting used in :doc:`step2`.

Test procedures
---------------

1. Start the ConsoleIn and Festival components.

  Open two terminals and enter following commands respectively
    ::

    % python ConsoleIn.py
  
    ::
  
    % festivalrtc

  Make sure you start naming service view component is displayed.

  .. image:: ss_jtalk01.png

2. Place the ConsoleIn and Festival component to RT System Editor.

  Drag and drop the components to the editor panel.

  .. image:: ss_jtalk02.png

3. Remove the links between AudioInput-AudioOutput.

  Select the link and choose "Delete" from the right-click menu.

  .. image:: ss_jtalk03.png

4. Connect the ConsoleIn, Festival, and AudioOutput, respectively.

  * Connect ConsoleIn output port and Festival input port.

  * Connect the Festival “result” output port  and AudioOutput input port.

  (Please be careful not to connect to the different port. )

  .. image:: ss_jtalk04.png

5. Activate and verify the behavior.

  Press "All Activate" button to activate all the components.

  Verify the text you set the ConsoleIn component is synthesized as audio.

In the next step, we will create a complete dialog system by connecting the speech recognition component.

Proceed to :doc:`step4`.

