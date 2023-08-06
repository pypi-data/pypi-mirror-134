#############
# MIT License
#
# Copyright (C) 2020 ThoughtForge Inc.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy 
# of this software and associated documentation files (the "Software"), to deal 
# in the Software without restriction, including without limitation the rights 
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell 
# copies of the Software, and to permit persons to whom the Software is 
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all 
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR 
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE 
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, 
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE 
# SOFTWARE.
#############

import gym
import math, os, json
import numpy as np

from thoughtforge_client.thoughtforge_client import BaseThoughtForgeClientSession
from advanced.reacher.example_reacher_client import ExampleReacherSession


if __name__ == "__main__": 
    host = '0.0.0.0' if not 'HOST' in os.environ else os.environ['HOST']
    port = 4343 if not 'PORT' in os.environ else int(os.environ['PORT'])
    saved_network_directory = "./advanced/reacher/"
    filename = INSERT FILE NAME HERE
    file_location = os.path.join(saved_network_directory, filename)
    model_data_file = None
    with open(file_location, 'r', encoding='utf-8') as out_file:
        model_data_file = json.load(out_file)

    json_model_specification = model_data_file['specification']
    model_data = model_data_file['model_data']
    session = ExampleReacherSession(json_model_specification, model_data=model_data)
