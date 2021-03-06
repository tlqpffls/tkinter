from tkinter import *
import pandas as pd
import os

print(os.getcwd())

# 파일 불러오기
dat = pd.read_csv('./대한석탄공사_석탄용어사전_20201231.csv', encoding='utf-8')
# dat = pd.read_csv('./dic_csv.csv')
# dat = pd.read_excel('./dic_excel.xlsx')

# 기능 추가
# 제출 버튼을 클릭했을 때, 동작
def click(event=None) :
    print("버튼이 클릭되었습니다.")
    print(dat)
    word = entry.get()  # 아래 엔트리 상자의 내용을 text로 넣는다.
    # END로 지정하면 문자열이 입력된 최종 입력 지점을 의미.
    # 특정 시작 지점부터 텍스트 엔트리 위젯의 끝까지 모두 지우기 위해 END를 쓴다.
    output.delete(0.0, END)  # 텍스트 박스 내용을 지운다.
    try:
        # def_word = dat.loc[dat['word'] == word, 'def'].values[0]
        def_word = dat.loc[dat['용어명'] == word, '용어설명'].values[0]
        # print(dat.loc[dat['용어명'] == word, '용어설명'])
        # print(def_word)
    except:
        def_word = "단어를 뜻을 찾을 수 없음."

    output.insert(END, def_word)

window = Tk()
window.title('나의 사전')

# 01 입력상자 설명 레이블
label = Label(window, text='원하는 단어 입력 후, 엔터 키 누르기')
label.grid(row=0, column=0, sticky=W)

# 02 텍스트 입력이 가능한 상자(Entry)
entry = Entry(window, width=15, bg="light green")
entry.grid(row=1, column=0, sticky=W)

# 03 제출 버튼 추가
btn = Button(window, width=5, text='제출', command=click)
btn.grid(row=2, column=0, sticky=W)

# 04 설명 레이블 - 의미
label2 = Label(window, text='\n의미 : ')
label2.grid(row=3, column=0, sticky=W)

# 05 텍스트 박스 입력 상자
# columnspan=2 는 (4,0)~(4,1) 위치까지 분포
output = Text(window, width=50, height=6, wrap=WORD, background="light green")
output.grid(row=4, column=0, columnspan=2, sticky=W)

# 엔터키 입력 시 click 실행
window.bind("<Return>", click)
# <Key> 모든키에 해당하는 이벤트코드
# <Return> : enter키 이벤트코드
# <less> : < 키 이벤트코드
# <space> : 스페이스바 이벤트코드


# 메인 반복문 실행
window.mainloop()

