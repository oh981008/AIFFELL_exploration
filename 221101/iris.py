import os
image_dir_path = "C:\\Users\\오순정\\Pictures\\Saved Pictures"   
# 각자의 사진이 보관된 디렉토리를 골라 주세요. 
# 클라우드의 경우에는 사진이 이미 있으므로 코드를 실행시켜주세요. 
photo = os.listdir(image_dir_path )
png = [png for png in photo if png.endswith('.jpg')]
print(png)