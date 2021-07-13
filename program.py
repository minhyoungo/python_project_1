from db import Person

from datetime import datetime
from util import Util
from datetime import datetime


class Program:

    def is_late():

        now = datetime.now()
        if int(now.hour) <= 8:
            if int(now.minute) <= 00:
                print(f"🕖 지금은 {now.hour}시 {now.minute}분이에요.")
                print("😀 늦지않게 잘 왔네요!!")
            else:
                print(f"🕖 지금은 {now.hour}시 {now.minute}분이에요.")
                print("😠 너무 늦었어요!!")
        else:
            print(f"🕖 지금은 {now.hour}시 {now.minute}분이에요.")
            print("😡 너무 늦었어요!!")

    def chul_check(people):

        print("___________________________________________")
        for p in enumerate(people):
            print(f"{(p[0] + 1)} - {p[1].name}")
        print("___________________________________________")

        answer = int(input("출석할 사람의 번호를 입력해주세요. >> "))
        entered_password = input("비밀번호를 입력하세요. >> ")
        user = people[(answer - 1)]
        user_password = str(people[(answer - 1)]).split(" | ")[1]
        user_chulcheck = str(people[(answer - 1)]).split(" | ")[2]
        # print(user_chulcheck)
        # print(people)
        if user_password == entered_password:
            if user_chulcheck == "True":
                print("이미 출석 함")
                return False
            else:
                print("출석되었습니다.")

                person_data = Person()
                c = True
                person_data.c_data_setter(c)
                # print(f"h{user_chulcheck}")
                # print(f"l{Person.chulcheck}")
                return True

        else:
            print("비밀번호가 틀렸습니다.")
            return False

        #

        # print(p.chul_check)
        # print(enumerate(people[0].filter(entered_name)))
        # print(people)

        # if entered_name ==
        # for p in people:

        # print(list(people[0]))

    def create_people(people):
        prev_length = len(people)

        new_person = Person()

        name = input("이름을 입력하세요. >> ")
        secret_code = input("비밀번호를 입력하세요. >> ")
        chul_check = False

        new_person.data_setter(name, secret_code, chul_check)

        people.append(new_person)

        next_length = len(people)

        if prev_length < next_length:
            return True
        else:
            return False

    def view_all_user(people):

        for p in people:
            print(f"NAME : {p.name}")
            print(f"PASSWORD : {p.secret_code}")
            print(f"출석 : {p.chul_check}")
            print("___________________________________________")

            # print(f"결석 : {}")

    def delete_people(people):
        prev_length = len(people)

        print("==============================")
        for p in enumerate(people):
            print(f"{(p[0] + 1)} - {p[1].name}")
        print("==============================")
        answer = int(input("삭제할 사람의 번호를 입력해주세요. >>"))

        people.pop(answer - 1)
        next_length = len(people)

        if prev_length > next_length:
            return True
        else:
            return False
