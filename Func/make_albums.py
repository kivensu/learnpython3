def make_album(singer_name, album_name, album_number=''):
    album_info = {'singer_name': singer_name.title(
    ), 'album_name': album_name.title()}
    if album_number:
        album_info['album_number'] = album_number
    return album_info


#album01 = make_album('zhoujiellun', 'qilixiang')
# print(album01)
#album01 = make_album('beyond', 'guanghuisuiyue', '10')
# print(album01)
while True:
    singer_name = input("Please input you favorite singer name: ")
    if singer_name == "q":
        break
    album_name = input("Please input you favorite singer album name:")
    if album_name == "q":
        break
    album01 = make_album(singer_name, album_name)
    print(album01)
