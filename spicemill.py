# MIT License
#
# Copyright (c) 2024 Diordany van Hemert
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

import matplotlib.pyplot as m_pyplot
import numpy as m_numpy
import os as m_os
import sys as m_sys

from modules.argparser import ArgParser
from modules.config import Config
from modules.rawfile import RawFile

if __name__ == "__main__":
  argParser = ArgParser()
  argParser.parse(m_sys.argv)

  config = Config()
  config.read_args(argParser)

  rawFile = RawFile(config.rawFileName)
  rawFile.open()
  rawFile.read()
  rawFile.close()

  time = rawFile.get_time_data()
  curves = rawFile.get_curve_data(config.vars)

  nCurves = len(curves)

  if nCurves > 0:
    figure, axes = m_pyplot.subplots(nCurves)

    figure.suptitle(rawFile.title+" ["+rawFile.plotName+"]")

    for i in range(nCurves):
      if nCurves > 1:
        axes[i].plot(time, curves[i]["data"])
        axes[i].set_ylabel(curves[i]["name"])
        axes[i].set_xlabel("Time [s]")
        axes[i].grid()
      else:
        axes.plot(time, curves[i]["data"])
        axes.set_ylabel(curves[i]["name"])
        axes.set_xlabel("Time [s]")
        axes.grid()

    figure.tight_layout()

    m_pyplot.show()
  else:
    print("No curves to show.")