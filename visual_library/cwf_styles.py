
from matplotlib.colors import LinearSegmentedColormap


COLOR_SCALE_RED_TO_GREEN = [
    "#E58663",
    "#E8B86F",
    "#EBE275",
    "#A8D266",
    "#70B565",
    "#46966E",
    "#38796E",
]

COLOR_SCALE_GREENS = [
    "#C6EB84",
    "#A8D166",
    "#A8D266",
    "#70B565",
    "#46966E",
    "#1C3D37"
]


COLOR_SCALE_HEATMAP = [
    "#D8ECE2",
    "#234B37",
]

COLOR_SCALE_REDS = [
    "#E37750",
    "#E7AB52",
    "#ECE162",
]

CWF_CMAP = LinearSegmentedColormap.from_list("CWF", COLOR_SCALE_GREENS, N=100)
