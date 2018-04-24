# 학생 번호에 해당하는 학생 이름 찾기
# 입력: 학생 번호 리스트 s_no, 학생 이름 리스트 s_name, 찾는 학생 번호 find_no
# 출력: 해당하는 학생 이름, 해당하는 학생 이름이 없으면 물음표 "?"

def get_name(s_no, s_name, find_no):

    n = len(s_no)
    for i in range(0, n):
        if find_no == s_no[i]:
            return s_name[i]
    return "?"

if __name__ == '__main__':

    sample_no = [39, 14, 67, 105]
    sample_name = ["Justin", "John", "Mike", "Summer"]
    print (get_name(sample_no, sample_name, 105))
    print (get_name(sample_no, sample_name, 777))
