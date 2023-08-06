# capture = cv2.VideoCapture('rtsp://username:password@192.168.1.64/1')
# capture = cv2.VideoCapture('rtsp://zyf:123456@192.168.2.28:8554/live')

# source = str(source)
# save_img = not nosave and not source.endswith('.txt')  # save inference images
# is_file = Path(source).suffix[1:] in (IMG_FORMATS + VID_FORMATS)
# is_url = source.lower().startswith(('rtsp://', 'rtmp://', 'http://', 'https://'))
# webcam = source.isnumeric() or source.endswith('.txt') or (is_url and not is_file)
# if is_url and is_file:
#     source = check_file(source)  # download



# import re
# # # print(re.search('www', 'www.runoob.com').span())  # 在起始位置匹配
# # # print(re.search('com', 'www.runoob.com').span())
# # print(re.search('ru', 'www.runoob.com') != None)


# def is_chinese(s='人工智能'):
#     # Is string composed of any Chinese characters?
#     return re.search('[\u4e00-\u9fff]', s)


# print(is_chinese("你好"))

# a = "aaa.bbb.ccc.log"
# print(a.endswith('ccc.log'))

from opencv_webcam import webcam_opencv

webcam_opencv(is_autoSaveFrame=True)