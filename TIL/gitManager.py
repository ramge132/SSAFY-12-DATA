########################################################
##          AUTOMATIC GIT MANAGEMENT SYSTEM           ##
##                                                    ##
##                    How to use                      ##
##       C: Clone lab.ssafy repo automatically        ##
##       D: Delete .git folders automatically         ##
##       P: Push to lab.ssafy automatically           ##
##       S: SSAFY github management(Personal)         ##
##       R: Add upstream remote to repositories       ##
##       U: Pull updates from upstream repositories   ##
##       B: Create develop branch in repositories     ##
##       X: Exit the program                          ##
##                                                    ##
##                        Made by taeyeong(ramge132)  ##
########################################################

import os
import subprocess
import platform

def clear_console():
    os.system('cls' if platform.system() == 'Windows' else 'clear')

def clone_repositories(subject, set_number):
    # 현재 작업 디렉토리를 저장
    original_dir = os.getcwd()
    
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
    
    # 작업이 끝난 후 원래 디렉토리로 돌아감
    os.chdir(original_dir)


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

def add_upstream(subject):
    os.chdir(subject)
    dir_list = os.listdir()
    
    for dir in dir_list:
        os.chdir(dir)
        sep = dir.split('_')[1]
        stage = dir.split('_')[-1]
        repo_url = f"https://lab.ssafy.com/data_track/{subject}_daily_practice/{subject}_{sep}_{stage}"
        result = subprocess.run(['git', 'remote', 'add', 'upstream', repo_url], capture_output=True)
        if result.returncode == 0:
            print(f"{dir}에 upstream remote를 성공적으로 추가했습니다.")
        else:
            print(f"{dir}에 upstream remote를 추가하는데 실패했습니다. {result.stderr.decode()}")
        os.chdir('..')

def pull_upstream(subject):
    os.chdir(subject)
    dir_list = os.listdir()
    
    for dir in dir_list:
        os.chdir(dir)
        subprocess.run(['git', 'pull', 'upstream', 'master'])
        os.chdir('..')

def create_develop_branch(subject):
    os.chdir(subject)
    dir_list = os.listdir()
    
    for dir in dir_list:
        os.chdir(dir)
        subprocess.run(['git', 'checkout', '-b', 'develop'])
        os.chdir('..')

if __name__ == "__main__":
    while True:
        clear_console()
        print("########################################################")
        print("##          AUTOMATIC GIT MANAGEMENT SYSTEM           ##")
        print("##                                                    ##")
        print("##                    How to use                      ##")
        print("##       C: Clone lab.ssafy repo automatically        ##")
        print("##       D: Delete .git folders automatically         ##")
        print("##       P: Push to lab.ssafy automatically           ##")
        print("##       S: SSAFY github management(Personal)         ##")
        print("##       R: Add upstream remote to repositories       ##")
        print("##       U: Pull updates from upstream repositories   ##")
        print("##       B: Create develop branch in repositories     ##")
        print("##       X: Exit the program                          ##")
        print("##                                                    ##")
        print("##                        Made by taeyeong(ramge132)  ##")
        print("########################################################")

        task = input("작업을 선택해 주세요 (C, P, D, S, R, U, B, X): ").lower()

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
        elif task == 'r':
            subject = input("과목을 입력해 주세요 (예: python, web, js, django, db, vue): ")
            add_upstream(subject)
        elif task == 'u':
            subject = input("과목을 입력해 주세요 (예: python, web, js, django, db, vue): ")
            pull_upstream(subject)
        elif task == 'b':
            subject = input("과목을 입력해 주세요 (예: python, web, js, django, db, vue): ")
            create_develop_branch(subject)
        elif task == 'x':
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 입력입니다. 'C', 'P', 'D', 'S', 'R', 'U', 'B' 또는 'X'를 입력해 주세요.")
        
        input("\n계속하려면 아무 키나 누르세요...")

