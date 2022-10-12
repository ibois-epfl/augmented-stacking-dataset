
'''
Author: Andrea Settimi (andrea.settimi@epfl.ch), 2022
The script quickly checks the oreinted bounding box for each point cloud and calculate the diameter.
This data is used to give an overahul idea of the stone sizes distribution of the dataset.
'''

import os

import numpy as np
from tqdm import tqdm

import git
import open3d as o3d

import matplotlib.pyplot as plt


repo = git.Repo('.', search_parent_directories=True)
STONES_PCD_DIR = os.path.join(repo.working_dir, "stones/pcd_high_res")
PCD_PATHS = [os.path.join(STONES_PCD_DIR, f) for f in os.listdir(STONES_PCD_DIR) if f.endswith(".ply")]
LBL = [(f.split(".")[0]).split("_")[-1] for f in os.listdir(STONES_PCD_DIR) if f.endswith(".ply")]
GRAPH_OUT_DIR = os.path.join(repo.working_dir, "graphs")

def main() -> int:

    o3d_pcd = [o3d.io.read_point_cloud(path) for path in PCD_PATHS]
    print(f"Number of pcd: {len(o3d_pcd)}")

    obbox = []
    diagonals = []

    for idx, pcd in enumerate(o3d_pcd):
        pcd_volume = pcd.get_axis_aligned_bounding_box().volume()

    for idx, pcd in enumerate(o3d_pcd):
        obbox.append(pcd.get_oriented_bounding_box())

    for idx, ob in enumerate(obbox):
        obbox_pts = ob.get_box_points()
        diagonals.append(np.linalg.norm(obbox_pts[0] - obbox_pts[6]))

    diagonals = sorted(diagonals)

    diagonals_labeled = zip(diagonals, LBL)

    plt.scatter(range(len(diagonals)), diagonals, c=diagonals, cmap='viridis')
    plt.ylabel("OrientedBoundingBox diagonal length [m]")
    plt.xlabel("Stones")
    plt.xticks([])
    # plt.show()

    plt.savefig(os.path.join(GRAPH_OUT_DIR,"stones_diagonal_length.png"))

    # >>>>>>>>>>>>>> PRINT OUT >>>>>>>>>>>>>>
    for l in diagonals_labeled:
        print(f"{l[1]}: {l[0]}")
    # <<<<<<<<<<<<<< PRINT OUT <<<<<<<<<<<<<<

    return 0


if __name__ == "__main__":
    main()