#%%
from train.src.train import jcell_train
from evaluation.run import jcell_eval
from dataset_utils.proc2d.inst2sem import inst2sem as inst2sem2D
from dataset_utils.proc3d.inst2sem import inst2sem as inst2sem3D

import imageio

import matplotlib.pyplot as plt

#%%
model = jcell_train(
    experiment="new",
    dataset="tcells",
    use_gpu=[1],
    optimizer_param={"lr": 0.0001},
    epochs=1,
)

# %%
image = imageio.imread(
    "/media/fillo/_home/work/caltech/400_test/image1_3_4_image.png"
)
plt.matshow(image)

#%%
results = jcell_eval(
    input=image,
    model="generalist",
    use_gpu=1,
    crop_size=512,
    confidence=0.90,
    adaptive_area_filter=True,
)
#%%

plt.imshow(image)
plt.show()
for im in results:
    if im.ndim > 2:
        plt.imshow(im[:, :, :3])
    else:
        plt.matshow(im)

# %%
inst = imageio.imread("/home/fillo/.jcell/output/image_instances.tif")
plt.matshow(inst)

L = inst2sem2D(inst, se1_radius=1, se2_radius=7)
plt.matshow(L)
# %%
