# APmaker

APmaker is a Python based toolset to assist with the creation of [autoprotocol](http://autoprotocol.org/) [JSON files](https://www.json.org/).

## Purpose

Designing, building and debugging robotically controlled experiments can quickly turn into a daunting task, especially if the operation includes more than a couple of assay conditions, microtiter plates, cell lines, reagents, or other components. [Autoprotocol](http://autoprotocol.org/) has been developed to assist scientists with the establishment of well-defined and repetitive equipment controlling protocols. Creating the JSON instruction sets for the robotic interfaces can be completed using the Python library, but the library only provides methods and functions for outputting the raw JSON commands. 

The APmaker tools add additional Python objects and tools to facilitate the design of large-scale experiments and to assist with the generation of sophisticated JSON pipelines.

## Dependencies

APmaker support Python 3.5+

Installation requires: [autoprotocol](http://autoprotocol.org/) and [NumPy](https://www.numpy.org/)

## Instructions

To use AP Maker, install this code base and run the following command:

      `python ap_maker.py --plates <csv file for plate list>
                          --logging <log level: info, debug>`
