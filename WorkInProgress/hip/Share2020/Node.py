# Initialize parent node variable.
if locals().get("hou_parent") is None:
    hou_parent = hou.node("/obj")

# Code for /obj/Node_for_OUTPUT
hou_node = hou_parent.createNode("geo", "Node_for_OUTPUT", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(9.48049, -1.94924))
if hou_parent.findNetworkBox("__netbox1") is not None:
    hou_parent.findNetworkBox("__netbox1").addNode(hou_node)
hou_node.setSelectableInViewport(True)
hou_node.showOrigin(False)
hou_node.useXray(False)
hou_node.setDisplayFlag(True)
hou_node.hide(False)
hou_node.setSelected(False)

hou_parm_template_group = hou.ParmTemplateGroup()
# Code for parameter template
hou_parm_template = hou.FolderParmTemplate("stdswitcher4", "Transform", folder_type=hou.folderType.Tabs, default_value=0, ends_tab_group=False)
# Code for parameter template
hou_parm_template2 = hou.MenuParmTemplate("xOrd", "Transform Order", menu_items=(["srt","str","rst","rts","tsr","trs"]), menu_labels=(["Scale Rot Trans","Scale Trans Rot","Rot Scale Trans","Rot Trans Scale","Trans Scale Rot","Trans Rot Scale"]), default_value=0, icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal, menu_use_token=False, is_button_strip=False, strip_uses_icons=False)
hou_parm_template2.setJoinWithNext(True)
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.MenuParmTemplate("rOrd", "Rotate Order", menu_items=(["xyz","xzy","yxz","yzx","zxy","zyx"]), menu_labels=(["Rx Ry Rz","Rx Rz Ry","Ry Rx Rz","Ry Rz Rx","Rz Rx Ry","Rz Ry Rx"]), default_value=0, icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal, menu_use_token=False, is_button_strip=False, strip_uses_icons=False)
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.FloatParmTemplate("t", "Translate", 3, default_value=([0, 0, 0]), min=0, max=10, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.XYZW)
hou_parm_template2.setTags({"autoscope": "1111111111111111111111111111111", "script_action": "import objecttoolutils\nobjecttoolutils.matchTransform(kwargs, 0)", "script_action_help": "Select an object to match the translation with.", "script_action_icon": "BUTTONS_match_transform"})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.FloatParmTemplate("r", "Rotate", 3, default_value=([0, 0, 0]), min=0, max=360, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.XYZW)
hou_parm_template2.setTags({"autoscope": "1111111111111111111111111111111", "script_action": "import objecttoolutils\nobjecttoolutils.matchTransform(kwargs, 1)", "script_action_help": "Select an object to match the rotation with.", "script_action_icon": "BUTTONS_match_rotation"})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.FloatParmTemplate("s", "Scale", 3, default_value=([1, 1, 1]), min=0, max=10, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.XYZW)
hou_parm_template2.setTags({"autoscope": "1111111111111111111111111111111", "script_action": "import objecttoolutils\nobjecttoolutils.matchTransform(kwargs, 2)", "script_action_help": "Select an object to match the scale with.", "script_action_icon": "BUTTONS_match_scale"})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.FloatParmTemplate("p", "Pivot Translate", 3, default_value=([0, 0, 0]), min=0, max=10, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.XYZW)
hou_parm_template2.setTags({"script_action": "import objecttoolutils\nobjecttoolutils.matchTransform(kwargs, 3)", "script_action_help": "Select an object to match the pivot with.", "script_action_icon": "BUTTONS_match_pivot"})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.FloatParmTemplate("pr", "Pivot Rotate", 3, default_value=([0, 0, 0]), min=0, max=10, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.XYZW)
hou_parm_template2.setTags({"script_action": "import objecttoolutils\nobjecttoolutils.matchTransform(kwargs, 4)", "script_action_help": "Select an object to match the pivot rotation with.", "script_action_icon": "BUTTONS_match_pivot_rotation"})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.FloatParmTemplate("scale", "Uniform Scale", 1, default_value=([1]), min=0, max=10, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.Base1)
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.MenuParmTemplate("pre_xform", "Modify Pre-Transform", menu_items=(["clean","cleantrans","cleanrot","cleanscales","extract","reset"]), menu_labels=(["Clean Transform","Clean Translates","Clean Rotates","Clean Scales","Extract Pre-transform","Reset Pre-transform"]), default_value=0, icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.StringReplace, menu_use_token=False, is_button_strip=False, strip_uses_icons=False)
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.ToggleParmTemplate("keeppos", "Keep Position When Parenting", default_value=False)
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.ToggleParmTemplate("childcomp", "Child Compensation", default_value=False)
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.ToggleParmTemplate("constraints_on", "Enable Constraints", default_value=False)
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.StringParmTemplate("constraints_path", "Constraints", 1, default_value=([""]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.NodeReference, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template2.setConditional(hou.parmCondType.HideWhen, "{ constraints_on == 0 }")
hou_parm_template2.setTags({"opfilter": "!!CHOP", "oprelative": ".", "script_action": "import objecttoolutils\nobjecttoolutils.constraintsMenu(kwargs)", "script_action_help": "", "script_action_icon": "BUTTONS_add_constraints"})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.StringParmTemplate("lookatpath", "Look At", 1, default_value=([""]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.NodeReference, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template2.hide(True)
hou_parm_template2.setTags({"opfilter": "!!OBJ!!", "oprelative": "."})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.StringParmTemplate("lookupobjpath", "Look Up Object", 1, default_value=([""]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.NodeReference, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template2.hide(True)
hou_parm_template2.setTags({"opfilter": "!!OBJ!!", "oprelative": "."})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.StringParmTemplate("lookup", "Look At Up Vector", 1, default_value=(["on"]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.Regular, menu_items=(["off","on","quat","pos","obj"]), menu_labels=(["Don't Use Up Vector","Use Up Vector","Use Quaternions","Use Global Position","Use Up Object"]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template2.hide(True)
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.StringParmTemplate("pathobjpath", "Path Object", 1, default_value=([""]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.NodeReference, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template2.hide(True)
hou_parm_template2.setTags({"opfilter": "!!SOP!!", "oprelative": "."})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.FloatParmTemplate("roll", "Roll", 1, default_value=([0]), min=-360, max=360, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Angle, naming_scheme=hou.parmNamingScheme.Base1)
hou_parm_template2.hide(True)
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.FloatParmTemplate("pos", "Position", 1, default_value=([0]), min=0, max=10, min_is_strict=True, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.Base1)
hou_parm_template2.hide(True)
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.MenuParmTemplate("uparmtype", "Parameterization", menu_items=(["uniform","arc"]), menu_labels=(["Uniform","Arc Length"]), default_value=1, icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal, menu_use_token=False, is_button_strip=False, strip_uses_icons=False)
hou_parm_template2.hide(True)
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.IntParmTemplate("pathorient", "Orient Along Path", 1, default_value=([1]), min=0, max=1, min_is_strict=False, max_is_strict=False, naming_scheme=hou.parmNamingScheme.Base1, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal, menu_use_token=False)
hou_parm_template2.hide(True)
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.FloatParmTemplate("up", "Orient Up Vector", 3, default_value=([0, 1, 0]), min=0, max=10, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Vector, naming_scheme=hou.parmNamingScheme.XYZW)
hou_parm_template2.hide(True)
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.FloatParmTemplate("bank", "Auto-Bank factor", 1, default_value=([0]), min=-1, max=1, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.Base1)
hou_parm_template2.hide(True)
hou_parm_template.addParmTemplate(hou_parm_template2)
hou_parm_template_group.append(hou_parm_template)
# Code for parameter template
hou_parm_template = hou.FolderParmTemplate("stdswitcher4_1", "Render", folder_type=hou.folderType.Tabs, default_value=0, ends_tab_group=False)
# Code for parameter template
hou_parm_template2 = hou.StringParmTemplate("shop_materialpath", "Material", 1, default_value=([""]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.NodeReference, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template2.setTags({"opfilter": "!!CUSTOM/MATERIAL!!", "oprelative": "."})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.MenuParmTemplate("shop_materialopts", "Options", menu_items=([]), menu_labels=([]), default_value=0, icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Mini, menu_use_token=False, is_button_strip=False, strip_uses_icons=False)
hou_parm_template2.hide(True)
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.ToggleParmTemplate("tdisplay", "Display", default_value=False)
hou_parm_template2.setJoinWithNext(True)
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.IntParmTemplate("display", "Display", 1, default_value=([1]), min=0, max=1, min_is_strict=True, max_is_strict=True, naming_scheme=hou.parmNamingScheme.Base1, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal, menu_use_token=False)
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.MenuParmTemplate("viewportlod", "Display As", menu_items=(["full","points","box","centroid","hidden","subd"]), menu_labels=(["Full Geometry","Point Cloud","Bounding Box","Centroid","Hidden","Subdivision Surface / Curves"]), default_value=0, icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal, menu_use_token=False, is_button_strip=False, strip_uses_icons=False)
hou_parm_template2.setHelp("Choose how the object's geometry should be rendered in the viewport")
hou_parm_template2.setTags({"spare_category": "Render"})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.StringParmTemplate("vm_rendervisibility", "Render Visibility", 1, default_value=(["*"]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.Regular, menu_items=(["*","primary","primary|shadow","-primary","-diffuse","-diffuse&-reflect&-refract",""]), menu_labels=(["Visible to all","Visible only to primary rays","Visible only to primary and shadow rays","Invisible to primary rays (Phantom)","Invisible to diffuse rays","Invisible to secondary rays","Invisible (Unrenderable)"]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.StringReplace)
hou_parm_template2.setTags({"mantra_class": "object", "mantra_name": "rendervisibility", "spare_category": "Render"})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.ToggleParmTemplate("vm_rendersubd", "Render Polygons As Subdivision (Mantra)", default_value=False)
hou_parm_template2.setTags({"mantra_class": "object", "mantra_name": "rendersubd", "spare_category": "Geometry"})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.StringParmTemplate("vm_subdstyle", "Subdivision Style", 1, default_value=(["mantra_catclark"]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.Regular, menu_items=(["mantra_catclark","osd_catclark"]), menu_labels=(["Mantra Catmull-Clark","OpenSubdiv Catmull-Clark"]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template2.setConditional(hou.parmCondType.HideWhen, "{ vm_rendersubd == 0 }")
hou_parm_template2.setTags({"mantra_class": "object", "mantra_name": "subdstyle", "spare_category": "Geometry"})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.StringParmTemplate("vm_subdgroup", "Subdivision Group", 1, default_value=([""]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.Regular, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template2.setConditional(hou.parmCondType.HideWhen, "{ vm_rendersubd == 0 }")
hou_parm_template2.setTags({"mantra_class": "object", "mantra_name": "subdgroup", "spare_category": "Geometry"})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.FloatParmTemplate("vm_osd_quality", "Open Subdiv Quality", 1, default_value=([1]), min=0, max=10, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.Base1)
hou_parm_template2.setConditional(hou.parmCondType.HideWhen, "{ vm_rendersubd == 0 vm_subdstyle != osd_catclark }")
hou_parm_template2.setTags({"mantra_class": "object", "mantra_name": "osd_quality", "spare_category": "Geometry"})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.IntParmTemplate("vm_osd_vtxinterp", "OSD Vtx Interp", 1, default_value=([2]), min=0, max=10, min_is_strict=False, max_is_strict=False, naming_scheme=hou.parmNamingScheme.Base1, menu_items=(["0","1","2"]), menu_labels=(["No vertex interpolation","Edges only","Edges and Corners"]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal, menu_use_token=False)
hou_parm_template2.setConditional(hou.parmCondType.HideWhen, "{ vm_rendersubd == 0 vm_subdstyle != osd_catclark }")
hou_parm_template2.setTags({"mantra_class": "object", "mantra_name": "osd_vtxinterp", "spare_category": "Geometry"})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.IntParmTemplate("vm_osd_fvarinterp", "OSD FVar Interp", 1, default_value=([4]), min=0, max=10, min_is_strict=False, max_is_strict=False, naming_scheme=hou.parmNamingScheme.Base1, menu_items=(["0","1","2","3","4","5"]), menu_labels=(["Smooth everywhere","Sharpen corners only","Sharpen edges and corners","Sharpen edges and propagated corners","Sharpen all boundaries","Bilinear interpolation"]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal, menu_use_token=False)
hou_parm_template2.setConditional(hou.parmCondType.HideWhen, "{ vm_rendersubd == 0 vm_subdstyle != osd_catclark }")
hou_parm_template2.setTags({"mantra_class": "object", "mantra_name": "osd_fvarinterp", "spare_category": "Geometry"})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.FolderParmTemplate("folder0", "Shading", folder_type=hou.folderType.Tabs, default_value=0, ends_tab_group=False)
# Code for parameter template
hou_parm_template3 = hou.StringParmTemplate("categories", "Categories", 1, default_value=([""]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.Regular, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template3.setHelp("A list of tags which can be used to select the object")
hou_parm_template3.setTags({"spare_category": "Shading"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
# Code for parameter template
hou_parm_template3 = hou.StringParmTemplate("reflectmask", "Reflection Mask", 1, default_value=(["*"]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.NodeReferenceList, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template3.setHelp("Objects that will be reflected on this object.")
hou_parm_template3.setTags({"opexpand": "1", "opfilter": "!!OBJ/GEOMETRY!!", "oprelative": "/obj", "spare_category": "Shading"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
# Code for parameter template
hou_parm_template3 = hou.StringParmTemplate("refractmask", "Refraction Mask", 1, default_value=(["*"]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.NodeReferenceList, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template3.setHelp("Objects that will be refracted on this object.")
hou_parm_template3.setTags({"opexpand": "1", "opfilter": "!!OBJ/GEOMETRY!!", "oprelative": "/obj", "spare_category": "Shading"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
# Code for parameter template
hou_parm_template3 = hou.StringParmTemplate("lightmask", "Light Mask", 1, default_value=(["*"]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.NodeReferenceList, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template3.setHelp("Lights that illuminate this object.")
hou_parm_template3.setTags({"opexpand": "1", "opfilter": "!!OBJ/LIGHT!!", "oprelative": "/obj", "spare_category": "Shading"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
# Code for parameter template
hou_parm_template3 = hou.StringParmTemplate("lightcategories", "Light Selection", 1, default_value=(["*"]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.Regular, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template3.setTags({"spare_category": "Shading"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
# Code for parameter template
hou_parm_template3 = hou.StringParmTemplate("vm_lpetag", "LPE Tag", 1, default_value=([""]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.Regular, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template3.setTags({"mantra_class": "object", "mantra_name": "lpetag", "spare_category": "Shading"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
# Code for parameter template
hou_parm_template3 = hou.StringParmTemplate("vm_volumefilter", "Volume Filter", 1, default_value=(["box"]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.Regular, menu_items=(["box","gaussian","bartlett","catrom","hanning","blackman","sinc"]), menu_labels=(["Box Filter","Gaussian","Bartlett (triangle)","Catmull-Rom","Hanning","Blackman","Sinc (sharpening)"]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template3.setTags({"mantra_class": "object", "mantra_name": "filter", "spare_category": "Shading"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
# Code for parameter template
hou_parm_template3 = hou.FloatParmTemplate("vm_volumefilterwidth", "Volume Filter Width", 1, default_value=([1]), min=0.001, max=5, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.Base1)
hou_parm_template3.setTags({"mantra_class": "object", "mantra_name": "filterwidth", "spare_category": "Shading"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
# Code for parameter template
hou_parm_template3 = hou.ToggleParmTemplate("vm_matte", "Matte shading", default_value=False)
hou_parm_template3.setTags({"mantra_class": "object", "mantra_name": "matte", "spare_category": "Shading"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
# Code for parameter template
hou_parm_template3 = hou.ToggleParmTemplate("vm_rayshade", "Raytrace Shading", default_value=False)
hou_parm_template3.setTags({"mantra_class": "object", "mantra_name": "rayshade", "spare_category": "Shading"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.FolderParmTemplate("folder0_1", "Sampling", folder_type=hou.folderType.Tabs, default_value=0, ends_tab_group=False)
# Code for parameter template
hou_parm_template3 = hou.MenuParmTemplate("geo_velocityblur", "Geometry Velocity Blur", menu_items=(["off","on","accelblur"]), menu_labels=(["No Velocity Blur","Velocity Blur","Acceleration Blur"]), default_value=0, icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal, menu_use_token=False, is_button_strip=False, strip_uses_icons=False)
hou_parm_template3.setConditional(hou.parmCondType.DisableWhen, "{ allowmotionblur == 0 }")
hou_parm_template2.addParmTemplate(hou_parm_template3)
# Code for parameter template
hou_parm_template3 = hou.StringParmTemplate("geo_accelattribute", "Acceleration Attribute", 1, default_value=(["accel"]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.Regular, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template3.setConditional(hou.parmCondType.HideWhen, "{ geo_velocityblur != accelblur }")
hou_parm_template3.setTags({"spare_category": "Sampling"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.FolderParmTemplate("folder0_2", "Dicing", folder_type=hou.folderType.Tabs, default_value=0, ends_tab_group=False)
# Code for parameter template
hou_parm_template3 = hou.FloatParmTemplate("vm_shadingquality", "Shading Quality", 1, default_value=([1]), min=0, max=10, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.Base1)
hou_parm_template3.setTags({"mantra_class": "object", "mantra_name": "shadingquality", "spare_category": "Dicing"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
# Code for parameter template
hou_parm_template3 = hou.FloatParmTemplate("vm_flatness", "Dicing Flatness", 1, default_value=([0.05]), min=0, max=1, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.Base1)
hou_parm_template3.setTags({"mantra_class": "object", "mantra_name": "flatness", "spare_category": "Dicing"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
# Code for parameter template
hou_parm_template3 = hou.IntParmTemplate("vm_raypredice", "Ray Predicing", 1, default_value=([0]), min=0, max=10, min_is_strict=False, max_is_strict=False, naming_scheme=hou.parmNamingScheme.Base1, menu_items=(["0","1","2"]), menu_labels=(["Disable Predicing","Full Predicing","Precompute Bounds"]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal, menu_use_token=False)
hou_parm_template3.setTags({"mantra_class": "object", "mantra_name": "raypredice", "spare_category": "Dicing"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
# Code for parameter template
hou_parm_template3 = hou.ToggleParmTemplate("vm_curvesurface", "Shade Curves As Surfaces", default_value=False)
hou_parm_template3.setTags({"mantra_class": "object", "mantra_name": "curvesurface", "spare_category": "Dicing"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.FolderParmTemplate("folder0_3", "Geometry", folder_type=hou.folderType.Tabs, default_value=0, ends_tab_group=False)
# Code for parameter template
hou_parm_template3 = hou.ToggleParmTemplate("vm_rmbackface", "Backface Removal", default_value=False)
hou_parm_template3.setTags({"mantra_class": "object", "mantra_name": "rmbackface", "spare_category": "Geometry"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
# Code for parameter template
hou_parm_template3 = hou.StringParmTemplate("shop_geometrypath", "Procedural Shader", 1, default_value=([""]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.NodeReference, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template3.setTags({"opfilter": "!!SHOP/GEOMETRY!!", "oprelative": ".", "spare_category": "Geometry"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
# Code for parameter template
hou_parm_template3 = hou.ToggleParmTemplate("vm_forcegeometry", "Force Procedural Geometry Output", default_value=True)
hou_parm_template3.setTags({"spare_category": "Geometry"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
# Code for parameter template
hou_parm_template3 = hou.ToggleParmTemplate("vm_rendersubdcurves", "Render Polygon Curves As Subdivision (Mantra)", default_value=False)
hou_parm_template3.setTags({"mantra_class": "object", "mantra_name": "rendersubdcurves", "spare_category": "Geometry"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
# Code for parameter template
hou_parm_template3 = hou.IntParmTemplate("vm_renderpoints", "Render As Points (Mantra)", 1, default_value=([2]), min=0, max=10, min_is_strict=False, max_is_strict=False, naming_scheme=hou.parmNamingScheme.Base1, menu_items=(["0","1","2"]), menu_labels=(["No Point Rendering","Render Only Points","Render Unconnected Points"]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal, menu_use_token=False)
hou_parm_template3.setTags({"mantra_class": "object", "mantra_name": "renderpoints", "spare_category": "Geometry"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
# Code for parameter template
hou_parm_template3 = hou.IntParmTemplate("vm_renderpointsas", "Render Points As (Mantra)", 1, default_value=([0]), min=0, max=10, min_is_strict=False, max_is_strict=False, naming_scheme=hou.parmNamingScheme.Base1, menu_items=(["0","1"]), menu_labels=(["Spheres","Circles"]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal, menu_use_token=False)
hou_parm_template3.setConditional(hou.parmCondType.DisableWhen, "{ vm_renderpoints == 0 }")
hou_parm_template3.setTags({"mantra_class": "object", "mantra_name": "renderpointsas", "spare_category": "Geometry"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
# Code for parameter template
hou_parm_template3 = hou.ToggleParmTemplate("vm_usenforpoints", "Use N For Point Rendering", default_value=False)
hou_parm_template3.setConditional(hou.parmCondType.DisableWhen, "{ vm_renderpoints == 0 }")
hou_parm_template3.setTags({"mantra_class": "object", "mantra_name": "usenforpoints", "spare_category": "Geometry"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
# Code for parameter template
hou_parm_template3 = hou.FloatParmTemplate("vm_pointscale", "Point Scale", 1, default_value=([1]), min=0, max=10, min_is_strict=True, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.Base1)
hou_parm_template3.setConditional(hou.parmCondType.DisableWhen, "{ vm_renderpoints == 0 }")
hou_parm_template3.setTags({"mantra_class": "object", "mantra_name": "pointscale", "spare_category": "Geometry"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
# Code for parameter template
hou_parm_template3 = hou.ToggleParmTemplate("vm_pscalediameter", "Treat Point Scale as Diameter Instead of Radius", default_value=False)
hou_parm_template3.setTags({"mantra_class": "object", "mantra_name": "pscalediameter", "spare_category": "Geometry"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
# Code for parameter template
hou_parm_template3 = hou.ToggleParmTemplate("vm_metavolume", "Metaballs as Volume", default_value=False)
hou_parm_template3.setTags({"mantra_class": "object", "mantra_name": "metavolume", "spare_category": "Geometry"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
# Code for parameter template
hou_parm_template3 = hou.IntParmTemplate("vm_coving", "Coving", 1, default_value=([1]), min=0, max=10, min_is_strict=False, max_is_strict=False, naming_scheme=hou.parmNamingScheme.Base1, menu_items=(["0","1","2"]), menu_labels=(["Disable Coving","Coving for displacement/sub-d","Coving for all primitives"]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal, menu_use_token=False)
hou_parm_template3.setTags({"mantra_class": "object", "mantra_name": "coving", "spare_category": "Geometry"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
# Code for parameter template
hou_parm_template3 = hou.StringParmTemplate("vm_materialoverride", "Material Override", 1, default_value=(["compact"]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.Regular, menu_items=(["none","full","compact"]), menu_labels=(["Disabled","Evaluate for Each Primitve/Point","Evaluate Once"]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template3.setTags({"spare_category": "Geometry"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
# Code for parameter template
hou_parm_template3 = hou.ToggleParmTemplate("vm_overridedetail", "Ignore Geometry Attribute Shaders", default_value=False)
hou_parm_template3.setTags({"mantra_class": "object", "mantra_name": "overridedetail", "spare_category": "Geometry"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
# Code for parameter template
hou_parm_template3 = hou.ToggleParmTemplate("vm_procuseroottransform", "Proc Use Root Transform", default_value=True)
hou_parm_template3.setTags({"mantra_class": "object", "mantra_name": "procuseroottransform", "spare_category": "Geometry"})
hou_parm_template2.addParmTemplate(hou_parm_template3)
hou_parm_template.addParmTemplate(hou_parm_template2)
hou_parm_template_group.append(hou_parm_template)
# Code for parameter template
hou_parm_template = hou.FolderParmTemplate("stdswitcher4_2", "Misc", folder_type=hou.folderType.Tabs, default_value=0, ends_tab_group=False)
# Code for parameter template
hou_parm_template2 = hou.ToggleParmTemplate("use_dcolor", "Set Wireframe Color", default_value=False)
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.FloatParmTemplate("dcolor", "Wireframe Color", 3, default_value=([1, 1, 1]), min=0, max=1, min_is_strict=True, max_is_strict=True, look=hou.parmLook.ColorSquare, naming_scheme=hou.parmNamingScheme.RGBA)
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.ToggleParmTemplate("picking", "Viewport Selecting Enabled", default_value=True)
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.StringParmTemplate("pickscript", "Select Script", 1, default_value=([""]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.FileReference, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.StringReplace)
hou_parm_template2.setTags({"filechooser_mode": "read"})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.ToggleParmTemplate("caching", "Cache Object Transform", default_value=True)
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.ToggleParmTemplate("vport_shadeopen", "Shade Open Curves In Viewport", default_value=False)
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.ToggleParmTemplate("vport_displayassubdiv", "Display as Subdivision in Viewport", default_value=False)
hou_parm_template2.hide(True)
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.MenuParmTemplate("vport_onionskin", "Onion Skinning", menu_items=(["off","xform","on"]), menu_labels=(["Off","Transform only","Full Deformation"]), default_value=0, icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal, menu_use_token=False, is_button_strip=False, strip_uses_icons=False)
hou_parm_template.addParmTemplate(hou_parm_template2)
hou_parm_template_group.append(hou_parm_template)
hou_node.setParmTemplateGroup(hou_parm_template_group)
# Code for /obj/Node_for_OUTPUT/stdswitcher1 parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT")
hou_parm = hou_node.parm("stdswitcher1")
hou_parm.lock(False)
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/xOrd parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT")
hou_parm = hou_node.parm("xOrd")
hou_parm.lock(False)
hou_parm.set("srt")
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/rOrd parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT")
hou_parm = hou_node.parm("rOrd")
hou_parm.lock(False)
hou_parm.set("xyz")
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/t parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT")
hou_parm_tuple = hou_node.parmTuple("t")
hou_parm_tuple.lock((False, False, False))
hou_parm_tuple.set((0, 0, 0))
hou_parm_tuple.setAutoscope((True, True, True))


# Code for /obj/Node_for_OUTPUT/r parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT")
hou_parm_tuple = hou_node.parmTuple("r")
hou_parm_tuple.lock((False, False, False))
hou_parm_tuple.set((0, 0, 0))
hou_parm_tuple.setAutoscope((True, True, True))


# Code for /obj/Node_for_OUTPUT/s parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT")
hou_parm_tuple = hou_node.parmTuple("s")
hou_parm_tuple.lock((False, False, False))
hou_parm_tuple.set((1, 1, 1))
hou_parm_tuple.setAutoscope((True, True, True))


# Code for /obj/Node_for_OUTPUT/p parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT")
hou_parm_tuple = hou_node.parmTuple("p")
hou_parm_tuple.lock((False, False, False))
hou_parm_tuple.set((0, 0, 0))
hou_parm_tuple.setAutoscope((False, False, False))


# Code for /obj/Node_for_OUTPUT/pr parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT")
hou_parm_tuple = hou_node.parmTuple("pr")
hou_parm_tuple.lock((False, False, False))
hou_parm_tuple.set((0, 0, 0))
hou_parm_tuple.setAutoscope((False, False, False))


# Code for /obj/Node_for_OUTPUT/scale parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT")
hou_parm = hou_node.parm("scale")
hou_parm.lock(False)
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/pre_xform parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT")
hou_parm = hou_node.parm("pre_xform")
hou_parm.lock(False)
hou_parm.set("clean")
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/keeppos parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT")
hou_parm = hou_node.parm("keeppos")
hou_parm.lock(False)
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/childcomp parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT")
hou_parm = hou_node.parm("childcomp")
hou_parm.lock(False)
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/constraints_on parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT")
hou_parm = hou_node.parm("constraints_on")
hou_parm.lock(False)
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/constraints_path parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT")
hou_parm = hou_node.parm("constraints_path")
hou_parm.lock(False)
hou_parm.set("")
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/lookatpath parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT")
hou_parm = hou_node.parm("lookatpath")
hou_parm.lock(False)
hou_parm.set("")
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/lookupobjpath parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT")
hou_parm = hou_node.parm("lookupobjpath")
hou_parm.lock(False)
hou_parm.set("")
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/lookup parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT")
hou_parm = hou_node.parm("lookup")
hou_parm.lock(False)
hou_parm.set("on")
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/pathobjpath parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT")
hou_parm = hou_node.parm("pathobjpath")
hou_parm.lock(False)
hou_parm.set("")
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/roll parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT")
hou_parm = hou_node.parm("roll")
hou_parm.lock(False)
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/pos parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT")
hou_parm = hou_node.parm("pos")
hou_parm.lock(False)
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/uparmtype parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT")
hou_parm = hou_node.parm("uparmtype")
hou_parm.lock(False)
hou_parm.set("arc")
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/pathorient parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT")
hou_parm = hou_node.parm("pathorient")
hou_parm.lock(False)
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/up parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT")
hou_parm_tuple = hou_node.parmTuple("up")
hou_parm_tuple.lock((False, False, False))
hou_parm_tuple.set((0, 1, 0))
hou_parm_tuple.setAutoscope((False, False, False))


# Code for /obj/Node_for_OUTPUT/bank parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT")
hou_parm = hou_node.parm("bank")
hou_parm.lock(False)
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/shop_materialpath parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT")
hou_parm = hou_node.parm("shop_materialpath")
hou_parm.lock(False)
hou_parm.set("")
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/shop_materialopts parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT")
hou_parm = hou_node.parm("shop_materialopts")
hou_parm.lock(False)
hou_parm.set("override")
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/tdisplay parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT")
hou_parm = hou_node.parm("tdisplay")
hou_parm.lock(False)
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/display parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT")
hou_parm = hou_node.parm("display")
hou_parm.lock(False)
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/use_dcolor parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT")
hou_parm = hou_node.parm("use_dcolor")
hou_parm.lock(False)
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/dcolor parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT")
hou_parm_tuple = hou_node.parmTuple("dcolor")
hou_parm_tuple.lock((False, False, False))
hou_parm_tuple.set((1, 1, 1))
hou_parm_tuple.setAutoscope((False, False, False))


# Code for /obj/Node_for_OUTPUT/picking parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT")
hou_parm = hou_node.parm("picking")
hou_parm.lock(False)
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/pickscript parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT")
hou_parm = hou_node.parm("pickscript")
hou_parm.lock(False)
hou_parm.set("")
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/caching parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT")
hou_parm = hou_node.parm("caching")
hou_parm.lock(False)
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/vport_shadeopen parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT")
hou_parm = hou_node.parm("vport_shadeopen")
hou_parm.lock(False)
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/vport_displayassubdiv parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT")
hou_parm = hou_node.parm("vport_displayassubdiv")
hou_parm.lock(False)
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/vport_onionskin parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT")
hou_parm = hou_node.parm("vport_onionskin")
hou_parm.lock(False)
hou_parm.set("off")
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/stdswitcher41 parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT")
hou_parm = hou_node.parm("stdswitcher41")
hou_parm.lock(False)
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/viewportlod parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT")
hou_parm = hou_node.parm("viewportlod")
hou_parm.lock(False)
hou_parm.set("full")
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/vm_rendervisibility parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT")
hou_parm = hou_node.parm("vm_rendervisibility")
hou_parm.lock(False)
hou_parm.set("*")
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/vm_rendersubd parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT")
hou_parm = hou_node.parm("vm_rendersubd")
hou_parm.lock(False)
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/vm_subdstyle parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT")
hou_parm = hou_node.parm("vm_subdstyle")
hou_parm.lock(False)
hou_parm.set("mantra_catclark")
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/vm_subdgroup parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT")
hou_parm = hou_node.parm("vm_subdgroup")
hou_parm.lock(False)
hou_parm.set("")
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/vm_osd_quality parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT")
hou_parm = hou_node.parm("vm_osd_quality")
hou_parm.lock(False)
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/vm_osd_vtxinterp parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT")
hou_parm = hou_node.parm("vm_osd_vtxinterp")
hou_parm.lock(False)
hou_parm.set(2)
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/vm_osd_fvarinterp parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT")
hou_parm = hou_node.parm("vm_osd_fvarinterp")
hou_parm.lock(False)
hou_parm.set(4)
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/folder01 parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT")
hou_parm = hou_node.parm("folder01")
hou_parm.lock(False)
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/categories parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT")
hou_parm = hou_node.parm("categories")
hou_parm.lock(False)
hou_parm.set("")
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/reflectmask parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT")
hou_parm = hou_node.parm("reflectmask")
hou_parm.lock(False)
hou_parm.set("*")
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/refractmask parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT")
hou_parm = hou_node.parm("refractmask")
hou_parm.lock(False)
hou_parm.set("*")
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/lightmask parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT")
hou_parm = hou_node.parm("lightmask")
hou_parm.lock(False)
hou_parm.set("*")
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/lightcategories parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT")
hou_parm = hou_node.parm("lightcategories")
hou_parm.lock(False)
hou_parm.set("*")
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/vm_lpetag parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT")
hou_parm = hou_node.parm("vm_lpetag")
hou_parm.lock(False)
hou_parm.set("")
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/vm_volumefilter parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT")
hou_parm = hou_node.parm("vm_volumefilter")
hou_parm.lock(False)
hou_parm.set("box")
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/vm_volumefilterwidth parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT")
hou_parm = hou_node.parm("vm_volumefilterwidth")
hou_parm.lock(False)
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/vm_matte parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT")
hou_parm = hou_node.parm("vm_matte")
hou_parm.lock(False)
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/vm_rayshade parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT")
hou_parm = hou_node.parm("vm_rayshade")
hou_parm.lock(False)
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/geo_velocityblur parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT")
hou_parm = hou_node.parm("geo_velocityblur")
hou_parm.lock(False)
hou_parm.set("off")
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/geo_accelattribute parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT")
hou_parm = hou_node.parm("geo_accelattribute")
hou_parm.lock(False)
hou_parm.set("accel")
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/vm_shadingquality parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT")
hou_parm = hou_node.parm("vm_shadingquality")
hou_parm.lock(False)
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/vm_flatness parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT")
hou_parm = hou_node.parm("vm_flatness")
hou_parm.lock(False)
hou_parm.set(0.050000000000000003)
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/vm_raypredice parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT")
hou_parm = hou_node.parm("vm_raypredice")
hou_parm.lock(False)
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/vm_curvesurface parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT")
hou_parm = hou_node.parm("vm_curvesurface")
hou_parm.lock(False)
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/vm_rmbackface parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT")
hou_parm = hou_node.parm("vm_rmbackface")
hou_parm.lock(False)
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/shop_geometrypath parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT")
hou_parm = hou_node.parm("shop_geometrypath")
hou_parm.lock(False)
hou_parm.set("")
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/vm_forcegeometry parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT")
hou_parm = hou_node.parm("vm_forcegeometry")
hou_parm.lock(False)
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/vm_rendersubdcurves parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT")
hou_parm = hou_node.parm("vm_rendersubdcurves")
hou_parm.lock(False)
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/vm_renderpoints parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT")
hou_parm = hou_node.parm("vm_renderpoints")
hou_parm.lock(False)
hou_parm.set(2)
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/vm_renderpointsas parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT")
hou_parm = hou_node.parm("vm_renderpointsas")
hou_parm.lock(False)
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/vm_usenforpoints parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT")
hou_parm = hou_node.parm("vm_usenforpoints")
hou_parm.lock(False)
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/vm_pointscale parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT")
hou_parm = hou_node.parm("vm_pointscale")
hou_parm.lock(False)
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/vm_pscalediameter parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT")
hou_parm = hou_node.parm("vm_pscalediameter")
hou_parm.lock(False)
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/vm_metavolume parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT")
hou_parm = hou_node.parm("vm_metavolume")
hou_parm.lock(False)
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/vm_coving parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT")
hou_parm = hou_node.parm("vm_coving")
hou_parm.lock(False)
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/vm_materialoverride parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT")
hou_parm = hou_node.parm("vm_materialoverride")
hou_parm.lock(False)
hou_parm.set("compact")
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/vm_overridedetail parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT")
hou_parm = hou_node.parm("vm_overridedetail")
hou_parm.lock(False)
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/vm_procuseroottransform parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT")
hou_parm = hou_node.parm("vm_procuseroottransform")
hou_parm.lock(False)
hou_parm.set(1)
hou_parm.setAutoscope(False)


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "17.5.391")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("17.5.391")
# Update the parent node.
hou_parent = hou_node

# Code for /obj/Node_for_OUTPUT/testgeometry_rubbertoy1
hou_node = hou_parent.createNode("testgeometry_rubbertoy", "testgeometry_rubbertoy1", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(4.25201, -2.23851))
hou_node.bypass(False)
hou_node.setDisplayFlag(False)
hou_node.hide(False)
hou_node.setHighlightFlag(False)
hou_node.setHardLocked(False)
hou_node.setSoftLocked(False)
hou_node.setSelectableTemplateFlag(False)
hou_node.setSelected(False)
hou_node.setRenderFlag(False)
hou_node.setTemplateFlag(False)
hou_node.setUnloadFlag(False)

# Code for /obj/Node_for_OUTPUT/testgeometry_rubbertoy1/t parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT/testgeometry_rubbertoy1")
hou_parm_tuple = hou_node.parmTuple("t")
hou_parm_tuple.lock((False, False, False))
hou_parm_tuple.set((0, 0, 0))
hou_parm_tuple.setAutoscope((False, False, False))


# Code for /obj/Node_for_OUTPUT/testgeometry_rubbertoy1/r parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT/testgeometry_rubbertoy1")
hou_parm_tuple = hou_node.parmTuple("r")
hou_parm_tuple.lock((False, False, False))
hou_parm_tuple.set((0, 0, 0))
hou_parm_tuple.setAutoscope((False, False, False))


# Code for /obj/Node_for_OUTPUT/testgeometry_rubbertoy1/uniformscale parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT/testgeometry_rubbertoy1")
hou_parm = hou_node.parm("uniformscale")
hou_parm.lock(False)
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/testgeometry_rubbertoy1/difficulty parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT/testgeometry_rubbertoy1")
hou_parm = hou_node.parm("difficulty")
hou_parm.lock(False)
hou_parm.set("hard")
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/testgeometry_rubbertoy1/addshader parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT/testgeometry_rubbertoy1")
hou_parm = hou_node.parm("addshader")
hou_parm.lock(False)
hou_parm.set(1)
hou_parm.setAutoscope(False)


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___toolid___", "sop_testgeometry_rubbertoy")
hou_node.setUserData("___Version___", "")
hou_node.setUserData("___toolcount___", "1")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("")
# Code for /obj/Node_for_OUTPUT/by_using_include_file
hou_node = hou_parent.createNode("attribwrangle", "by_using_include_file", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(4.24901, -5.21841))
hou_node.bypass(False)
hou_node.setDisplayFlag(False)
hou_node.hide(False)
hou_node.setHighlightFlag(False)
hou_node.setHardLocked(False)
hou_node.setSoftLocked(False)
hou_node.setSelectableTemplateFlag(False)
hou_node.setSelected(False)
hou_node.setRenderFlag(False)
hou_node.setTemplateFlag(False)
hou_node.setUnloadFlag(False)

hou_parm_template_group = hou.ParmTemplateGroup()
# Code for parameter template
hou_parm_template = hou.FolderParmTemplate("folder1", "Code", folder_type=hou.folderType.Tabs, default_value=0, ends_tab_group=False)
# Code for parameter template
hou_parm_template2 = hou.StringParmTemplate("group", "Group", 1, default_value=([""]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.Regular, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="opmenu -l attribvop1 bindgroup", item_generator_script_language=hou.scriptLanguage.Hscript, menu_type=hou.menuType.StringToggle)
hou_parm_template2.setTags({"autoscope": "0000000000000000", "script_action": "import soputils\nkwargs['geometrytype'] = kwargs['node'].parmTuple('grouptype')\nkwargs['inputindex'] = 0\nsoputils.selectGroupParm(kwargs)", "script_action_help": "Select geometry from an available viewport.", "script_action_icon": "BUTTONS_reselect"})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.MenuParmTemplate("grouptype", "Group Type", menu_items=(["guess","vertices","edges","points","prims"]), menu_labels=(["Guess from Group","Vertices","Edges","Points","Primitives"]), default_value=0, icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal, menu_use_token=False, is_button_strip=False, strip_uses_icons=False)
hou_parm_template2.setTags({"autoscope": "0000000000000000"})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.MenuParmTemplate("class", "Run Over", menu_items=(["detail","primitive","point","vertex","number"]), menu_labels=(["Detail (only once)","Primitives","Points","Vertices","Numbers"]), default_value=2, icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal, menu_use_token=False, is_button_strip=False, strip_uses_icons=False)
hou_parm_template2.setTags({"autoscope": "0000000000000000"})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.IntParmTemplate("vex_numcount", "Number Count", 1, default_value=([10]), min=0, max=10000, min_is_strict=True, max_is_strict=False, naming_scheme=hou.parmNamingScheme.Base1, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal, menu_use_token=False)
hou_parm_template2.setConditional(hou.parmCondType.HideWhen, "{ class != number }")
hou_parm_template2.setTags({"autoscope": "0000000000000000"})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.IntParmTemplate("vex_threadjobsize", "Thread Job Size", 1, default_value=([1024]), min=1, max=10000, min_is_strict=True, max_is_strict=False, naming_scheme=hou.parmNamingScheme.Base1, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal, menu_use_token=False)
hou_parm_template2.setConditional(hou.parmCondType.HideWhen, "{ class != number }")
hou_parm_template2.setTags({"autoscope": "0000000000000000"})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.StringParmTemplate("snippet", "VEXpression", 1, default_value=([""]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.Regular, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="import vexpressionmenu\n\nreturn vexpressionmenu.buildSnippetMenu('attribwrangle/snippet')", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.StringReplace)
hou_parm_template2.setTags({"autoscope": "0000000000000000", "editor": "1", "editorlang": "VEX", "editorlines": "8-30", "script_action": "import vexpressionmenu\n\nnode = kwargs['node']\nparmname = 'snippet'\n\nvexpressionmenu.createSpareParmsFromChCalls(node, parmname)", "script_action_help": "Creates spare parameters for each unique call of ch() ", "script_action_icon": "BUTTONS_create_parm_from_ch"})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.StringParmTemplate("exportlist", "Attributes to Create", 1, default_value=(["*"]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.Regular, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template2.setTags({"autoscope": "0000000000000000"})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.ToggleParmTemplate("vex_strict", "Enforce Prototypes", default_value=False, default_expression='off', default_expression_language=hou.scriptLanguage.Hscript)
hou_parm_template2.setTags({"autoscope": "0000000000000000", "script_callback": ""})
hou_parm_template.addParmTemplate(hou_parm_template2)
hou_parm_template_group.append(hou_parm_template)
# Code for parameter template
hou_parm_template = hou.FolderParmTemplate("folder1_1", "Bindings", folder_type=hou.folderType.Tabs, default_value=0, ends_tab_group=False)
# Code for parameter template
hou_parm_template2 = hou.ToggleParmTemplate("autobind", "Autobind by Name", default_value=True, default_expression='on', default_expression_language=hou.scriptLanguage.Hscript)
hou_parm_template2.setTags({"autoscope": "0000000000000000"})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.FolderParmTemplate("bindings", "Number of Bindings", folder_type=hou.folderType.MultiparmBlock, default_value=0, ends_tab_group=False)
hou_parm_template2.setTags({"autoscope": "0000000000000000", "multistartoffset": "1"})
# Code for parameter template
hou_parm_template3 = hou.StringParmTemplate("bindname#", "Attribute Name", 1, default_value=([""]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.Regular, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template2.addParmTemplate(hou_parm_template3)
# Code for parameter template
hou_parm_template3 = hou.StringParmTemplate("bindparm#", "VEX Parameter", 1, default_value=([""]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.Regular, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template2.addParmTemplate(hou_parm_template3)
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.ToggleParmTemplate("groupautobind", "Autobind Groups by Name", default_value=True, default_expression='on', default_expression_language=hou.scriptLanguage.Hscript)
hou_parm_template2.setTags({"autoscope": "0000000000000000"})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.FolderParmTemplate("groupbindings", "Group Bindings", folder_type=hou.folderType.MultiparmBlock, default_value=0, ends_tab_group=False)
hou_parm_template2.setTags({"autoscope": "0000000000000000", "multistartoffset": "1"})
# Code for parameter template
hou_parm_template3 = hou.StringParmTemplate("bindgroupname#", "Group Name", 1, default_value=([""]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.Regular, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template2.addParmTemplate(hou_parm_template3)
# Code for parameter template
hou_parm_template3 = hou.StringParmTemplate("bindgroupparm#", "VEX Parameter", 1, default_value=([""]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.Regular, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template2.addParmTemplate(hou_parm_template3)
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.StringParmTemplate("vex_cwdpath", "Evaluation Node Path", 1, default_value=(["."]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.NodeReference, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template2.setTags({"autoscope": "0000000000000000", "oprelative": "."})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.StringParmTemplate("vex_outputmask", "Export Parameters", 1, default_value=(["*"]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.Regular, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template2.setTags({"autoscope": "0000000000000000"})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.ToggleParmTemplate("vex_updatenmls", "Update Normals If Displaced", default_value=False, default_expression='off', default_expression_language=hou.scriptLanguage.Hscript)
hou_parm_template2.setTags({"autoscope": "0000000000000000", "script_callback": ""})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.StringParmTemplate("vex_matchattrib", "Attribute to Match", 1, default_value=(["id"]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.Regular, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template2.setTags({"autoscope": "0000000000000000"})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.ToggleParmTemplate("vex_inplace", "Compute Results In Place", default_value=False, default_expression='off', default_expression_language=hou.scriptLanguage.Hscript)
hou_parm_template2.setTags({"autoscope": "0000000000000000"})
hou_parm_template.addParmTemplate(hou_parm_template2)
# Code for parameter template
hou_parm_template2 = hou.StringParmTemplate("vex_selectiongroup", "Output Selection Group", 1, default_value=([""]), naming_scheme=hou.parmNamingScheme.Base1, string_type=hou.stringParmType.Regular, menu_items=([]), menu_labels=([]), icon_names=([]), item_generator_script="", item_generator_script_language=hou.scriptLanguage.Python, menu_type=hou.menuType.Normal)
hou_parm_template2.setTags({"autoscope": "0000000000000000"})
hou_parm_template.addParmTemplate(hou_parm_template2)
hou_parm_template_group.append(hou_parm_template)
# Code for parameter template
hou_parm_template = hou.FloatParmTemplate("scale", "Scale", 1, default_value=([0]), min=0, max=1, min_is_strict=False, max_is_strict=False, look=hou.parmLook.Regular, naming_scheme=hou.parmNamingScheme.Base1)
hou_parm_template_group.append(hou_parm_template)
hou_node.setParmTemplateGroup(hou_parm_template_group)
# Code for /obj/Node_for_OUTPUT/by_using_include_file/folder01 parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT/by_using_include_file")
hou_parm = hou_node.parm("folder01")
hou_parm.lock(False)
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/by_using_include_file/group parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT/by_using_include_file")
hou_parm = hou_node.parm("group")
hou_parm.lock(False)
hou_parm.set("")
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/by_using_include_file/grouptype parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT/by_using_include_file")
hou_parm = hou_node.parm("grouptype")
hou_parm.lock(False)
hou_parm.set("guess")
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/by_using_include_file/class parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT/by_using_include_file")
hou_parm = hou_node.parm("class")
hou_parm.lock(False)
hou_parm.set("primitive")
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/by_using_include_file/vex_numcount parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT/by_using_include_file")
hou_parm = hou_node.parm("vex_numcount")
hou_parm.lock(False)
hou_parm.set(10)
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/by_using_include_file/vex_threadjobsize parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT/by_using_include_file")
hou_parm = hou_node.parm("vex_threadjobsize")
hou_parm.lock(False)
hou_parm.set(1024)
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/by_using_include_file/snippet parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT/by_using_include_file")
hou_parm = hou_node.parm("snippet")
hou_parm.lock(False)
hou_parm.set("#include \"Utility.h\"\nvector pos = getPrimCenter(0,@primnum);\nint pt = addpoint(0,pos);\nsetpointattrib(0,\"pscale\",pt,f@area*ch(\"scale\"));\nvector n = prim_normal(0,@primnum,0.5,0.5);\nsetpointattrib(0,\"N\",pt,n);\nremoveprim(0,@primnum,1);")
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/by_using_include_file/exportlist parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT/by_using_include_file")
hou_parm = hou_node.parm("exportlist")
hou_parm.lock(False)
hou_parm.set("*")
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/by_using_include_file/vex_strict parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT/by_using_include_file")
hou_parm = hou_node.parm("vex_strict")
hou_parm.lock(False)
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/by_using_include_file/autobind parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT/by_using_include_file")
hou_parm = hou_node.parm("autobind")
hou_parm.lock(False)
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/by_using_include_file/bindings parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT/by_using_include_file")
hou_parm = hou_node.parm("bindings")
hou_parm.lock(False)
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/by_using_include_file/groupautobind parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT/by_using_include_file")
hou_parm = hou_node.parm("groupautobind")
hou_parm.lock(False)
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/by_using_include_file/groupbindings parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT/by_using_include_file")
hou_parm = hou_node.parm("groupbindings")
hou_parm.lock(False)
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/by_using_include_file/vex_cwdpath parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT/by_using_include_file")
hou_parm = hou_node.parm("vex_cwdpath")
hou_parm.lock(False)
hou_parm.set(".")
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/by_using_include_file/vex_outputmask parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT/by_using_include_file")
hou_parm = hou_node.parm("vex_outputmask")
hou_parm.lock(False)
hou_parm.set("*")
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/by_using_include_file/vex_updatenmls parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT/by_using_include_file")
hou_parm = hou_node.parm("vex_updatenmls")
hou_parm.lock(False)
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/by_using_include_file/vex_matchattrib parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT/by_using_include_file")
hou_parm = hou_node.parm("vex_matchattrib")
hou_parm.lock(False)
hou_parm.set("id")
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/by_using_include_file/vex_inplace parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT/by_using_include_file")
hou_parm = hou_node.parm("vex_inplace")
hou_parm.lock(False)
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/by_using_include_file/vex_selectiongroup parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT/by_using_include_file")
hou_parm = hou_node.parm("vex_selectiongroup")
hou_parm.lock(False)
hou_parm.set("")
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/by_using_include_file/folder11 parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT/by_using_include_file")
hou_parm = hou_node.parm("folder11")
hou_parm.lock(False)
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/by_using_include_file/scale parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT/by_using_include_file")
hou_parm = hou_node.parm("scale")
hou_parm.lock(False)
hou_parm.set(15)
hou_parm.setAutoscope(False)


hou_node.setColor(hou.Color([0.996, 0.682, 0.682]))
hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("")
# Code for /obj/Node_for_OUTPUT/circle1
hou_node = hou_parent.createNode("circle", "circle1", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(1.38201, -5.21741))
hou_node.bypass(False)
hou_node.setDisplayFlag(False)
hou_node.hide(False)
hou_node.setHighlightFlag(False)
hou_node.setHardLocked(False)
hou_node.setSoftLocked(False)
hou_node.setSelectableTemplateFlag(False)
hou_node.setSelected(False)
hou_node.setRenderFlag(False)
hou_node.setTemplateFlag(False)
hou_node.setUnloadFlag(False)

# Code for /obj/Node_for_OUTPUT/circle1/type parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT/circle1")
hou_parm = hou_node.parm("type")
hou_parm.lock(False)
hou_parm.set("prim")
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/circle1/orient parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT/circle1")
hou_parm = hou_node.parm("orient")
hou_parm.lock(False)
hou_parm.set("xy")
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/circle1/rad parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT/circle1")
hou_parm_tuple = hou_node.parmTuple("rad")
hou_parm_tuple.lock((False, False))
hou_parm_tuple.set((1, 1))
hou_parm_tuple.setAutoscope((False, False))


# Code for /obj/Node_for_OUTPUT/circle1/t parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT/circle1")
hou_parm_tuple = hou_node.parmTuple("t")
hou_parm_tuple.lock((False, False, False))
hou_parm_tuple.set((0, 0, 0))
hou_parm_tuple.setAutoscope((False, False, False))


# Code for /obj/Node_for_OUTPUT/circle1/r parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT/circle1")
hou_parm_tuple = hou_node.parmTuple("r")
hou_parm_tuple.lock((False, False, False))
hou_parm_tuple.set((0, 0, 0))
hou_parm_tuple.setAutoscope((False, False, False))


# Code for /obj/Node_for_OUTPUT/circle1/scale parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT/circle1")
hou_parm = hou_node.parm("scale")
hou_parm.lock(False)
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/circle1/order parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT/circle1")
hou_parm = hou_node.parm("order")
hou_parm.lock(False)
hou_parm.set(4)
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/circle1/divs parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT/circle1")
hou_parm = hou_node.parm("divs")
hou_parm.lock(False)
hou_parm.set(12)
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/circle1/arc parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT/circle1")
hou_parm = hou_node.parm("arc")
hou_parm.lock(False)
hou_parm.set("closed")
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/circle1/angle parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT/circle1")
hou_parm_tuple = hou_node.parmTuple("angle")
hou_parm_tuple.lock((False, False))
hou_parm_tuple.set((0, 360))
hou_parm_tuple.setAutoscope((False, False))


# Code for /obj/Node_for_OUTPUT/circle1/imperfect parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT/circle1")
hou_parm = hou_node.parm("imperfect")
hou_parm.lock(False)
hou_parm.set(1)
hou_parm.setAutoscope(False)


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "17.5.391")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("17.5.391")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code for /obj/Node_for_OUTPUT/measure1
hou_node = hou_parent.createNode("measure::2.0", "measure1", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(4.25201, -3.81851))
hou_node.bypass(False)
hou_node.setDisplayFlag(False)
hou_node.hide(False)
hou_node.setHighlightFlag(False)
hou_node.setHardLocked(False)
hou_node.setSoftLocked(False)
hou_node.setSelectableTemplateFlag(False)
hou_node.setSelected(False)
hou_node.setRenderFlag(False)
hou_node.setTemplateFlag(True)
hou_node.setUnloadFlag(False)

# Code for /obj/Node_for_OUTPUT/measure1/group parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT/measure1")
hou_parm = hou_node.parm("group")
hou_parm.lock(False)
hou_parm.set("")
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/measure1/grouptype parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT/measure1")
hou_parm = hou_node.parm("grouptype")
hou_parm.lock(False)
hou_parm.set("prims")
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/measure1/measurement parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT/measure1")
hou_parm = hou_node.parm("measurement")
hou_parm.lock(False)
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/measure1/measure parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT/measure1")
hou_parm = hou_node.parm("measure")
hou_parm.lock(False)
hou_parm.set("area")
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/measure1/curvaturetype parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT/measure1")
hou_parm = hou_node.parm("curvaturetype")
hou_parm.lock(False)
hou_parm.set("gaussian")
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/measure1/principaltype parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT/measure1")
hou_parm = hou_node.parm("principaltype")
hou_parm.lock(False)
hou_parm.set("min")
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/measure1/principalsign parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT/measure1")
hou_parm = hou_node.parm("principalsign")
hou_parm.lock(False)
hou_parm.set("signed")
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/measure1/principalreportas parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT/measure1")
hou_parm = hou_node.parm("principalreportas")
hou_parm.lock(False)
hou_parm.set("scalar")
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/measure1/umbiliccutoff parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT/measure1")
hou_parm = hou_node.parm("umbiliccutoff")
hou_parm.lock(False)
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/measure1/integrationmode parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT/measure1")
hou_parm = hou_node.parm("integrationmode")
hou_parm.lock(False)
hou_parm.set("componentwise")
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/measure1/srcattrib parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT/measure1")
hou_parm = hou_node.parm("srcattrib")
hou_parm.lock(False)
hou_parm.set("P")
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/measure1/srccomp parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT/measure1")
hou_parm = hou_node.parm("srccomp")
hou_parm.lock(False)
hou_parm.set("x")
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/measure1/scalenormalize parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT/measure1")
hou_parm = hou_node.parm("scalenormalize")
hou_parm.lock(False)
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/measure1/integrationdomain parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT/measure1")
hou_parm = hou_node.parm("integrationdomain")
hou_parm.lock(False)
hou_parm.set("element")
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/measure1/pieceattrib parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT/measure1")
hou_parm = hou_node.parm("pieceattrib")
hou_parm.lock(False)
hou_parm.set("class")
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/measure1/usecustompos parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT/measure1")
hou_parm = hou_node.parm("usecustompos")
hou_parm.lock(False)
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/measure1/posattrib parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT/measure1")
hou_parm = hou_node.parm("posattrib")
hou_parm.lock(False)
hou_parm.set("P")
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/measure1/visrange parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT/measure1")
hou_parm = hou_node.parm("visrange")
hou_parm.lock(False)
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/measure1/userangemin parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT/measure1")
hou_parm = hou_node.parm("userangemin")
hou_parm.lock(False)
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/measure1/rangemin parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT/measure1")
hou_parm = hou_node.parm("rangemin")
hou_parm.lock(False)
hou_parm.set(-1)
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/measure1/userangemax parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT/measure1")
hou_parm = hou_node.parm("userangemax")
hou_parm.lock(False)
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/measure1/rangemax parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT/measure1")
hou_parm = hou_node.parm("rangemax")
hou_parm.lock(False)
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/measure1/usecenterwidth parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT/measure1")
hou_parm = hou_node.parm("usecenterwidth")
hou_parm.lock(False)
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/measure1/width parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT/measure1")
hou_parm = hou_node.parm("width")
hou_parm.lock(False)
hou_parm.set(6)
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/measure1/widthscale parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT/measure1")
hou_parm = hou_node.parm("widthscale")
hou_parm.lock(False)
hou_parm.set("mad")
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/measure1/centertype parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT/measure1")
hou_parm = hou_node.parm("centertype")
hou_parm.lock(False)
hou_parm.set("median")
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/measure1/fixedcenter parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT/measure1")
hou_parm = hou_node.parm("fixedcenter")
hou_parm.lock(False)
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/measure1/colorramp parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT/measure1")
hou_parm = hou_node.parm("colorramp")
hou_parm.lock(False)
hou_parm.set(3)
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/measure1/vectorscale parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT/measure1")
hou_parm = hou_node.parm("vectorscale")
hou_parm.lock(False)
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/measure1/output parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT/measure1")
hou_parm = hou_node.parm("output")
hou_parm.lock(False)
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/measure1/attribname parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT/measure1")
hou_parm = hou_node.parm("attribname")
hou_parm.lock(False)
hou_parm.set("area")
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/measure1/usetotalattrib parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT/measure1")
hou_parm = hou_node.parm("usetotalattrib")
hou_parm.lock(False)
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/measure1/totalattribname parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT/measure1")
hou_parm = hou_node.parm("totalattribname")
hou_parm.lock(False)
hou_parm.set("totalarea")
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/measure1/userangegroup parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT/measure1")
hou_parm = hou_node.parm("userangegroup")
hou_parm.lock(False)
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/measure1/rangegroup parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT/measure1")
hou_parm = hou_node.parm("rangegroup")
hou_parm.lock(False)
hou_parm.set("inrange")
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/measure1/bakeintooutput parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT/measure1")
hou_parm = hou_node.parm("bakeintooutput")
hou_parm.lock(False)
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/measure1/useremaprange parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT/measure1")
hou_parm = hou_node.parm("useremaprange")
hou_parm.lock(False)
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/measure1/remaprange parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT/measure1")
hou_parm_tuple = hou_node.parmTuple("remaprange")
hou_parm_tuple.lock((False, False))
hou_parm_tuple.set((0, 1))
hou_parm_tuple.setAutoscope((False, False))


# Code for /obj/Node_for_OUTPUT/measure1/colorramp1pos parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT/measure1")
hou_parm = hou_node.parm("colorramp1pos")
hou_parm.lock(False)
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/measure1/colorramp1c parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT/measure1")
hou_parm_tuple = hou_node.parmTuple("colorramp1c")
hou_parm_tuple.lock((False, False, False))
hou_parm_tuple.set((0, 0, 1))
hou_parm_tuple.setAutoscope((False, False, False))


# Code for /obj/Node_for_OUTPUT/measure1/colorramp1interp parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT/measure1")
hou_parm = hou_node.parm("colorramp1interp")
hou_parm.lock(False)
hou_parm.set("linear")
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/measure1/colorramp2pos parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT/measure1")
hou_parm = hou_node.parm("colorramp2pos")
hou_parm.lock(False)
hou_parm.set(0.5)
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/measure1/colorramp2c parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT/measure1")
hou_parm_tuple = hou_node.parmTuple("colorramp2c")
hou_parm_tuple.lock((False, False, False))
hou_parm_tuple.set((1, 1, 1))
hou_parm_tuple.setAutoscope((False, False, False))


# Code for /obj/Node_for_OUTPUT/measure1/colorramp2interp parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT/measure1")
hou_parm = hou_node.parm("colorramp2interp")
hou_parm.lock(False)
hou_parm.set("linear")
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/measure1/colorramp3pos parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT/measure1")
hou_parm = hou_node.parm("colorramp3pos")
hou_parm.lock(False)
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/measure1/colorramp3c parm tuple
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT/measure1")
hou_parm_tuple = hou_node.parmTuple("colorramp3c")
hou_parm_tuple.lock((False, False, False))
hou_parm_tuple.set((1, 0, 0))
hou_parm_tuple.setAutoscope((False, False, False))


# Code for /obj/Node_for_OUTPUT/measure1/colorramp3interp parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT/measure1")
hou_parm = hou_node.parm("colorramp3interp")
hou_parm.lock(False)
hou_parm.set("linear")
hou_parm.setAutoscope(False)


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "17.5.391")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("17.5.391")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code for /obj/Node_for_OUTPUT/copytopoints1
hou_node = hou_parent.createNode("copytopoints", "copytopoints1", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(3.31701, -6.55851))
hou_node.bypass(False)
hou_node.setDisplayFlag(False)
hou_node.hide(False)
hou_node.setHighlightFlag(False)
hou_node.setHardLocked(False)
hou_node.setSoftLocked(False)
hou_node.setSelectableTemplateFlag(False)
hou_node.setSelected(False)
hou_node.setRenderFlag(False)
hou_node.setTemplateFlag(False)
hou_node.setUnloadFlag(False)

# Code for /obj/Node_for_OUTPUT/copytopoints1/sourcegroup parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT/copytopoints1")
hou_parm = hou_node.parm("sourcegroup")
hou_parm.lock(False)
hou_parm.set("")
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/copytopoints1/targetgroup parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT/copytopoints1")
hou_parm = hou_node.parm("targetgroup")
hou_parm.lock(False)
hou_parm.set("")
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/copytopoints1/showguide parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT/copytopoints1")
hou_parm = hou_node.parm("showguide")
hou_parm.lock(False)
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/copytopoints1/pack parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT/copytopoints1")
hou_parm = hou_node.parm("pack")
hou_parm.lock(False)
hou_parm.set(0)
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/copytopoints1/pivot parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT/copytopoints1")
hou_parm = hou_node.parm("pivot")
hou_parm.lock(False)
hou_parm.set("centroid")
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/copytopoints1/viewportlod parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT/copytopoints1")
hou_parm = hou_node.parm("viewportlod")
hou_parm.lock(False)
hou_parm.set("full")
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/copytopoints1/transform parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT/copytopoints1")
hou_parm = hou_node.parm("transform")
hou_parm.lock(False)
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/copytopoints1/doattr parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT/copytopoints1")
hou_parm = hou_node.parm("doattr")
hou_parm.lock(False)
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/copytopoints1/setpt parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT/copytopoints1")
hou_parm = hou_node.parm("setpt")
hou_parm.lock(False)
hou_parm.set("*,^v,^Alpha,^N")
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/copytopoints1/mulpt parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT/copytopoints1")
hou_parm = hou_node.parm("mulpt")
hou_parm.lock(False)
hou_parm.set("Alpha")
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/copytopoints1/addpt parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT/copytopoints1")
hou_parm = hou_node.parm("addpt")
hou_parm.lock(False)
hou_parm.set("v")
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/copytopoints1/subpt parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT/copytopoints1")
hou_parm = hou_node.parm("subpt")
hou_parm.lock(False)
hou_parm.set("")
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/copytopoints1/setprim parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT/copytopoints1")
hou_parm = hou_node.parm("setprim")
hou_parm.lock(False)
hou_parm.set("")
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/copytopoints1/mulprim parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT/copytopoints1")
hou_parm = hou_node.parm("mulprim")
hou_parm.lock(False)
hou_parm.set("")
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/copytopoints1/addprim parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT/copytopoints1")
hou_parm = hou_node.parm("addprim")
hou_parm.lock(False)
hou_parm.set("")
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/copytopoints1/subprim parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT/copytopoints1")
hou_parm = hou_node.parm("subprim")
hou_parm.lock(False)
hou_parm.set("")
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/copytopoints1/setvtx parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT/copytopoints1")
hou_parm = hou_node.parm("setvtx")
hou_parm.lock(False)
hou_parm.set("")
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/copytopoints1/mulvtx parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT/copytopoints1")
hou_parm = hou_node.parm("mulvtx")
hou_parm.lock(False)
hou_parm.set("")
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/copytopoints1/addvtx parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT/copytopoints1")
hou_parm = hou_node.parm("addvtx")
hou_parm.lock(False)
hou_parm.set("")
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/copytopoints1/subvtx parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT/copytopoints1")
hou_parm = hou_node.parm("subvtx")
hou_parm.lock(False)
hou_parm.set("")
hou_parm.setAutoscope(False)


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "17.5.391")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("17.5.391")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code for /obj/Node_for_OUTPUT/OUT
hou_node = hou_parent.createNode("null", "OUT", run_init_scripts=False, load_contents=True, exact_type_name=True)
hou_node.move(hou.Vector2(3.31701, -7.82051))
hou_node.bypass(False)
hou_node.setDisplayFlag(True)
hou_node.hide(False)
hou_node.setHighlightFlag(False)
hou_node.setHardLocked(False)
hou_node.setSoftLocked(False)
hou_node.setSelectableTemplateFlag(False)
hou_node.setSelected(False)
hou_node.setRenderFlag(True)
hou_node.setTemplateFlag(False)
hou_node.setUnloadFlag(False)

# Code for /obj/Node_for_OUTPUT/OUT/copyinput parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT/OUT")
hou_parm = hou_node.parm("copyinput")
hou_parm.lock(False)
hou_parm.set(1)
hou_parm.setAutoscope(False)


# Code for /obj/Node_for_OUTPUT/OUT/cacheinput parm 
if locals().get("hou_node") is None:
    hou_node = hou.node("/obj/Node_for_OUTPUT/OUT")
hou_parm = hou_node.parm("cacheinput")
hou_parm.lock(False)
hou_parm.set(0)
hou_parm.setAutoscope(False)


hou_node.setExpressionLanguage(hou.exprLanguage.Hscript)

hou_node.setUserData("___Version___", "17.5.391")
if hasattr(hou_node, "syncNodeVersionIfNeeded"):
    hou_node.syncNodeVersionIfNeeded("17.5.391")
# Update the parent node.
hou_parent = hou_node


# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

# Code to establish connections for /obj/Node_for_OUTPUT/by_using_include_file
hou_node = hou_parent.node("by_using_include_file")
if hou_parent.node("measure1") is not None:
    hou_node.setInput(0, hou_parent.node("measure1"), 0)
# Code to establish connections for /obj/Node_for_OUTPUT/measure1
hou_node = hou_parent.node("measure1")
if hou_parent.node("testgeometry_rubbertoy1") is not None:
    hou_node.setInput(0, hou_parent.node("testgeometry_rubbertoy1"), 0)
# Code to establish connections for /obj/Node_for_OUTPUT/copytopoints1
hou_node = hou_parent.node("copytopoints1")
if hou_parent.node("circle1") is not None:
    hou_node.setInput(0, hou_parent.node("circle1"), 0)
if hou_parent.node("by_using_include_file") is not None:
    hou_node.setInput(1, hou_parent.node("by_using_include_file"), 0)
# Code to establish connections for /obj/Node_for_OUTPUT/OUT
hou_node = hou_parent.node("OUT")
if hou_parent.node("copytopoints1") is not None:
    hou_node.setInput(0, hou_parent.node("copytopoints1"), 0)

# Restore the parent and current nodes.
hou_parent = hou_parent.parent()
hou_node = hou_node.parent()

