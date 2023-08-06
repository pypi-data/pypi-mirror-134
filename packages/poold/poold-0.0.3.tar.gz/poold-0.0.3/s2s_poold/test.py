from dataset import S2SDataset

targets = [1, 2, 3]
models = ["doy", "cfsv2"]
s2s_data = S2SDataset(targets, models, gt_id="contest_precip", horizon="34w")
