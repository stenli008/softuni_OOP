from math import ceil


class PhotoAlbum:
	PHOTOS_PER_PAGE = 4

	def __init__(self, pages):
		self.pages = pages
		self.photos = self.__make_album_pages()

	@classmethod
	def from_photos_count(cls, photos_count: int):
		pages = ceil(photos_count / PhotoAlbum.PHOTOS_PER_PAGE)
		return cls(pages)

	def __make_album_pages(self):
		result = []
		for page in range(self.pages):
			result.append([] * self.PHOTOS_PER_PAGE)
		return result

	def add_photo(self, label: str):
		free_spaces = False
		for page in self.photos:
			if len(page) < self.PHOTOS_PER_PAGE:
				free_spaces = True
				break
		if free_spaces:
			for page in range(len(self.photos)):
				if len(self.photos[page]) < self.PHOTOS_PER_PAGE:
					self.photos[page].append(label)
					return f'{label} photo added successfully on page {page+1} slot {len(self.photos[page])}'
		return 'No more free slots'

	def display(self):
		result = f'-----------\n'
		for page in self.photos:
			result += f'{(len(page) * "[] ").strip()}\n-----------\n'
		return result.strip()



album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())
