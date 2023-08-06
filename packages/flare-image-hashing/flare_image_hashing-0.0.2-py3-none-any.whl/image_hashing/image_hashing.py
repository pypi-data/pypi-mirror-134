from typing import Union
from PIL import Image as img
from PIL.Image import Image
import imagehash
from imagehash import ImageHash


def __load_image(image_path: str) -> Union[Image, None]:
    """
    Opens and identifies the given image file.

    :param image_path: A string specifying where the image in located
    :return: PIL.Image on success. None otherwise.
    """
    try:
        return img.open(image_path)
    except FileNotFoundError as exception:
        print("Exception: {}".format(type(exception).__name__))
        print("Exception message: {}".format(exception))
        return None


def hash_image(image_path: str) -> Union[ImageHash, None]:
    """
    Average Hash computation of the given image.

    :param image_path: A string specifying where the image in located.
    :return: An imagehash `ImageHash` object on success. None otherwise.
    """
    image = __load_image(image_path)

    if not image:
        return None

    return imagehash.average_hash(image)


def image_difference(reference_image_path: str, other_time_path: str) -> int:
    """
    Calculates the Average Hash difference between the two provided images.

    :param reference_image_path: A string specifying where the first image in located.
    :param other_time_path: A string specifying where the second image in located.
    :return: A non-negative integer on success. -1 on failure.
    """
    reference_image_hash = hash_image(reference_image_path)
    other_image_hash = hash_image(other_time_path)

    if reference_image_hash is None or other_image_hash is None:
        return -1

    return abs(reference_image_hash - other_image_hash)


def equal_images(reference_image_path: str, other_time_path: str) -> bool:
    """
    Checks if the Average Hash of two images is equal.
    Here the definition of equal is using computed hashes and not raw pixel values.
    Meaning two different images could be 'equal'.

    :param reference_image_path: A string specifying where the first image in located.
    :param other_time_path: A string specifying where the second image in located.
    :return: True if equal. False otherwise.
    """
    return image_difference(reference_image_path, other_time_path) == 0
