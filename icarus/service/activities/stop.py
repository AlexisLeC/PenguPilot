"""
  ___________________________________________________
 |  _____                       _____ _ _       _    |
 | |  __ \                     |  __ (_) |     | |   |
 | | |__) |__ _ __   __ _ _   _| |__) || | ___ | |_  |
 | |  ___/ _ \ '_ \ / _` | | | |  ___/ | |/ _ \| __| |
 | | |  |  __/ | | | (_| | |_| | |   | | | (_) | |_  |
 | |_|   \___|_| |_|\__, |\__,_|_|   |_|_|\___/ \__| |
 |                   __/ |                           |
 |  GNU/Linux based |___/  Multi-Rotor UAV Autopilot |
 |___________________________________________________|
 
 Stop Activity Class

 Copyright (C) 2013 Tobias Simon, Ilmenau University of Technology

 This program is free software; you can redistribute it and/or modify
 it under the terms of the GNU General Public License as published by
 the Free Software Foundation; either version 2 of the License, or
 (at your option) any later version.

 This program is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU General Public License for more details. """


from core_pb2 import *
from activity import Activity, StabMixIn


class StopActivity(Activity, StabMixIn):

   def __init__(self, fsm, core, mon_data):
      Activity.__init__(self)
      self.fsm = fsm
      self.core = core
      self.mon_data = mon_data
      self.canceled = False

   def run(self):
      core = self.core
      mon_data = self.mon_data
      self.core.set_ctrl_param(POS_X, mon_data.x)
      self.core.set_ctrl_param(POS_Y, mon_data.y)
      self.core.set_ctrl_param(POS_Z, mon_data.z)
      self.stabilize()
      self.fsm.done()
