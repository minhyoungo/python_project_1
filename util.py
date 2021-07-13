import getpass
from datetime import datetime


class Util:

    def time_print():
        now = datetime.now()
        print(f"현재 시각 {now.hour}시 {now.minute}분")

    def custom_input():
        answer = input(">> ")
        # answerswer의 길이가 1보다 크다면

        if len(answer) > 1:
            return False
        elif len(answer) == 0:
            return False
        else:
            ascii_value = ord(answer)

            if ascii_value >= 48 and ascii_value <= 57:
                return int(answer)
            else:
                return False

    def code_input():
        entered_code = input(">> ")
        if entered_code != code:
            print("비밀번호가 일치하지 않습니다.")

    def add_code_input():
        code = input("사용할 비밀번호를 입력해 주세요. >> ")

        if len(code) != 4:
            print("비밀번호를 네자리로 설정하여주세요.")
            return False
        else:
            ascii_value2 = ord(code)

            if ascii_value2 >= 48 and ascii_value2 <= 57:
                c1 = int(code[0])
                c2 = int(code[1])
                c3 = int(code[2])
                c4 = int(code[3])

                if c1+1 == c2 and c2+1 == c3 and c3+1 == c4:
                    print("보안에 취약합니다.")
                    return False
                elif c1-1 == c2 and c2-1 == c3 and c3-1 == c4:
                    print("보안에 취약합니다.")
                    return False
                else:
                    print("생성완료")
                    return int(code)
            else:
                return False

        # if len(code) != 4:
        #     print("비밀번호를 네자리로 설정하여주세요.")
        #     return False
        # if c1+1 == c2 and c2+1 == c3 and c3+1 == c4:
        #     print("보안에 취약합니다.")
        # elif c1-1 == c2 and c2-1 == c3 and c3-1 == c4:
        #     print("보안에 취약합니다.")

    def pw_input():
        pw = getpass.getpass("패스워드를 입력하세요. >> ")

    def custom_print():
        print("🛸🛸🛸 ADMIN 🛸🛸🛸")
        print("0. 홈으로")
        print("1. 전체 학생 보기")
        print("2. 바른 학생 보기")
        print("3. 지각한 학생 보기")
        print("4. 결석한 학생 보기")
        print("5. 학생 추가하기")
        print("6. 학생 삭제하기")
