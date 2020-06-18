# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

bl_info = {
    "name" : "testaddon",
    "author" : "jw",
    "description" : "simple test addon",
    "blender" : (2, 80, 0),
    "version" : (0, 0, 1),
    "location" : "View 3D",
    "warning" : "",
    "category" : "Generic"
}

import bpy
# from test_op import Test_OT_Operator 
from . test_op    import Test_OT_Operator
from . test_panel import Test_PT_Panel

classes = (Test_OT_Operator, Test_PT_Panel)

register, unregister = bpy.utils.register_classes_factory(classes)
