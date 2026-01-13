class BinaryStream:
    index = 0

    def __init__(self, **kwargs):
        if "path" in kwargs:
            # Read binary
            with open(kwargs["path"], "rb") as file:
                self.data = file.read()
        elif "binary" in kwargs:
            self.data = kwargs["binary"]

    def __len__(self) -> int:
        return len(self.data)

    def __call__(self, chunk_length):
        output = self.data[self.index : self.index + chunk_length]
        self.index += chunk_length

        return output

    def __bool__(self):
        return self.index < len(self.data)
