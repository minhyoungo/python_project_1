from db import Person

from datetime import datetime
from util import Util
from datetime import datetime


class Program:

    def is_late():

        now = datetime.now()
        if int(now.hour) <= 8:
            if int(now.minute) <= 00:
                print(f"π μ§κΈμ {now.hour}μ {now.minute}λΆμ΄μμ.")
                print("π λ¦μ§μκ² μ μλ€μ!!")
            else:
                print(f"π μ§κΈμ {now.hour}μ {now.minute}λΆμ΄μμ.")
                print("π  λλ¬΄ λ¦μμ΄μ!!")
        else:
            print(f"π μ§κΈμ {now.hour}μ {now.minute}λΆμ΄μμ.")
            print("π‘ λλ¬΄ λ¦μμ΄μ!!")

    def chul_check(people):

        print("___________________________________________")
        for p in enumerate(people):
            print(f"{(p[0] + 1)} - {p[1].name}")
        print("___________________________________________")

        answer = int(input("μΆμν  μ¬λμ λ²νΈλ₯Ό μλ ₯ν΄μ£ΌμΈμ. >> "))
        entered_password = input("λΉλ°λ²νΈλ₯Ό μλ ₯νμΈμ. >> ")
        user = people[(answer - 1)]
        user_password = str(people[(answer - 1)]).split(" | ")[1]
        user_chulcheck = str(people[(answer - 1)]).split(" | ")[2]
        # print(user_chulcheck)
        # print(people)
        if user_password == entered_password:
            if user_chulcheck == "True":
                print("μ΄λ―Έ μΆμ ν¨")
                return False
            else:
                print("μΆμλμμ΅λλ€.")

                person_data = Person()
                c = True
                person_data.c_data_setter(c)
                # print(f"h{user_chulcheck}")
                # print(f"l{Person.chulcheck}")
                return True

        else:
            print("λΉλ°λ²νΈκ° νλ Έμ΅λλ€.")
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

        name = input("μ΄λ¦μ μλ ₯νμΈμ. >> ")
        secret_code = input("λΉλ°λ²νΈλ₯Ό μλ ₯νμΈμ. >> ")
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
            print(f"μΆμ : {p.chul_check}")
            print("___________________________________________")

            # print(f"κ²°μ : {}")

    def delete_people(people):
        prev_length = len(people)

        print("==============================")
        for p in enumerate(people):
            print(f"{(p[0] + 1)} - {p[1].name}")
        print("==============================")
        answer = int(input("μ­μ ν  μ¬λμ λ²νΈλ₯Ό μλ ₯ν΄μ£ΌμΈμ. >>"))

        people.pop(answer - 1)
        next_length = len(people)

        if prev_length > next_length:
            return True
        else:
            return False
