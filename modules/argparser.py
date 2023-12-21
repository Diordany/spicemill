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

class ArgParser:
  def __init__(self):
    self.args = None
    self.options = {}
    self.optionPrefix = "--"

  def get_option(self, p_name):
    if p_name in self.options:
      return self.options[p_name]
    else:
      return None

  def parse(self, p_args):
    self.args = p_args
    self.parse_options()

  def parse_options(self):
    # For every argument.
    for i in range(len(self.args)):
      arg = self.args[i]

      # Check if the argument starts with the option prefix.
      if arg.startswith(self.optionPrefix):
        optName = arg[len(self.optionPrefix):]
        optVal = None

        # If it's not the last argument in the list.
        if i < len(self.args) - 1:
          nextArg = self.args[i + 1]

          # Set the next argument as the value if it's not an option.
          if not nextArg.startswith(self.optionPrefix):
            optVal = nextArg

        self.options[optName] = optVal