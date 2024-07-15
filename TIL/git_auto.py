########################################################
##                  깃허브 자동 clone                  ##
##                                                    ##
## Automatically clone SSAFY repo to the current path ##
##                                                    ##
########################################################


import os
import subprocess

# 현재 폴더 경로를 변수에 저장
current_folder = os.getcwd()

# 사용자 입력 받기
subject = input('과목을 입력해 주세요 (예: python, web, js, django, db, vue): ')
set_number = input('세트 번호를 입력해 주세요: ')

# 구분에 따른 단계 설정
seperators = ['hw', 'ws']
stages_dict = {
    'hw': [2, 4],  # 과제의 경우 2, 4
    'ws': [1, 2, 3, 4, 5, 'a', 'b', 'c']  # 워크숍의 경우 1~5, a~c
}

for sep in seperators:
    stages = stages_dict[sep]
    for stage in stages:
        URL = f'https://lab.ssafy.com/taeyoun9/{subject}_{sep}_{set_number}_{stage}'
        print(f'Cloning from URL: {URL}')
        try:
            subprocess.run(['git', 'clone', URL], check=True)
            # 폴더 경로 추출
            folder_name = f'{subject}_{sep}_{set_number}_{stage}'
            folder_path = os.path.join(current_folder, folder_name)
            # .git 폴더 제거
            git_folder_path = os.path.join(folder_path, '.git')
            if os.path.exists(git_folder_path):
                subprocess.run(['rm', '-rf', git_folder_path], check=True)
                print(f'{folder_path}에서 .git 폴더를 삭제하였습니다.')
            else:
                print(f'{folder_path}에서 .git 폴더를 찾지 못했습니다.')
        except subprocess.CalledProcessError as e:
            print(f'URL로부터 clone하지 못했습니다.: {URL}. Error: {e}')

print("Git clone을 성공적으로 마쳤습니다.")