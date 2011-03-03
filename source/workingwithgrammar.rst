---------------------------------------
Working with Speech Recognition Grammar
---------------------------------------

Introduction
============

Speech recognition grammar defines syntactical structure of the words
to be recognized.

Julius speech recognition component provided by OpenHRI uses W3C-SRGS
format to define the speech recognition grammar.

In this section, we explain the W3C-SRGS format and introduce the
tools provided by OpenHRI to help authoring the grammar.

W3C-SRGS Grammar
================

W3C-SRGS (Speech Recognition Grammar Specification) is one of the
standard to define the speech recognition grammar. It uses XML format
with following tags to 

Tags
----

lexicon
  Indicates URI of W3C-PLS lexicon (see next section). Required for
  every grammar.

rule
  Indicates set of grammar distinguished by an ID. This will be
  used to reference the grammar from the other grammar or to switch
  the active grammar recognized by the Julius speech recognition
  component.

item
  Indicates a word or a sentence (space separated words) to be
  recognized. "repeat" property can be used.

one-of
  Indicates the child items are all acceptable.

ruleref
  Import the rule defined by the uri.

Example
-------

.. literalinclude:: sample-en.grxml

W3C-PLS Lexicon
===============

W3C-PLS (Pronunciation Lexicon Specification) is one of the
standard to define the speech recognition lexicon. It uses XML format
with following tags to 

Tags
----

lexeme
  Set of grapheme and phoneme.

grapheme
  Indicates how you write the word.

phoneme
  Indicates how you pronounce the word.

Example
-------

.. literalinclude:: sample-lex-en.xml

Tools
=====

Validation tool
---------------

You can validate your grammar in W3C-SRGS format by using "validatesrgs" tool.

You can use the validation tool by simply entering the following command::
  
  $ validatesrgs [grammarfile]

If the grammar is correct, you will get the following output::
  
  $ validatesrgs sample-en.grxml
  Validating SRGS file sample-en.grxml...
  SRGS file is valid.
  Validating PLS file sample-lex-en.xml...
  PLS file is valid.

If the grammar is not correct, you will get error messages for example as follows::

  $ validatesrgs sample-invalid.grxml
  Validating SRGS file sample-invalid.grxml...
  [error] Invalid SRGS file.
  Element '{http://www.w3.org/2001/06/grammar}one-of': Missing child element(s). Expected is ( {http://www.w3.org/2001/06/grammar}item )., line 12

Visualization tool
------------------

OpenHRI has more powerful tool to validate the structure of the
W3C-SRGS grammar.  "juliustographviz" tool can visualize the grammar
in graph to check the correctness.

To draw the graph, enter following command::

  $ srgstojulius sample-en.grxml | juliustographviz | dot -Txlib

For example, you will get the following output:

  .. image:: sample-grammar-en.png


Lexicon generation tool
-----------------------

After you have finished writing W3C-SRGS grammar, you also have to
prepare W3C-PLS lexicon.

OpenHRI provides a tool to automatically generate W3C-PLS lexicon from
the W3C-SRGS grammar.

The "srgstopls" tool can be used as follows::
  
  $ srgstopls sample-en.grxml > sample-lex-en.xml

English lexicon (by using julius-voxforge dictionary) and Japanese
lexicon (by using julius-runkit dictionary) are supported by this tool
at the moment.

.. note:: Words not in the dictionary remains blank in output XML
   file. You should always check the output XML and fill in manually
   for such words.
