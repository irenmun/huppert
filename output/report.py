class Report:

    def save(

        self,

        renamed,

        filename

    ):

        with open(

            filename,

            "w",

            encoding="utf-8"

        ) as file:

            file.write(

                "Rename Report\n\n"

            )

            for old, new in renamed:

                file.write(

                    f"{old} -> {new}\n"

                )

            file.write("\n")

            file.write(

                f"Files processed: {len(renamed)}"

            )
