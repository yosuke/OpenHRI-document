----------------------------------
Step5: Extending the Dialog System
----------------------------------

Here, we connect our dialog system to the external components.

Edit the script given to the dialog manager as follows.
  
  sample-en2.seatml	   

  .. literalinclude:: sample-en2.seatml

Stop the SEAT components (by entering Ctrl + C in the terminal) and start again with the edited script.

  ::

  % seat sample-en2.seatml

Dialog manager starts with one more output ports.

  .. image:: step5_02.png

You can give command to external components by connecting to this port.

For example, we can connect the components shown in the following script.

  ConsoleOut.py	   

  .. literalinclude:: ConsoleOut.py

This component shows the command to the terminal. Please check the received commands, by saying "Hello" "Bye" to the microphone.

By editing the script given to the dialog manager, you can create a port you like and send data of any type. By using this feature, for example, you can connect the dialog system to the actual robot to send command "moving forward" or "retreat".
