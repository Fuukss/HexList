class HexList(list):
    def __getitem__(self, index):
        value = super().__getitem__(index)
        return hex(value)