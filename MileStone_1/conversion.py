import pandas as pd

col_names = ["engine_id", "cycle", "op_setting_1", "op_setting_2", "op_setting_3"] \
            + [f"s{i}" for i in range(1, 22)]

train = pd.read_csv(r"C:\infosys_project\archive (3)\CMaps\train_FD001.txt", sep=r"\s+", header=None, names=col_names)
train.to_csv(r"C:\infosys_project\archive (3)\CMaps\train_FD001.csv", index=False)

test = pd.read_csv(r"C:\infosys_project\archive (3)\CMaps\test_FD001.txt", sep=r"\s+", header=None, names=col_names)
test.to_csv(r"C:\infosys_project\archive (3)\CMaps\test_FD001.csv", index=False)

rul = pd.read_csv(r"C:\infosys_project\archive (3)\CMaps\RUL_FD001.txt", header=None, names=["RUL"])
rul.to_csv(r"C:\infosys_project\archive (3)\CMaps\RUL_FD001.csv", index=False)
