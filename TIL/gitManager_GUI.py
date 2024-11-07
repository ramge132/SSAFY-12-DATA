import sys
import os
import subprocess
import platform
import shutil
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, QVBoxLayout,
                             QWidget, QLabel, QInputDialog, QMessageBox,
                             QTextEdit, QHBoxLayout, QDialog)
from PyQt5.QtGui import QFont, QFontDatabase 
from PyQt5.QtCore import Qt

# 포함된 폰트 파일 경로 설정
def load_fonts():
    font_path_black = "Pretendard-Black.otf"
    font_path_bold = "Pretendard-Bold.otf"
    if hasattr(sys, '_MEIPASS'):
        font_path_black = os.path.join(sys._MEIPASS, "Pretendard-Black.otf")
        font_path_bold = os.path.join(sys._MEIPASS, "Pretendard-Bold.otf")

    QFontDatabase.addApplicationFont(font_path_black)
    QFontDatabase.addApplicationFont(font_path_bold)

# Git 명령 실행 함수
def run_subprocess(command, log_func=None):
    startupinfo = None
    if platform.system() == "Windows":
        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW

    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, startupinfo=startupinfo)
    if log_func:
        if result.stdout:
            log_func(result.stdout)
        if result.stderr:
            log_func(result.stderr)
    return result

# 저장소 클론 함수
def clone_repositories(subject, set_number, log_func=None):
    original_dir = os.getcwd()
    if not os.path.exists(subject):
        os.makedirs(subject)

    os.chdir(subject)
    if log_func:
        log_func(f"{os.getcwd()}으로 클론하는 중...")

    stages_dict = {'hw': [2, 4], 'ws': [1, 2, 3, 4, 5, 'a', 'b', 'c']}
    for sep, stages in stages_dict.items():
        for stage in stages:
            folder_name = f"{subject}_{sep}_{set_number}_{stage}"
            if os.path.exists(folder_name):
                log_func(f"{folder_name}가 이미 존재합니다.")
                os.chdir(folder_name)
                run_subprocess(['git', 'pull', 'origin', 'master'], log_func)
                os.chdir('..')
            else:
                url = f"https://lab.ssafy.com/taeyoun9/{subject}_{sep}_{set_number}_{stage}"
                log_func(f"git clone {url}")
                run_subprocess(['git', 'clone', url], log_func)
    os.chdir(original_dir)
    
# 저장소 푸시 함수
def push_repositories(subject, log_func=None):
    if not os.path.exists(subject):
        log_func(f"{subject} 폴더가 존재하지 않습니다.")
        return
    original_dir = os.getcwd()
    os.chdir(subject)
    for dir in os.listdir():
        os.chdir(dir)
        run_subprocess(['git', 'add', '.'], log_func)
        run_subprocess(['git', 'commit', '-m', f'Update {subject} - {dir}'], log_func)
        run_subprocess(['git', 'push', 'origin', 'master'], log_func)
        log_func(f"{dir} repository has been pushed.")
        os.chdir('..')
    os.chdir(original_dir)

# .git 폴더 삭제 함수
def delete_git_folder(subject, log_func=None):
    if os.path.exists(subject):
        for root, dirs, files in os.walk(subject):
            if '.git' in dirs:
                git_folder_path = os.path.join(root, '.git')
                log_func(f'Deleting {git_folder_path}...')
                shutil.rmtree(git_folder_path)
                log_func(f'{git_folder_path}는 성공적으로 제거되었습니다.')
    else:
        log_func(f"{subject} 폴더가 존재하지 않습니다.")

# 폴더 복사 함수
def copy_subject_folder(subject, log_func=None):
    destination = r"C:\Users\rbfrl\OneDrive\Documents\VSCode\github\SSAFY-12-DATA\TIL"
    source = os.path.join(os.getcwd(), subject)
    
    if os.path.exists(source):
        destination_path = os.path.join(destination, subject)
        log_func(f'{source}를 {destination_path}으로 복사하겠습니다.')
        if os.path.exists(destination_path):
            shutil.rmtree(destination_path)
        shutil.copytree(source, destination_path)
        log_func(f'{subject}가 {destination}에 성공적으로 복사되었습니다.')
    else:
        log_func(f"{subject} 폴더가 존재하지 않습니다.")

# upstream 추가 함수
def add_upstream(subject, log_func=None):
    if not os.path.exists(subject):
        log_func(f"{subject} 폴더가 존재하지 않습니다.")
        return
    original_dir = os.getcwd()
    os.chdir(subject)
    for dir in os.listdir():
        os.chdir(dir)
        sep = dir.split('_')[1]
        stage = dir.split('_')[-1]
        repo_url = f"https://lab.ssafy.com/data_track/{subject}_daily_practice/{subject}_{sep}_{stage}"
        result = run_subprocess(['git', 'remote', 'add', 'upstream', repo_url], log_func)
        if result.returncode == 0:
            log_func(f"{dir}에 upstream remote를 성공적으로 추가했습니다.")
        else:
            log_func(f"{dir}에 upstream remote를 추가하는데 실패했습니다. {result.stderr}")
        os.chdir('..')
    os.chdir(original_dir)

# upstream에서 업데이트 가져오기 함수
def pull_upstream(subject, log_func=None):
    if not os.path.exists(subject):
        log_func(f"{subject} 폴더가 존재하지 않습니다.")
        return
    original_dir = os.getcwd()
    os.chdir(subject)
    for dir in os.listdir():
        os.chdir(dir)
        run_subprocess(['git', 'pull', 'upstream', 'master'], log_func)
        log_func(f"{dir}에서 upstream의 업데이트를 가져왔습니다.")
        os.chdir('..')
    os.chdir(original_dir)

