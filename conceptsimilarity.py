#!/usr/bin/env python2

import logging
import json

from cmg import dbpediaparser

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


#Functions
text = "The French Revolution was a period of far-reaching social and political upheaval in France and its colonies that lasted from 1789 until 1799. It was partially carried forward by Napoleon during the later expansion of the French Empire."
print dbpediaparser.entity_extractor(text)