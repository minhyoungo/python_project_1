from db import Person, Admin
from util import Util
from program import Program
from datetime import datetime

# 회원로그인
DB_PEOPLE = []
admin_login_code = "fourleaf0309"
now = datetime.now()


def start_app():
    # now = datetime.now()
    # print(now)

    print("🚀🚀🚀 HOME 🚀🚀🚀")

    print("1. 출석 🚀")
    print("0 관리자 모드 🛸")

    answer = Util.custom_input()

    if answer is False:
        print("[SYSTEM] 잘못 입력하셨습니다.")
        start_app()
    else:
        if answer == 0:

            login_admin()
        elif answer == 1:
            print("🚀출석을 체크를 위해 로그인 하세요🚀")

            if len(DB_PEOPLE) == 0:
                print("[SYSTEM] 출석할 학생이 없습니다.")
            elif len(DB_PEOPLE) > answer:
                print("dpfj")
            else:
                result = Program.chul_check(DB_PEOPLE)
                if result is True:

                    Program.chul_check(DB_PEOPLE)
                    Program.is_late()

            start_app()
        else:
            print("[SYSTEM] 잘못 입력하셨습니다.")
            start_app()


def login_admin():
    print("관리자 로그인")

    id = input("아이디를 입력하세요. | 홈으로 갈려면 '/home'를 입력하세요. >>")
    pw = input("비밀번호 입력 >>")
    if(id == "system" and pw == "fourleaf0309"):
        print("로그인되었습니다.")

        admin()
    elif id == "/home":
        start_app()
    else:
        print("로그인 실패")
        login_admin()


def admin():
    Util.custom_print()
    answer = Util.custom_input()

    if answer is False:
        print("[SYSTEM] 잘못 입력하셨습니다.")
        admin()
    else:
        if answer == 0:
            start_app()

        elif answer == 1:
            print("🛸 전체 학생 🛸")
            Program.view_all_user(DB_PEOPLE)

            admin()
        elif answer == 2:
            print("🛸 바른 학생 🛸")

            admin()

        elif answer == 3:
            print("🛸 지각한 학생 🛸")

            admin()

        elif answer == 4:
            print("🛸 결석한 학생 🛸")

            admin()

        elif answer == 5:
            print("🛸 학생 추가하기 🛸")
            print("유저를 등록합니다. 이름과 비밀번호를 설정해주세요.")
            result = Program.create_people(DB_PEOPLE)

            print("[SYSTEM] ✅ 학생 추가에 성공하였습니다.")

            admin()

        elif answer == 6:
            print("🛸 학생 정보 삭제하기 🛸")

            if len(DB_PEOPLE) == 0:
                print("삭제할 학생 정보가 없습니다.")
            else:
                result = Program.delete_people(DB_PEOPLE)
                print(result)
                if len(DB_PEOPLE) == -1:
                    print("[SYSTEM] ❌ 삭제할 유저가 없습니다.")

                elif result is True:

                    print("[SYSTEM] ✅ 학생 정보 삭제에 성공하였습니다.")

                else:
                    print("[SYSTEM] ❌ 학생 정보 삭제에 실패하였습니다. 다시 시도해주세요")

            admin()


start_app()
# admin()
