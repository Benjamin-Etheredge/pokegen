from torchvision import transforms
import pathlib
from PIL import Image


def display(tensor):
    im = transforms.ToPILImage()(tensor)
    im.show()


def save(tensor, path):
    im = transforms.ToPILImage()(tensor)
    im.save(path)


def make_gif(path):
    path = pathlib.Path(path)
    ims = [Image.open(file) for file in path.iterdir()]
    ims[0].save(path, 
        save_all=True,
        append_images=ims[1:], 
        optimize=False,
        duration=30,
        loops=0)
