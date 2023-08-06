import scanpy as sc

import normalize

ad = sc.datasets.visium_sge('V1_Breast_Cancer_Block_A_Section_1')

ad_norm = normalize.normalize_Dino(ad)

print(ad_norm)
print(ad_norm.X)
