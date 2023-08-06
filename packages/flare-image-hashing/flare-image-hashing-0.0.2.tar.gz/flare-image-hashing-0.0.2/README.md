# image-hashing

# facial-extractor

PyPi: [flare-image-hashing](https://test.pypi.org/project/flare-image-hashing/)

## API
* `hash_image`
  * Average Hash computation of the given image.
  * Parameters
    * `image_path` - A string specifying where the image in located.
  * Return:
    * An imagehash `ImageHash` object on success. `None` otherwise.

* `image_difference`
  * Checks if the Average Hash of two images is equal.
    Here the definition of equal is using computed hashes and not raw pixel values.
    Meaning two different images could be 'equal'.
  * Parameters
    * `reference_image_path` - A string specifying where the first image in located.
    * `other_time_path` - A string specifying where the second image in located.
  * Return:
    * True if equal. False otherwise.

## Publishing the package
1. Install packages in `requirements.txt`
2. Bump the version number in [setup.cfg](/setup.cfg)
3. Building (Now run this command from the same directory where pyproject.toml is located): 
   `python3 -m build`
4. Get the PyPI API token
5. Run Twine to upload all the archives under `dist`: 
   `python3 -m twine upload dist/*`
  1. username: `__token__`
  2. password: the PyPi token  including the `pypi-` prefix

## Helpful links 
* [Instructions](https://packaging.python.org/en/latest/tutorials/packaging-projects/)