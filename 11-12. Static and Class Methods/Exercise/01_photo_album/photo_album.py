class PhotoAlbum:
    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count: int):
        pages = (photos_count + 3) // 4
        return cls(pages)

    def add_photo(self, label: str):
        for i, page in enumerate(self.photos, start=1):
            if len(page) < 4:
                page.append(label)
                slot_number = len(page)
                return f"{label} photo added successfully on page {i} slot {slot_number}"
        return "No more free slots"

    def display(self):
        result = ""
        for page in self.photos:
            result += f"-----------\n" + ' '.join(["[]" for _ in range(len(page))]) + '\n'
        result += "-----------"
        return result
