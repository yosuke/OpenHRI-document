------------------------
Scripting Dialog Manager
------------------------

Introduction
============

Dialog manager is the core part of the dialog system which defines
interactive behavior of the system.

OpenHRI provides two dialog manager that you can chose at your
preference.


SEAT: Simple Dialog Manager
===========================

SEAT (Speech Event Action Transfer) is a simple state-transition model
based dialog manager. You can define the behavior of the system by
using following XML tags.


Tags
----

- Adaptor definition

  SEAT has an adaptor mechanism which gives mappings between the name
  and the actual connection method (RTM and socket). The adaptor
  mechanism abstracts the hardware configuration of the system and
  assists the reuse of the dialog logic.

  general
    This tag is used to indicate the adaptor definition part.

  agent
    Map of the name and actual connection method. Attribute "type"
    can take "rtcin", "rtcout" or "socket". When type is defined as
    "rtcin" or "rtcout", you can define "datatype" attribute (see RTM's
    specification for standard data types). When type is defined as
    "socket", you can define "host" and "port" attributes.

- Script definition

  state
    Indicates a state in state-transition model.

  rule
    Defines set of keywords and commands.

  key
    Keywords to be matched to the inputs.

  command
    Command to be executed when the keyword matches the input.

  statetransition
    Transit to different state.

Example
-------

.. literalinclude:: sample-en.seatml
   :language: xml

Validation tool
---------------

You can validate your script in SEATML format by using "validateseatml" tool.

You can use the validation tool by simply entering the following command::
  
  $ validateseatml [scriptfile]

If the script is correct, you will get the following output::
  
  $ validateseatml sample-en.seatml
  validating script file sample-en.seatml...
  script file is valid.

If the script is not correct, you will get error messages for example as follows::

  $ validateseatml sample-invalid.seatml
  validating script file sample-invalid.seatml...
  [error] invalid script file.
  Element 'transition': This element is not expected. Expected is one of ( command, statetransition )., line 23

Visualization tool
------------------

OpenHRI has more powerful tool to validate the structure of the
SEATML script.  "seatmltographviz" tool can visualize the script
in graph to check the correctness.

To draw the graph, enter following command::

  $ seatmltographviz sample-en.seatml | dot -Txlib

For example, you will get the following output:

  .. image:: sample-script-en.png

Soar: General Artificial Intelligence
=====================================

Soar ( http://sitemaker.umich.edu/soar/home ) is one of the most
popular software to realize production system based AI.

OpenHRI provides a wrapper to embed Soar into RTM based systems as a
component.

More documents T.B.D
