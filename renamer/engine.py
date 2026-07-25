from helpers.counters import Counter

class RenameEngine:

    def rename(

        self,

        files,

        prefix,

        start,

        formatter

    ):

        counter = Counter(start)

        result = []

        for file in files:

            result.append(

                (

                    file,

                    formatter.build(

                        prefix,

                        counter.next(),

                        file

                    )

                )

            )

        return result
