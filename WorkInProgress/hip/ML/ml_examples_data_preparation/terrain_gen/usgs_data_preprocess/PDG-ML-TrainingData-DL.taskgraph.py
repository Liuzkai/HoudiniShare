import pdg
file_pdg_version = (0,0,1)

def deserializeWorkItems(context):
    context.beginDeserialization()
    s = pdg.WorkItem.Serialization()
    s.nodeName = 'fetch_download_list'
    s.name = 'fetch_download_list0'
    s.baseName = 'fetch_download_list0'
    s.index = 0
    s.isStatic = True
    s.state = pdg.workItemState.CookedSuccess
    s.type = pdg.workItemType.Regular
    context.addWorkItem(s)
    context.addWorkItemData('GenericData', 'fetch_download_list0', '[{},{},{"directory":["__PDG_DIR__/downloadlist"],"filename":["Rockies-small-FLT.txt"],"extension":[".txt"]}]', (), {})
    context.addWorkItemResults('fetch_download_list0', ['__PDG_DIR__/downloadlist/Rockies-small-FLT.txt',],['file/text',],[1551379270,],[False,],[False,])
    s = pdg.WorkItem.Serialization()
    s.nodeName = 'build_csv_filename'
    s.name = 'build_csv_filename0'
    s.baseName = 'build_csv_filename0'
    s.index = 0
    s.isStatic = True
    s.isCloneResultData = True
    s.state = pdg.workItemState.CookedSuccess
    s.type = pdg.workItemType.Regular
    context.addWorkItem(s)
    context.addWorkItemData('GenericData', 'build_csv_filename0', '[{},{},{"directory":["__PDG_DIR__/downloadlist"],"csv_filename":["/mnt/hq/ML/examples/terrain_gen/usgs_data_preprocess/CSV/downloadlist_0.csv"],"filename":["Rockies-small-FLT.txt"],"extension":[".txt"]}]', (), {})
    context.addWorkItemResults('build_csv_filename0', ['__PDG_DIR__/downloadlist/Rockies-small-FLT.txt',],['file/text',],[1551379270,],[False,],[False,])
    s = pdg.WorkItem.Serialization()
    s.nodeName = 'TXT_to_CSV'
    s.name = 'TXT_to_CSV0'
    s.baseName = 'TXT_to_CSV0'
    s.parentName = 'build_csv_filename0'
    s.staticAncestorNames = ['build_csv_filename0',]
    s.index = 0
    s.state = pdg.workItemState.CookedSuccess
    s.type = pdg.workItemType.Regular
    context.addWorkItem(s)
    context.addWorkItemData('GenericData', 'TXT_to_CSV0', '[{},{},{"directory":["__PDG_DIR__/downloadlist"],"csv_filename":["/mnt/hq/ML/examples/terrain_gen/usgs_data_preprocess/CSV/downloadlist_0.csv"],"filename":["Rockies-small-FLT.txt"],"extension":[".txt"]}]', (), {})
    context.addWorkItemResults('TXT_to_CSV0', ['/mnt/hq/ML/examples/terrain_gen/usgs_data_preprocess/CSV/downloadlist_0.csv',],['file/csv',],[0,],[False,],[True,])
    s = pdg.WorkItem.Serialization()
    s.nodeName = 'read_download_url'
    s.name = 'read_download_url0'
    s.baseName = 'read_download_url0'
    s.parentName = 'TXT_to_CSV0'
    s.staticAncestorNames = ['build_csv_filename0',]
    s.index = 0
    s.state = pdg.workItemState.CookedSuccess
    s.type = pdg.workItemType.Regular
    context.addWorkItem(s)
    context.addWorkItemData('GenericData', 'read_download_url0', '[{},{},{"column_0":["https://prd-tnm.s3.amazonaws.com/StagedProducts/Elevation/13/GridFloat/USGS_NED_13_n46w115_GridFloat.zip"],"directory":["__PDG_DIR__/downloadlist"],"csv_filename":["/mnt/hq/ML/examples/terrain_gen/usgs_data_preprocess/CSV/downloadlist_0.csv"],"filename":["Rockies-small-FLT.txt"],"extension":[".txt"]}]', (), {})
    s = pdg.WorkItem.Serialization()
    s.nodeName = 'pythonhttpsverify'
    s.name = 'pythonhttpsverify0_3'
    s.baseName = 'pythonhttpsverify0'
    s.parentName = 'read_download_url0'
    s.staticAncestorNames = ['build_csv_filename0',]
    s.environment = {'PYTHONHTTPSVERIFY':0,}
    s.index = 0
    s.isClearEnvironment = True
    s.isCloneResultData = True
    s.state = pdg.workItemState.CookedSuccess
    s.type = pdg.workItemType.Regular
    context.addWorkItem(s)
    context.addWorkItemData('GenericData', 'pythonhttpsverify0_3', '[{},{},{"column_0":["https://prd-tnm.s3.amazonaws.com/StagedProducts/Elevation/13/GridFloat/USGS_NED_13_n46w115_GridFloat.zip"],"directory":["__PDG_DIR__/downloadlist"],"csv_filename":["/mnt/hq/ML/examples/terrain_gen/usgs_data_preprocess/CSV/downloadlist_0.csv"],"filename":["Rockies-small-FLT.txt"],"extension":[".txt"]}]', (), {})
    s = pdg.WorkItem.Serialization()
    s.nodeName = 'create_height_export_filepath'
    s.name = 'create_height_export_filepath_static_wrapper0'
    s.baseName = 'create_height_export_filepath_static_wrapper0'
    s.staticAncestorNames = ['build_csv_filename0',]
    s.index = 0
    s.frame = 0
    s.hasFrame = True
    s.isControl = True
    s.state = pdg.workItemState.Waiting
    s.type = pdg.workItemType.StaticWrapper
    context.addWorkItem(s)
    s = pdg.WorkItem.Serialization()
    s.nodeName = 'import_terrain_file'
    s.name = 'import_terrain_file_static_wrapper0'
    s.baseName = 'import_terrain_file_static_wrapper0'
    s.staticAncestorNames = ['build_csv_filename0',]
    s.index = 0
    s.frame = 0
    s.hasFrame = True
    s.isControl = True
    s.state = pdg.workItemState.Waiting
    s.type = pdg.workItemType.StaticWrapper
    context.addWorkItem(s)
    s = pdg.WorkItem.Serialization()
    s.nodeName = 'read_download_url'
    s.name = 'read_download_url0_2'
    s.baseName = 'read_download_url0'
    s.parentName = 'TXT_to_CSV0'
    s.staticAncestorNames = ['build_csv_filename0',]
    s.index = 0
    s.state = pdg.workItemState.CookedSuccess
    s.type = pdg.workItemType.Regular
    context.addWorkItem(s)
    context.addWorkItemData('GenericData', 'read_download_url0_2', '[{},{},{"column_0":["https://prd-tnm.s3.amazonaws.com/StagedProducts/Elevation/13/GridFloat/USGS_NED_13_n46w114_GridFloat.zip"],"directory":["__PDG_DIR__/downloadlist"],"csv_filename":["/mnt/hq/ML/examples/terrain_gen/usgs_data_preprocess/CSV/downloadlist_0.csv"],"filename":["Rockies-small-FLT.txt"],"extension":[".txt"]}]', (), {})
    s = pdg.WorkItem.Serialization()
    s.nodeName = 'pythonhttpsverify'
    s.name = 'pythonhttpsverify0_2'
    s.baseName = 'pythonhttpsverify0'
    s.parentName = 'read_download_url0_2'
    s.staticAncestorNames = ['build_csv_filename0',]
    s.environment = {'PYTHONHTTPSVERIFY':0,}
    s.index = 0
    s.isClearEnvironment = True
    s.isCloneResultData = True
    s.state = pdg.workItemState.CookedSuccess
    s.type = pdg.workItemType.Regular
    context.addWorkItem(s)
    context.addWorkItemData('GenericData', 'pythonhttpsverify0_2', '[{},{},{"column_0":["https://prd-tnm.s3.amazonaws.com/StagedProducts/Elevation/13/GridFloat/USGS_NED_13_n46w114_GridFloat.zip"],"directory":["__PDG_DIR__/downloadlist"],"csv_filename":["/mnt/hq/ML/examples/terrain_gen/usgs_data_preprocess/CSV/downloadlist_0.csv"],"filename":["Rockies-small-FLT.txt"],"extension":[".txt"]}]', (), {})
    s = pdg.WorkItem.Serialization()
    s.nodeName = 'download_files'
    s.name = 'download_files0'
    s.baseName = 'download_files0'
    s.command = 'python "/mnt/hq/ML/examples/terrain_gen/usgs_data_preprocess/pdgtemp/18108/scripts/download_files0.py"'
    s.parentName = 'pythonhttpsverify0_2'
    s.staticAncestorNames = ['build_csv_filename0',]
    s.index = 0
    s.state = pdg.workItemState.CookedCancel
    s.type = pdg.workItemType.Regular
    context.addWorkItem(s)
    context.addWorkItemData('GenericData', 'download_files0', '[{},{},{"column_0":["https://prd-tnm.s3.amazonaws.com/StagedProducts/Elevation/13/GridFloat/USGS_NED_13_n46w114_GridFloat.zip"],"directory":["__PDG_DIR__/downloadlist"],"csv_filename":["/mnt/hq/ML/examples/terrain_gen/usgs_data_preprocess/CSV/downloadlist_0.csv"],"filename":["Rockies-small-FLT.txt"],"extension":[".txt"]}]', (), {})
    context.addWorkItemResults('download_files0', ['__PDG_DIR__/output/USGS_NED_13_n46w114_GridFloat.zip',],['file/archive',],[0,],[False,],[True,])
    s = pdg.WorkItem.Serialization()
    s.nodeName = 'export_heightfields'
    s.name = 'export_heightfields_static_wrapper0'
    s.baseName = 'export_heightfields_static_wrapper0'
    s.staticAncestorNames = ['build_csv_filename0',]
    s.index = 0
    s.frame = 0
    s.hasFrame = True
    s.isControl = True
    s.state = pdg.workItemState.Waiting
    s.type = pdg.workItemType.StaticWrapper
    context.addWorkItem(s)
    s = pdg.WorkItem.Serialization()
    s.nodeName = 'split_terrain_to_tiles'
    s.name = 'split_terrain_to_tiles_static_wrapper0'
    s.baseName = 'split_terrain_to_tiles_static_wrapper0'
    s.staticAncestorNames = ['build_csv_filename0',]
    s.index = 0
    s.frame = 0
    s.hasFrame = True
    s.isControl = True
    s.state = pdg.workItemState.Waiting
    s.type = pdg.workItemType.StaticWrapper
    context.addWorkItem(s)
    s = pdg.WorkItem.Serialization()
    s.nodeName = 'download_files'
    s.name = 'download_files0_1'
    s.baseName = 'download_files0'
    s.command = 'python "/mnt/hq/ML/examples/terrain_gen/usgs_data_preprocess/pdgtemp/18108/scripts/download_files0_1.py"'
    s.parentName = 'pythonhttpsverify0_3'
    s.staticAncestorNames = ['build_csv_filename0',]
    s.index = 0
    s.state = pdg.workItemState.CookedCancel
    s.type = pdg.workItemType.Regular
    context.addWorkItem(s)
    context.addWorkItemData('GenericData', 'download_files0_1', '[{},{},{"column_0":["https://prd-tnm.s3.amazonaws.com/StagedProducts/Elevation/13/GridFloat/USGS_NED_13_n46w115_GridFloat.zip"],"directory":["__PDG_DIR__/downloadlist"],"csv_filename":["/mnt/hq/ML/examples/terrain_gen/usgs_data_preprocess/CSV/downloadlist_0.csv"],"filename":["Rockies-small-FLT.txt"],"extension":[".txt"]}]', (), {})
    context.addWorkItemResults('download_files0_1', ['__PDG_DIR__/output/USGS_NED_13_n46w115_GridFloat.zip',],['file/archive',],[0,],[False,],[True,])
    s = pdg.WorkItem.Serialization()
    s.nodeName = 'pair_sketches_and_heightfields'
    s.name = 'pair_sketches_and_heightfields_dynamic_post_partition'
    s.baseName = 'pair_sketches_and_heightfields_dynamic_post_partition'
    s.frame = 0
    s.hasFrame = True
    s.isControl = True
    s.isNoGenerate = True
    s.state = pdg.workItemState.Waiting
    s.type = pdg.workItemType.DynamicPartition
    context.addWorkItem(s)
    s = pdg.WorkItem.Serialization()
    s.nodeName = 'fetch_terrain_tiles'
    s.name = 'fetch_terrain_tiles_static_wrapper0'
    s.baseName = 'fetch_terrain_tiles_static_wrapper0'
    s.staticAncestorNames = ['build_csv_filename0',]
    s.index = 0
    s.frame = 0
    s.hasFrame = True
    s.isControl = True
    s.state = pdg.workItemState.Waiting
    s.type = pdg.workItemType.StaticWrapper
    context.addWorkItem(s)
    s = pdg.WorkItem.Serialization()
    s.nodeName = 'TXT_to_CSV'
    s.name = 'TXT_to_CSV_static_wrapper0'
    s.baseName = 'TXT_to_CSV_static_wrapper0'
    s.staticAncestorNames = ['build_csv_filename0',]
    s.index = 0
    s.frame = 0
    s.hasFrame = True
    s.isControl = True
    s.state = pdg.workItemState.CookedSuccess
    s.type = pdg.workItemType.StaticWrapper
    context.addWorkItem(s)
    s = pdg.WorkItem.Serialization()
    s.nodeName = 'read_download_url'
    s.name = 'read_download_url0_3'
    s.baseName = 'read_download_url0'
    s.parentName = 'TXT_to_CSV0'
    s.staticAncestorNames = ['build_csv_filename0',]
    s.index = 0
    s.state = pdg.workItemState.CookedSuccess
    s.type = pdg.workItemType.Regular
    context.addWorkItem(s)
    context.addWorkItemData('GenericData', 'read_download_url0_3', '[{},{},{"column_0":["https://prd-tnm.s3.amazonaws.com/StagedProducts/Elevation/13/GridFloat/USGS_NED_13_n47w114_GridFloat.zip"],"directory":["__PDG_DIR__/downloadlist"],"csv_filename":["/mnt/hq/ML/examples/terrain_gen/usgs_data_preprocess/CSV/downloadlist_0.csv"],"filename":["Rockies-small-FLT.txt"],"extension":[".txt"]}]', (), {})
    s = pdg.WorkItem.Serialization()
    s.nodeName = 'pythonhttpsverify'
    s.name = 'pythonhttpsverify0_1'
    s.baseName = 'pythonhttpsverify0'
    s.parentName = 'read_download_url0_3'
    s.staticAncestorNames = ['build_csv_filename0',]
    s.environment = {'PYTHONHTTPSVERIFY':0,}
    s.index = 0
    s.isClearEnvironment = True
    s.isCloneResultData = True
    s.state = pdg.workItemState.CookedSuccess
    s.type = pdg.workItemType.Regular
    context.addWorkItem(s)
    context.addWorkItemData('GenericData', 'pythonhttpsverify0_1', '[{},{},{"column_0":["https://prd-tnm.s3.amazonaws.com/StagedProducts/Elevation/13/GridFloat/USGS_NED_13_n47w114_GridFloat.zip"],"directory":["__PDG_DIR__/downloadlist"],"csv_filename":["/mnt/hq/ML/examples/terrain_gen/usgs_data_preprocess/CSV/downloadlist_0.csv"],"filename":["Rockies-small-FLT.txt"],"extension":[".txt"]}]', (), {})
    s = pdg.WorkItem.Serialization()
    s.nodeName = 'download_files'
    s.name = 'download_files0_2'
    s.baseName = 'download_files0'
    s.command = 'python "/mnt/hq/ML/examples/terrain_gen/usgs_data_preprocess/pdgtemp/18108/scripts/download_files0_2.py"'
    s.parentName = 'pythonhttpsverify0_1'
    s.staticAncestorNames = ['build_csv_filename0',]
    s.index = 0
    s.state = pdg.workItemState.CookedCancel
    s.type = pdg.workItemType.Regular
    context.addWorkItem(s)
    context.addWorkItemData('GenericData', 'download_files0_2', '[{},{},{"column_0":["https://prd-tnm.s3.amazonaws.com/StagedProducts/Elevation/13/GridFloat/USGS_NED_13_n47w114_GridFloat.zip"],"directory":["__PDG_DIR__/downloadlist"],"csv_filename":["/mnt/hq/ML/examples/terrain_gen/usgs_data_preprocess/CSV/downloadlist_0.csv"],"filename":["Rockies-small-FLT.txt"],"extension":[".txt"]}]', (), {})
    context.addWorkItemResults('download_files0_2', ['__PDG_DIR__/output/USGS_NED_13_n47w114_GridFloat.zip',],['file/archive',],[0,],[False,],[True,])
    s = pdg.WorkItem.Serialization()
    s.nodeName = 'pair_sketches_and_heightfields'
    s.name = 'pair_sketches_and_heightfields_dynamic_pre_partition'
    s.baseName = 'pair_sketches_and_heightfields_dynamic_pre_partition'
    s.staticAncestorNames = ['build_csv_filename0',]
    s.frame = 0
    s.hasFrame = True
    s.isControl = True
    s.isNoGenerate = True
    s.state = pdg.workItemState.Waiting
    s.type = pdg.workItemType.StaticPartition
    context.addWorkItem(s)
    s = pdg.WorkItem.Serialization()
    s.nodeName = 'clean_up_attributes'
    s.name = 'clean_up_attributes_static_wrapper0'
    s.baseName = 'clean_up_attributes_static_wrapper0'
    s.staticAncestorNames = ['build_csv_filename0',]
    s.index = 0
    s.frame = 0
    s.hasFrame = True
    s.isControl = True
    s.state = pdg.workItemState.Waiting
    s.type = pdg.workItemType.StaticWrapper
    context.addWorkItem(s)
    s = pdg.WorkItem.Serialization()
    s.nodeName = 'read_download_url'
    s.name = 'read_download_url_static_wrapper0'
    s.baseName = 'read_download_url_static_wrapper0'
    s.staticAncestorNames = ['build_csv_filename0',]
    s.index = 0
    s.frame = 0
    s.hasFrame = True
    s.isControl = True
    s.state = pdg.workItemState.CookedSuccess
    s.type = pdg.workItemType.StaticWrapper
    context.addWorkItem(s)
    s = pdg.WorkItem.Serialization()
    s.nodeName = 'read_download_url'
    s.name = 'read_download_url0_1'
    s.baseName = 'read_download_url0'
    s.parentName = 'TXT_to_CSV0'
    s.staticAncestorNames = ['build_csv_filename0',]
    s.index = 0
    s.state = pdg.workItemState.CookedSuccess
    s.type = pdg.workItemType.Regular
    context.addWorkItem(s)
    context.addWorkItemData('GenericData', 'read_download_url0_1', '[{},{},{"column_0":["https://prd-tnm.s3.amazonaws.com/StagedProducts/Elevation/13/GridFloat/USGS_NED_13_n47w115_GridFloat.zip"],"directory":["__PDG_DIR__/downloadlist"],"csv_filename":["/mnt/hq/ML/examples/terrain_gen/usgs_data_preprocess/CSV/downloadlist_0.csv"],"filename":["Rockies-small-FLT.txt"],"extension":[".txt"]}]', (), {})
    s = pdg.WorkItem.Serialization()
    s.nodeName = 'pythonhttpsverify'
    s.name = 'pythonhttpsverify0'
    s.baseName = 'pythonhttpsverify0'
    s.parentName = 'read_download_url0_1'
    s.staticAncestorNames = ['build_csv_filename0',]
    s.environment = {'PYTHONHTTPSVERIFY':0,}
    s.index = 0
    s.isClearEnvironment = True
    s.isCloneResultData = True
    s.state = pdg.workItemState.CookedSuccess
    s.type = pdg.workItemType.Regular
    context.addWorkItem(s)
    context.addWorkItemData('GenericData', 'pythonhttpsverify0', '[{},{},{"column_0":["https://prd-tnm.s3.amazonaws.com/StagedProducts/Elevation/13/GridFloat/USGS_NED_13_n47w115_GridFloat.zip"],"directory":["__PDG_DIR__/downloadlist"],"csv_filename":["/mnt/hq/ML/examples/terrain_gen/usgs_data_preprocess/CSV/downloadlist_0.csv"],"filename":["Rockies-small-FLT.txt"],"extension":[".txt"]}]', (), {})
    s = pdg.WorkItem.Serialization()
    s.nodeName = 'download_files'
    s.name = 'download_files0_3'
    s.baseName = 'download_files0'
    s.command = 'python "/mnt/hq/ML/examples/terrain_gen/usgs_data_preprocess/pdgtemp/18108/scripts/download_files0_3.py"'
    s.parentName = 'pythonhttpsverify0'
    s.staticAncestorNames = ['build_csv_filename0',]
    s.index = 0
    s.state = pdg.workItemState.CookedCancel
    s.type = pdg.workItemType.Regular
    context.addWorkItem(s)
    context.addWorkItemData('GenericData', 'download_files0_3', '[{},{},{"column_0":["https://prd-tnm.s3.amazonaws.com/StagedProducts/Elevation/13/GridFloat/USGS_NED_13_n47w115_GridFloat.zip"],"directory":["__PDG_DIR__/downloadlist"],"csv_filename":["/mnt/hq/ML/examples/terrain_gen/usgs_data_preprocess/CSV/downloadlist_0.csv"],"filename":["Rockies-small-FLT.txt"],"extension":[".txt"]}]', (), {})
    context.addWorkItemResults('download_files0_3', ['__PDG_DIR__/output/USGS_NED_13_n47w115_GridFloat.zip',],['file/archive',],[0,],[False,],[True,])
    s = pdg.WorkItem.Serialization()
    s.nodeName = 'create_peak_and_valley_export_path'
    s.name = 'create_peak_and_valley_export_path_static_wrapper0'
    s.baseName = 'create_peak_and_valley_export_path_static_wrapper0'
    s.staticAncestorNames = ['build_csv_filename0',]
    s.index = 0
    s.frame = 0
    s.hasFrame = True
    s.isControl = True
    s.state = pdg.workItemState.Waiting
    s.type = pdg.workItemType.StaticWrapper
    context.addWorkItem(s)
    s = pdg.WorkItem.Serialization()
    s.nodeName = 'pythonhttpsverify'
    s.name = 'pythonhttpsverify_static_wrapper0'
    s.baseName = 'pythonhttpsverify_static_wrapper0'
    s.staticAncestorNames = ['build_csv_filename0',]
    s.index = 0
    s.frame = 0
    s.hasFrame = True
    s.isControl = True
    s.state = pdg.workItemState.CookedSuccess
    s.type = pdg.workItemType.StaticWrapper
    context.addWorkItem(s)
    s = pdg.WorkItem.Serialization()
    s.nodeName = 'create_peak_and_valley_masks'
    s.name = 'create_peak_and_valley_masks_static_wrapper0'
    s.baseName = 'create_peak_and_valley_masks_static_wrapper0'
    s.staticAncestorNames = ['build_csv_filename0',]
    s.index = 0
    s.frame = 0
    s.hasFrame = True
    s.isControl = True
    s.state = pdg.workItemState.Waiting
    s.type = pdg.workItemType.StaticWrapper
    context.addWorkItem(s)
    s = pdg.WorkItem.Serialization()
    s.nodeName = 'download_files'
    s.name = 'download_files_static_wrapper0'
    s.baseName = 'download_files_static_wrapper0'
    s.staticAncestorNames = ['build_csv_filename0',]
    s.index = 0
    s.frame = 0
    s.hasFrame = True
    s.isControl = True
    s.state = pdg.workItemState.Waiting
    s.type = pdg.workItemType.StaticWrapper
    context.addWorkItem(s)
    s = pdg.WorkItem.Serialization()
    s.nodeName = 'resample_to_20m_spacing'
    s.name = 'resample_to_20m_spacing_static_wrapper0'
    s.baseName = 'resample_to_20m_spacing_static_wrapper0'
    s.staticAncestorNames = ['build_csv_filename0',]
    s.index = 0
    s.frame = 0
    s.hasFrame = True
    s.isControl = True
    s.state = pdg.workItemState.Waiting
    s.type = pdg.workItemType.StaticWrapper
    context.addWorkItem(s)
    s = pdg.WorkItem.Serialization()
    s.nodeName = 'create_source_filename_attribute'
    s.name = 'create_source_filename_attribute_static_wrapper0'
    s.baseName = 'create_source_filename_attribute_static_wrapper0'
    s.staticAncestorNames = ['build_csv_filename0',]
    s.index = 0
    s.frame = 0
    s.hasFrame = True
    s.isControl = True
    s.state = pdg.workItemState.Waiting
    s.type = pdg.workItemType.StaticWrapper
    context.addWorkItem(s)
    s = pdg.WorkItem.Serialization()
    s.nodeName = 'validate_tile_by_height_and_coverage'
    s.name = 'validate_tile_by_height_and_coverage_static_wrapper0'
    s.baseName = 'validate_tile_by_height_and_coverage_static_wrapper0'
    s.staticAncestorNames = ['build_csv_filename0',]
    s.index = 0
    s.frame = 0
    s.hasFrame = True
    s.isControl = True
    s.state = pdg.workItemState.Waiting
    s.type = pdg.workItemType.StaticWrapper
    context.addWorkItem(s)
    s = pdg.WorkItem.Serialization()
    s.nodeName = 'decompress_downloaded_files'
    s.name = 'decompress_downloaded_files_static_wrapper0'
    s.baseName = 'decompress_downloaded_files_static_wrapper0'
    s.staticAncestorNames = ['build_csv_filename0',]
    s.index = 0
    s.frame = 0
    s.hasFrame = True
    s.isControl = True
    s.state = pdg.workItemState.Waiting
    s.type = pdg.workItemType.StaticWrapper
    context.addWorkItem(s)
    s = pdg.WorkItem.Serialization()
    s.nodeName = 'import_validation_attributes'
    s.name = 'import_validation_attributes_static_wrapper0'
    s.baseName = 'import_validation_attributes_static_wrapper0'
    s.staticAncestorNames = ['build_csv_filename0',]
    s.index = 0
    s.frame = 0
    s.hasFrame = True
    s.isControl = True
    s.state = pdg.workItemState.Waiting
    s.type = pdg.workItemType.StaticWrapper
    context.addWorkItem(s)
    s = pdg.WorkItem.Serialization()
    s.nodeName = 'fetch_extracted_HGT_files'
    s.name = 'fetch_extracted_HGT_files_static_wrapper0'
    s.baseName = 'fetch_extracted_HGT_files_static_wrapper0'
    s.staticAncestorNames = ['build_csv_filename0',]
    s.index = 0
    s.frame = 0
    s.hasFrame = True
    s.isControl = True
    s.state = pdg.workItemState.Waiting
    s.type = pdg.workItemType.StaticWrapper
    context.addWorkItem(s)
    s = pdg.WorkItem.Serialization()
    s.nodeName = 'valid_tiles'
    s.name = 'valid_tiles_static_wrapper0'
    s.baseName = 'valid_tiles_static_wrapper0'
    s.staticAncestorNames = ['build_csv_filename0',]
    s.index = 0
    s.frame = 0
    s.hasFrame = True
    s.isControl = True
    s.state = pdg.workItemState.Waiting
    s.type = pdg.workItemType.StaticWrapper
    context.addWorkItem(s)
    s = pdg.WorkItem.Serialization()
    s.nodeName = 'fetch_extracted_FLT_files'
    s.name = 'fetch_extracted_FLT_files_static_wrapper0'
    s.baseName = 'fetch_extracted_FLT_files_static_wrapper0'
    s.staticAncestorNames = ['build_csv_filename0',]
    s.index = 0
    s.frame = 0
    s.hasFrame = True
    s.isControl = True
    s.state = pdg.workItemState.Waiting
    s.type = pdg.workItemType.StaticWrapper
    context.addWorkItem(s)
    s = pdg.WorkItem.Serialization()
    s.nodeName = 'create_sketch_export_filepath'
    s.name = 'create_sketch_export_filepath_static_wrapper0'
    s.baseName = 'create_sketch_export_filepath_static_wrapper0'
    s.staticAncestorNames = ['build_csv_filename0',]
    s.index = 0
    s.frame = 0
    s.hasFrame = True
    s.isControl = True
    s.state = pdg.workItemState.Waiting
    s.type = pdg.workItemType.StaticWrapper
    context.addWorkItem(s)
    s = pdg.WorkItem.Serialization()
    s.nodeName = 'merge_all_file_types'
    s.name = 'merge_all_file_types_static_wrapper0'
    s.baseName = 'merge_all_file_types_static_wrapper0'
    s.staticAncestorNames = ['build_csv_filename0',]
    s.index = 0
    s.frame = 0
    s.hasFrame = True
    s.isControl = True
    s.state = pdg.workItemState.Waiting
    s.type = pdg.workItemType.StaticWrapper
    context.addWorkItem(s)
    s = pdg.WorkItem.Serialization()
    s.nodeName = 'export_sketches'
    s.name = 'export_sketches_static_wrapper0'
    s.baseName = 'export_sketches_static_wrapper0'
    s.staticAncestorNames = ['build_csv_filename0',]
    s.index = 0
    s.frame = 0
    s.hasFrame = True
    s.isControl = True
    s.state = pdg.workItemState.Waiting
    s.type = pdg.workItemType.StaticWrapper
    context.addWorkItem(s)
    s = pdg.WorkItem.Serialization()
    s.nodeName = 'create_imported_filepath'
    s.name = 'create_imported_filepath_static_wrapper0'
    s.baseName = 'create_imported_filepath_static_wrapper0'
    s.staticAncestorNames = ['build_csv_filename0',]
    s.index = 0
    s.frame = 0
    s.hasFrame = True
    s.isControl = True
    s.state = pdg.workItemState.Waiting
    s.type = pdg.workItemType.StaticWrapper
    context.addWorkItem(s)
    context.addWorkItemDependency('create_height_export_filepath_static_wrapper0','valid_tiles_static_wrapper0',False)
    context.addWorkItemDependency('import_terrain_file_static_wrapper0','create_imported_filepath_static_wrapper0',False)
    context.addWorkItemDependency('export_heightfields_static_wrapper0','create_height_export_filepath_static_wrapper0',False)
    context.addWorkItemDependency('split_terrain_to_tiles_static_wrapper0','import_terrain_file_static_wrapper0',False)
    context.addWorkItemDependency('build_csv_filename0','fetch_download_list0',True)
    context.addWorkItemDependency('pair_sketches_and_heightfields_dynamic_post_partition','pair_sketches_and_heightfields_dynamic_pre_partition',False)
    context.addWorkItemDependency('fetch_terrain_tiles_static_wrapper0','split_terrain_to_tiles_static_wrapper0',False)
    context.addWorkItemDependency('TXT_to_CSV_static_wrapper0','TXT_to_CSV0',False)
    context.addWorkItemDependency('TXT_to_CSV_static_wrapper0','build_csv_filename0',False)
    context.addWorkItemDependency('pair_sketches_and_heightfields_dynamic_pre_partition','create_sketch_export_filepath_static_wrapper0',False)
    context.addWorkItemDependency('pair_sketches_and_heightfields_dynamic_pre_partition','create_height_export_filepath_static_wrapper0',False)
    context.addWorkItemDependency('clean_up_attributes_static_wrapper0','fetch_terrain_tiles_static_wrapper0',False)
    context.addWorkItemDependency('read_download_url_static_wrapper0','TXT_to_CSV_static_wrapper0',False)
    context.addWorkItemDependency('read_download_url_static_wrapper0','read_download_url0',False)
    context.addWorkItemDependency('read_download_url_static_wrapper0','read_download_url0_2',False)
    context.addWorkItemDependency('read_download_url_static_wrapper0','read_download_url0_1',False)
    context.addWorkItemDependency('read_download_url_static_wrapper0','read_download_url0_3',False)
    context.addWorkItemDependency('create_peak_and_valley_export_path_static_wrapper0','clean_up_attributes_static_wrapper0',False)
    context.addWorkItemDependency('pythonhttpsverify_static_wrapper0','read_download_url_static_wrapper0',False)
    context.addWorkItemDependency('pythonhttpsverify_static_wrapper0','pythonhttpsverify0_1',False)
    context.addWorkItemDependency('pythonhttpsverify_static_wrapper0','pythonhttpsverify0',False)
    context.addWorkItemDependency('pythonhttpsverify_static_wrapper0','pythonhttpsverify0_2',False)
    context.addWorkItemDependency('pythonhttpsverify_static_wrapper0','pythonhttpsverify0_3',False)
    context.addWorkItemDependency('create_peak_and_valley_masks_static_wrapper0','create_peak_and_valley_export_path_static_wrapper0',False)
    context.addWorkItemDependency('download_files_static_wrapper0','download_files0_3',False)
    context.addWorkItemDependency('download_files_static_wrapper0','download_files0_2',False)
    context.addWorkItemDependency('download_files_static_wrapper0','download_files0_1',False)
    context.addWorkItemDependency('download_files_static_wrapper0','pythonhttpsverify_static_wrapper0',False)
    context.addWorkItemDependency('download_files_static_wrapper0','download_files0',False)
    context.addWorkItemDependency('resample_to_20m_spacing_static_wrapper0','create_peak_and_valley_masks_static_wrapper0',False)
    context.addWorkItemDependency('create_source_filename_attribute_static_wrapper0','download_files_static_wrapper0',False)
    context.addWorkItemDependency('validate_tile_by_height_and_coverage_static_wrapper0','resample_to_20m_spacing_static_wrapper0',False)
    context.addWorkItemDependency('decompress_downloaded_files_static_wrapper0','create_source_filename_attribute_static_wrapper0',False)
    context.addWorkItemDependency('import_validation_attributes_static_wrapper0','validate_tile_by_height_and_coverage_static_wrapper0',False)
    context.addWorkItemDependency('fetch_extracted_HGT_files_static_wrapper0','decompress_downloaded_files_static_wrapper0',False)
    context.addWorkItemDependency('valid_tiles_static_wrapper0','import_validation_attributes_static_wrapper0',False)
    context.addWorkItemDependency('fetch_extracted_FLT_files_static_wrapper0','decompress_downloaded_files_static_wrapper0',False)
    context.addWorkItemDependency('create_sketch_export_filepath_static_wrapper0','valid_tiles_static_wrapper0',False)
    context.addWorkItemDependency('merge_all_file_types_static_wrapper0','fetch_extracted_HGT_files_static_wrapper0',False)
    context.addWorkItemDependency('merge_all_file_types_static_wrapper0','fetch_extracted_FLT_files_static_wrapper0',False)
    context.addWorkItemDependency('export_sketches_static_wrapper0','create_sketch_export_filepath_static_wrapper0',False)
    context.addWorkItemDependency('create_imported_filepath_static_wrapper0','merge_all_file_types_static_wrapper0',False)
    context.commitWorkItem('pythonhttpsverify0_3')
    context.commitWorkItem('create_height_export_filepath_static_wrapper0')
    context.commitWorkItem('import_terrain_file_static_wrapper0')
    context.commitWorkItem('fetch_download_list0')
    context.commitWorkItem('download_files0')
    context.commitWorkItem('export_heightfields_static_wrapper0')
    context.commitWorkItem('split_terrain_to_tiles_static_wrapper0')
    context.commitWorkItem('build_csv_filename0')
    context.commitWorkItem('download_files0_1')
    context.commitWorkItem('pair_sketches_and_heightfields_dynamic_post_partition')
    context.commitWorkItem('fetch_terrain_tiles_static_wrapper0')
    context.commitWorkItem('TXT_to_CSV_static_wrapper0')
    context.commitWorkItem('download_files0_2')
    context.commitWorkItem('pair_sketches_and_heightfields_dynamic_pre_partition')
    context.commitWorkItem('clean_up_attributes_static_wrapper0')
    context.commitWorkItem('read_download_url_static_wrapper0')
    context.commitWorkItem('download_files0_3')
    context.commitWorkItem('TXT_to_CSV0')
    context.commitWorkItem('create_peak_and_valley_export_path_static_wrapper0')
    context.commitWorkItem('pythonhttpsverify_static_wrapper0')
    context.commitWorkItem('read_download_url0')
    context.commitWorkItem('create_peak_and_valley_masks_static_wrapper0')
    context.commitWorkItem('download_files_static_wrapper0')
    context.commitWorkItem('read_download_url0_1')
    context.commitWorkItem('resample_to_20m_spacing_static_wrapper0')
    context.commitWorkItem('create_source_filename_attribute_static_wrapper0')
    context.commitWorkItem('read_download_url0_2')
    context.commitWorkItem('validate_tile_by_height_and_coverage_static_wrapper0')
    context.commitWorkItem('decompress_downloaded_files_static_wrapper0')
    context.commitWorkItem('read_download_url0_3')
    context.commitWorkItem('import_validation_attributes_static_wrapper0')
    context.commitWorkItem('fetch_extracted_HGT_files_static_wrapper0')
    context.commitWorkItem('pythonhttpsverify0')
    context.commitWorkItem('valid_tiles_static_wrapper0')
    context.commitWorkItem('fetch_extracted_FLT_files_static_wrapper0')
    context.commitWorkItem('pythonhttpsverify0_1')
    context.commitWorkItem('create_sketch_export_filepath_static_wrapper0')
    context.commitWorkItem('merge_all_file_types_static_wrapper0')
    context.commitWorkItem('pythonhttpsverify0_2')
    context.commitWorkItem('export_sketches_static_wrapper0')
    context.commitWorkItem('create_imported_filepath_static_wrapper0')
