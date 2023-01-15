from PIL import Image
from io import BytesIO

class Message:
    def __init__(self, message, photo):
        self.message = message
        self.photo = photo

    def get_message_information(self):
        return self.message
    
    def get_message(self):
        return self.message.message

    def get_photo(self):
        return self.photo

    # def convert_photo(self):
        # image = Image.open(BytesIO(self.photo.sizes[0].bytes))
        # image.save('result.png')
        # image.show()
        # string = BytesIO(self.photo.file_reference)
        # string1 = BytesIO(self.photo.sizes[0].bytes)
        # print(string.decode("utf-8"))
        # print(string1.decode("utf-8"))
        

    

    
