#hackerank - https://www.hackerrank.com/challenges/nested-list/problem

def nested_lists_challenge(input):
    students = []
    score_list = []

    if __name__ == '__main__':
        for _ in range(int(input())):
            name = input()
            score = float(input())

            temp = []
            temp.append(name)
            temp.append(score)
            score_list.append(score)
            students.append(temp)

        score_list = list(dict.fromkeys(score_list))
        score_list.sort()
        if len(students) >= 2:
            second_lowest_students = []
            second_lowest_score = score_list[1]

            for i in students:
                if second_lowest_score in i:
                    # print(i[0])
                    second_lowest_students.append(i[0])
                else:
                    pass

            print('\n'.join(sorted(second_lowest_students, key=lambda second_lowest_students: second_lowest_students)))

        else:
            print(students[0][0])

input = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
nested_lists_challenge(input)