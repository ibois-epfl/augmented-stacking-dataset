<h1 align="center">Stone dataset for augmented-stacking</h1>

<p align="center">
    <img src="https://user-images.githubusercontent.com/50238678/173020102-c50f7609-2276-4d5a-8ca2-f5791145dc32.gif" width="400">
</p>
<br/>

<div align = "center">
    <a>
        <img src = "./img/ibosiTraspBlack.png" height="30"/>
    </a>
    <a>
        <img src = "./img/50x50-00000000.png" height="20"/>
    </a>
    <a>
        <img src = "./img/eesd_logo_black.png" height="30"/>
    </a>
    <a>
        <img src = "./img/50x50-00000000.png" height="20"/>
    </a>
    <a>
        <img src = "./img/logoEPFLblack.png" height="30"/>
    </a>
</div>

<br />



Dataset of stone files for [augmented stacking project](https://github.com/ibois-epfl/augmented-stacking).
Stones are stored in .ply in both mesh and point cloud format.
For more info contact [andrea.settimi@epfl.ch](andrea.settimi@epfl.ch)

Structure of the repo:
```bash
.
├── img
│   ├── *.png
├── README.md
├── stones
│   ├── mesh_high_res
│   │   ├── remeshed_high_res_A0.ply
│   │   ├── remeshed_high_res_A10.ply
│   │   ├── ...
│   │   └── remeshed_high_res_E56.ply
│   └── pcd_high_res
│       ├── pcd_high_res_A0.ply
│       ├── pcd_high_res_A10.ply
│       ├── ...
│       └── pcd_high_res_E56.ply
└── util
    └── *.py
```

