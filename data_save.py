from glob import glob
import face_recognition
from db import access_db

client, db, col, error_col = access_db()

path = 'test_img\\'
extension = '.jpg'
for i in glob(path + '*' + extension):
  filename = i.replace(path, '')
  name = filename.replace(extension, '')
  name = filename.replace(extension, '')
  try:
    id = face_recognition.face_encodings(face_recognition.load_image_file(i), model='large')[0]
    data = {'name': name, 'id': id.tolist()}
    col.insert_one(data)
    print(name)
  except IndexError:
    error_col.insert_one({'name': name})
    print('cannot add: ', name)

client.close()
