import os

class Formatter:

    def build(

        self,

        prefix,

        number,

        filename

    ):

        extension = os.path.splitext(

            filename

        )[1]

        return f"{prefix}_{number:03d}{extension}"
