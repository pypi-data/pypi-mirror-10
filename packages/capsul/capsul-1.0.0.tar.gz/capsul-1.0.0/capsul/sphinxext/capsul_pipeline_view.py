#! /usr/bin/env python
##########################################################################
# CAPSUL - CAPS - Copyright (C) CEA, 2013
# Distributed under the terms of the CeCILL-B license, as published by
# the CEA-CNRS-INRIA. Refer to the LICENSE file or to
# http://www.cecill.info/licences/Licence_CeCILL-B_V1-en.html
# for details.
##########################################################################

""" Script to auto-generate pipeline png representation.
"""

# System import
import os
from optparse import OptionParser
import sys
import logging
import tempfile
import subprocess

# Get the module name passed in argument
default_output_dir = os.path.join("source", "generated")
parser = OptionParser(usage="usage: %prog -i <inputmodule>'")
parser.add_option("-i", "--imodule",
                  action="store",
                  dest="module",
                  default=None,
                  help="the name of the module we want to document.")
parser.add_option("-v", "--verbose",
                  action="store_true", dest="verbose", default=False,
                  help="set the logging level to DEBUG.")
parser.add_option("-o", "--outdir",
                  action="store",
                  dest="outdir",
                  default=default_output_dir,
                  help="output base directory. Docs will be generated in "
                  "sub-directories there, named by their module names. "
                  "default: {0}".format(
                      default_output_dir))
(options, args) = parser.parse_args()
if options.module is None:
    parser.error("Wrong number of arguments.")

# Define logger
logger = logging.getLogger(__file__)
if options.verbose:
    logging.basicConfig(
        level=logging.DEBUG,
        format="{0}::%(asctime)s::%(levelname)s::%(message)s".format(
            logger.name))
else:
    logging.basicConfig(
        level=logging.INFO,
        format="{0}::%(asctime)s::%(levelname)s::%(message)s".format(
            logger.name))

base_outdir = options.outdir

# Capsul import
from capsul.qt_apps.utils.find_pipelines import find_pipeline_and_process
from capsul.process import get_process_instance
from capsul.pipeline import pipeline_tools


# Get all caps pipelines
pipelines = find_pipeline_and_process(
    os.path.basename(options.module))["pipeline_descs"]
logger.info("Found '{0}' pipeline(s) in '{1}'.".format(
    len(pipelines), options.module))

# Sort pipelines processes
# From the pipelines full path 'm1.m2.pipeline' get there module names 'm2'
module_names = set([x.split(".")[1] for x in pipelines])
# Sort each pipeline according to its module name.
# The result is a dict of the form 'd[m2] = [pipeline1, pipeline2, ...]'.
sorted_pipelines = dict((x, []) for x in module_names)
for pipeline in pipelines:
    module_name = pipeline.split(".")[1]
    sorted_pipelines[module_name].append(pipeline)

# Generate a png representation of each pipeline.
for module_name, module_pipelines in sorted_pipelines.items():

    # Where the documentation will be written: a relative path from the
    # makefile
    outdir = os.path.join(base_outdir, module_name, "schema")

    # Go through all pipeline
    for module_pipeline in module_pipelines:

        # Get pipeline instance
        pipeline_instance = get_process_instance(module_pipeline)

        # Get output files
        if not os.path.isdir(outdir):
            os.makedirs(outdir)
        image_name = os.path.join(outdir, module_pipeline + ".png")
        pipeline_tools.save_dot_image(
            pipeline_instance, image_name, nodesep=0.1, include_io=False,
            rankdir='TB')
        logger.info("Pipeline '{0}' representation has been written at "
                    "location '{1}'.".format(module_pipeline,
                                             os.path.abspath(image_name)))

    # Just print a summary
    logger.info("Summary: '{0}' files written for module '{1}'.".format(
        len(module_pipelines), module_name))