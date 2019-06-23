
class Reader:
    def read(self, file_name: str) -> str:
        handle = open(file_name)

        return handle.read()

