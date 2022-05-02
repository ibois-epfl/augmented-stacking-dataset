
'''
Author: Andrea Settimi (andrea.settimi@epfl.ch), 2022
The script allows batch convert a PCD file to a mesh file.
'''


import os
import sys
import rhinoscriptsyntax as rs


IN_PCD_DIR = r"C:\augmented-stacking-dataset\util\test_folder_in"  # replace with clouds dir
OUT_MESH_DIR = r"C:\augmented-stacking-dataset\util\test_folder_out"  # replace with out dir


def main():
    print("POP")
    
    # Get all pcd file paths
    pcds = []
    pcd_names = []
    for file in os.listdir(IN_PCD_DIR):
        if file.endswith(".ply"):
            pcd_file = os.path.join(IN_PCD_DIR, file)
            pcds.append(pcd_file)
            pcd_names.append(pcd_file.split('_')[-1].split('.')[0])
    
    # Get pcd, scale to m, mesh and export
    rs.EnableRedraw(True)
    for i in range(len(pcds)):
        filepath = pcds[i]
        rs.Command("!_-Import \"" + filepath + "\" -Enter -Enter")
        rs.Command("_SelectAll")
        rs.Command("_Cockroach_MeshPoisson" + " -Enter -Enter -Enter !")

        rs.UnselectAllObjects()
        filename = "remeshed_high_res_" + pcd_names[i] + '.ply'
        filepath = os.path.join(OUT_MESH_DIR, filename)

        rs.Command("_-SelMesh")  # mm to m
        rs.Command("_-Scale 0 1000")

        rs.Command('! _-Export "{}" _Enter _Enter'.format(filepath), True)
        
        rs.UnselectAllObjects()
        rs.Command("-SelAll")
        rs.Command("-Delete")

if __name__ == "__main__":
    main()