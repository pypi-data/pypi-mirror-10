.. _help:

==============
SamSifter Help
==============

.. .. contents:: Contents

Manual
======

.. toctree::
    :maxdepth: 4

    manual

Frequently Asked Questions
==========================

None so far...

Known Bugs
==========

Please report new bugs to samsifter@biohazardous.de.

Bugs in SamSifter
-----------------

.. Currently no known bugs specific to SamSifter.
.. Please report new bugs to samsifter@biohazardous.de.

* The filter direction parameter of some filters, especially the 'Filter taxa by
  list' filter, should be moved from the optional to the required tab to avoid
  confusion, eg. when running the human pathogen screening workflow.
* Exported bash scripts will attempt to execute SAM2RMA even if this option
  was disabled in the GUI. In combination with the 'Stop on error' option
  the script will fail silently on systems without SAM2RMA in their ``$PATH``
  because of the ``which sam2rma`` in the bash script's first lines. Workaround:
  comment out the optional SAM2RMA commands or install MEGAN incl. SAM2RMA.

Bugs in Tools used by SamSifter
-------------------------------

* BetterRMDup fails when processing MALT'ed files. This is actually a bug of
  the SAM parsing library used in BetterRMDup that does not handle the custom MALT
  ``@mm`` record properly. The bug has been reported and will be fixed in a future
  version.
* SAMtools ``view`` reports a possibly truncated file and complains about a
  missing EOF marker. This is likely a bug in either
  MALT and/or SAMtools ``view`` which can be safely ignored. See
  http://sourceforge.net/p/samtools/mailman/samtools-help/thread/4EC52844.3090808@broadinstitute.org/
  for details. It is caused by a missing compression flag when processing
  uncompressed files.
* SAMtools ``view`` complains about inconsistency of the sequence length when
  compared to the CIGAR string. This is a bug in MALT 0.0.12 that has been
  reported. Please re-MALT your files with a newer version or remove the
  affected reads manually.
