===============================
SeedMe OpenMM
===============================

.. image:: https://img.shields.io/travis/sqamara/seedmeopenmm.svg
        :target: https://travis-ci.org/sqamara/seedmeopenmm

.. image:: https://img.shields.io/pypi/v/seedmeopenmm.svg
        :target: https://pypi.python.org/pypi/seedmeopenmm


SeedMe OpenMM contains a reporter that connects OpOpenMM and SeedMe

* Free software: BSD license
* Documentation: https://seedmeopenmm.readthedocs.org.

Features
--------

The SeedMeStateDataReporter is an adaptation of the OpenMM StateDataReporter such that it functions in the same way, outputting information about the simulation, but reports the information in the form of tickers in a new collection on SeedMe.

Installation
--------

Instal OpenMM
    conda install -c https://conda.binstar.org/omnia openmm 
Perform the SeedMe Command Line setup 
    https://www.seedme.org/help/use/command-line/get-seedme-client
Get your API key 
    https://www.seedme.org/help/use/get-apikey

Usage
--------

The `SeedMeStateDataReporter` is used in the same way as the `StateDataReporter`.  Create a SeedMeStateDataReporter, then add it to the Simulation's list of reporters.  The set of data to write is configurable using boolean flags passed to the constructor.  By default the data is written in comma-separated-value (CSV) format, but you can specify a different separator to use.

An example simulation can be found in the examples_ folder.

.. _examples: https://github.com/paesanilab/seedmeopenmm/tree/master/examples

Link to example output https://www.seedme.org/node/40083
