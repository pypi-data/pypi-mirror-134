from main import FeatureExtractionTool

# fet = FeatureExtractionTool("./src/MSA_FET/example_configs/opensmile+vggface.json")
# feature = fet.run_single("./src/MSA_FET/test_files/0001.mp4", "./tmp/feature.pkl")
# print(feature)

fet = FeatureExtractionTool("./example_configs/wav2vec.json",
                            dataset_root_dir="/home/sharing/disk3/Datasets/MMSA-Standard")
feature = fet.run_dataset('MOSI', out_file="./feature.pkl")
