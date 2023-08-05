# -*- coding: utf-8 -*-
#
# AWL simulator - SFCs
#
# Copyright 2015 Michael Buesch <m@bues.ch>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#

from __future__ import division, absolute_import, print_function, unicode_literals
from awlsim.common.compat import *

from awlsim.core.systemblocks.systemblocks import *
from awlsim.core.util import *

import time


class SFC47(SFC):
	name = (47, "WAIT", "delay time")

	interfaceFields = {
		BlockInterfaceField.FTYPE_IN	: (
			BlockInterfaceField(name = "WT",
					    dataType = AwlDataType.makeByName("INT")),
		)
	}

	def run(self):
		s = self.cpu.statusWord

		# Delay for the specified amount of microseconds.
		# WT is an int, so the maximum delay is 32767 us.
		WT = wordToSignedPyInt(self.fetchInterfaceFieldByName("WT"))
		if WT > 0:
			time.sleep(WT / 1000000.0)
		self.cpu.updateTimestamp()

		s.BIE = 1
