import os

for split in ["train", "valid", "test"]:
    print(f"Processing {split}...")
    os.system(f"python preprocessing/gsm_icot.py {split}")
    os.remove(f"data/gsm_{split}.txt")