# develop 브랜치 생성 함수
def create_develop_branch(subject, log_func=None):
    if not os.path.exists(subject):
        log_func(f"{subject} 폴더가 존재하지 않습니다.")
        return
    original_dir = os.getcwd()
    os.chdir(subject)
    for dir in os.listdir():
        os.chdir(dir)
        run_subprocess(['git', 'checkout', '-b', 'develop'], log_func)
        log_func(f"{dir}에서 develop 브랜치를 생성했습니다.")
        os.chdir('..')
    os.chdir(original_dir)

# 단색 텍스트 타이틀을 위한 Label 클래스
class TitleLabel(QLabel):
    def __init__(self, text):
        super().__init__(text)
        self.setFont(QFont("Pretendard Black", 28))
        self.setStyleSheet("color: #09bbeb;")
        self.setAlignment(Qt.AlignCenter)

# 메인 윈도우 클래스
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SSAFY GIT 관리 시스템")
        self.resize(800, 600)
        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)

        title_label = TitleLabel("SSAFY GIT 관리 시스템")
        main_layout.addWidget(title_label)

        description_label = QLabel("Made by Taeyeong (ramge132)")
        description_label.setAlignment(Qt.AlignCenter)
        description_label.setStyleSheet("font-size: 14px; color: gray; font-family: 'Pretendard';")
        main_layout.addWidget(description_label)

        buttons_layout = QVBoxLayout()
        main_layout.addLayout(buttons_layout)

        operations = [
            ("CLONE", self.clone_repos),
            ("PUSH", self.push_repos),
            ("DELETE .git Folders", self.delete_git_folders),
            ("COPY", self.copy_subject_folder),
            ("ADD Upstream Remote", self.add_upstream),
            ("PULL Upstream Updates", self.pull_upstream),
            ("CREATE Develop Branch", self.create_develop_branch),
            ("EXIT", self.close)
        ]

        for i in range(0, len(operations), 2):
            row_layout = QHBoxLayout()
            for j in range(2):
                if i + j < len(operations):
                    text, func = operations[i + j]
                    btn = QPushButton(text)
                    btn.setFixedSize(180, 50)
                    btn.clicked.connect(func)
                    btn.setStyleSheet("""
                        QPushButton {
                            font-size: 14px;
                            background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #09bbeb, stop:1 #0999ee);
                            color: white;
                            border-radius: 5px;
                            font-family: 'Pretendard SemiBold';
                        }
                        QPushButton:hover {
                            background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #0999ee, stop:1 #09bbeb);
                        }
                    """)
                    row_layout.addWidget(btn)
            buttons_layout.addLayout(row_layout)

        self.log_text_edit = QTextEdit()
        self.log_text_edit.setReadOnly(True)
        self.log_text_edit.setStyleSheet("font-size: 12px;")
        main_layout.addWidget(self.log_text_edit)

    def log(self, message):
        self.log_text_edit.append(message)

    def select_subject_dialog(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("과목 선택")
        dialog.resize(400, 200)
        layout = QVBoxLayout()
        dialog.setLayout(layout)

        self.selected_subject = None
        subjects = ['python', 'web', 'js', 'django', 'db', 'vue', 'data_analysis']
        for subject in subjects:
            btn = QPushButton(subject)
            btn.clicked.connect(lambda _, s=subject: self.handle_subject_selection(dialog, s))
            layout.addWidget(btn)

        dialog.exec_()
        return self.selected_subject

    def handle_subject_selection(self, dialog, subject):
        self.selected_subject = subject
        dialog.accept()

    def clone_repos(self):
        subject = self.select_subject_dialog()
        if subject:
            set_number, ok = QInputDialog.getText(self, "Clone Repositories", "세트 번호를 입력해 주세요:")
            if ok and set_number:
                self.log(f"Cloning repositories for subject: {subject}, set number: {set_number}")
                clone_repositories(subject, set_number, self.log)
            else:
                QMessageBox.warning(self, "Input Error", "세트 번호를 입력해 주세요.")
        else:
            QMessageBox.warning(self, "Input Error", "과목을 선택해 주세요.")

    def push_repos(self):
        subject = self.select_subject_dialog()
        if subject:
            self.log(f"Pushing repositories for subject: {subject}")
            push_repositories(subject, self.log)
        else:
            QMessageBox.warning(self, "Input Error", "과목을 선택해 주세요.")

    def delete_git_folders(self):
        subject = self.select_subject_dialog()
        if subject:
            self.log(f"Deleting .git folders in subject: {subject}")
            delete_git_folder(subject, self.log)
        else:
            QMessageBox.warning(self, "Input Error", "과목을 선택해 주세요.")

    def copy_subject_folder(self):
        subject = self.select_subject_dialog()
        if subject:
            self.log(f"Copying subject folder: {subject}")
            copy_subject_folder(subject, self.log)
        else:
            QMessageBox.warning(self, "Input Error", "과목을 선택해 주세요.")

    def add_upstream(self):
        subject = self.select_subject_dialog()
        if subject:
            self.log(f"Adding upstream remote for subject: {subject}")
            add_upstream(subject, self.log)
        else:
            QMessageBox.warning(self, "Input Error", "과목을 선택해 주세요.")

    def pull_upstream(self):
        subject = self.select_subject_dialog()
        if subject:
            self.log(f"Pulling upstream updates for subject: {subject}")
            pull_upstream(subject, self.log)
        else:
            QMessageBox.warning(self, "Input Error", "과목을 선택해 주세요.")

    def create_develop_branch(self):
        subject = self.select_subject_dialog()
        if subject:
            self.log(f"Creating develop branch for subject: {subject}")
            create_develop_branch(subject, self.log)
        else:
            QMessageBox.warning(self, "Input Error", "과목을 선택해 주세요.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    load_fonts()
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
