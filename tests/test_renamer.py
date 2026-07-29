import unittest

from renamer.patterns import apply_pattern


class TestRenamer(unittest.TestCase):

    def test_prefix(self):
        result = apply_pattern("image.jpg", prefix="IMG_")
        self.assertEqual(result, "IMG_image.jpg")

    def test_suffix(self):
        result = apply_pattern("photo.png", suffix="_backup")
        self.assertEqual(result, "photo_backup.png")


if __name__ == "__main__":
    unittest.main()
