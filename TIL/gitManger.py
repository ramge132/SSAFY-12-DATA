########################################################
##          AUTOMATIC GIT MANAGEMENT SYSTEM           ##
##                                                    ##
##                    How to use                      ##
##       C: Clone lab.ssafy repo automatically        ##
##       D: Delete .git folders automatically         ##
##       P: Push to lab.ssafy automatically           ##
##       S: SSAFY github management(Personal)         ##
##                                                    ##
##                        Made by taeyeong(ramge132)  ##
########################################################

import os
import subprocess

def clone_repositories(subject, set_number):
    if not os.path.exists(subject):
        os.makedirs(subject)

    os.chdir(subject)
    current_folder = os.getcwd()

    print(f"{current_folder}으로 clone 하는 중...")

    seperators = ['hw', 'ws']
    
    stages_dict = {
        'hw': [2, 4],
        'ws': [1, 2, 3, 4, 5, 'a', 'b', 'c']
    }

    for sep in seperators:
        stages = stages_dict[sep]
        for stage in stages:
            folder_name = f"{subject}_{sep}_{set_number}_{stage}"
            if os.path.exists(folder_name):
                print(f"{folder_name}가 이미 존재합니다.")
                os.chdir(folder_name)
                subprocess.run(['git', 'pull', 'origin', 'master'])
                os.chdir('..')
            else:
                url = f"https://lab.ssafy.com/taeyoun9/{subject}_{sep}_{set_number}_{stage}"
                print(f"git clone {url}")
                subprocess.run(['git', 'clone', url])

def push_repositories(subject):
    os.chdir(subject)
    dir_list = os.listdir()

    for dir in dir_list:
        os.chdir(dir)
        subprocess.run(['git', 'add', '.'])
        subprocess.run(['git', 'commit', '-m', f'Update {subject} - {dir}'])
        subprocess.run(['git', 'push', 'origin', 'master'])
        os.chdir('..')

def delete_git_folder(subject):
    if os.path.exists(subject):
        for root, dirs, files in os.walk(subject):
            if '.git' in dirs:
                git_folder_path = os.path.join(root, '.git')
                print(f'Trying to delete {git_folder_path} using system command...')
                os.system(f'rmdir /S /Q "{git_folder_path}"')
                if not os.path.exists(git_folder_path):
                    print(f'{git_folder_path}는 성공적으로 제거되었습니다.')
                else:
                    print(f'{git_folder_path}를 제거하는데 실패하였습니다.')
    else:
        print(f"{subject}폴더가 존재하지 않습니다.")

def copy_subject_folder(subject):
    destination = r"C:\Users\rbfrl\OneDrive\Documents\VSCode\github\SSAFY-12-DATA\TIL"
    source = os.path.join(os.getcwd(), subject)
    
    if os.path.exists(source):
        destination_path = os.path.join(destination, subject)
        print(f'{source}를 {destination_path}으로 복사하겠습니다.')
        os.system(f'xcopy /E /I /H "{source}" "{destination_path}"')
        if os.path.exists(destination_path):
            print(f'{subject}가 {destination}에 성공적으로 복사되었습니다.')
        else:
            print(f'{subject}를 {destination}에 복사하는데 실패하였습니다.')
    else:
        print(f"{subject}폴더가 존재하지 않습니다.")

if __name__ == "__main__":
    task = input("작업을 선택해 주세요 (c: clone, p: push, d: .git 삭제, s: 폴더 복사): ").lower()

    if task == 'c':
        subject = input('과목을 입력해 주세요 (예: python, web, js, django, db, vue): ')
        set_number = input('세트 번호를 입력해 주세요: ')
        clone_repositories(subject, set_number)
    elif task == 'p':
        subject = input("과목을 입력해 주세요 (예: python, web, js, django, db, vue): ")
        push_repositories(subject)
    elif task == 'd':
        subject = input("과목을 입력해 주세요 (예: python, web, js, django, db, vue): ")
        delete_git_folder(subject)
    elif task == 's':
        subject = input("과목을 입력해 주세요 (예: python, web, js, django, db, vue): ")
        copy_subject_folder(subject)
    else:
        print("잘못된 입력입니다. 'c', 'p', 'd' 또는 's'를 입력해 주세요.")
