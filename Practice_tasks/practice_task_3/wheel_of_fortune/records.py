import os


class Records:
    def __init__(self):
        self.__path = "\\".join(__file__.split("\\")[:-1] + ["records.txt"])
        if not os.path.exists(self.__path):
            open(self.__path, mode="w").close()

    def add_new_record(self, name: str, record: int):
        with open(self.__path, mode="a") as file:
            file.write(f"{name} - {record}\n")

    def read_records(self) -> list[str]:
        with open(self.__path, mode="r") as file:
            data = file.read()
            return list(filter(lambda x: len(x) != 0, data.split("\n")))

    def read_records_sorted(self) -> list[str]:
        records = self.read_records()
        return sorted(records, key=lambda x: int(x.split(" - ")[1]), reverse=True)

    def __str__(self):
        rating = self.read_records_sorted()
        return ("-" * 15 + "Таблица лидеров" + "-" * 15 + "\n" +
                (" " * 16 + "Таблица пуста" + " " * 16 if len(rating) == 0 else
                 "\n".join([(("🥇", "🥈", "🥉")[i] if i < 3 else f"{i + 1}") + f" {e}" for i, e in enumerate(rating)])))