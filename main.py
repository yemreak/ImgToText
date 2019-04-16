from utils import path, file
from word import Word

IMAGE_PATH = path.get_file_path("test1.jpg", "in", "test")

word = Word.read_from_img(IMAGE_PATH)
img = word.print_to_img()
file.save_file(img, file_name='test1.jpg', data_attr='test')
print(img)
# img = io.print_to_img(text)
