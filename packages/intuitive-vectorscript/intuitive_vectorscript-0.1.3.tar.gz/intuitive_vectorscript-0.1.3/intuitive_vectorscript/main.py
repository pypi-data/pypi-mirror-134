import intuitive_vectorscript as ivs

dialog = ivs.Dialog("Test")

item1 = dialog.create_item(0, "TextField")
item2 = dialog.create_item(1, "PDMenu")
item3 = dialog.create_item(2, "IntegerField")
item4 = dialog.create_item(3, "PDMenu")
item5 = dialog.create_item(4, "ClassPDMenu")
item6 = dialog.create_item(5, "LayerPDMenu")
item7 = dialog.create_item(6, "SheetLayerPDMenu")

item3.set_default_value(120)
item1.set_default_value("12")

arg = {0: "test", 1: "fsü"}
item2.add_choices(arg)
item4.add_choices(arg)
item7.set_bounding(bottom={"fixed_binding": True, "prop_binding": False})

item3.set_editable(False)
dialog.create_my_dialog()
