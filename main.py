from difflib import SequenceMatcher
from timeit import default_timer as timer
from tkinter import *
import random

list_of_texts = ['Ministers are desperately trying to find ways to offer financial\n'
                 ' support to Welsh businesses hit by cancellations in response to\n'
                 ' the phenomenal spread of Omicron.',
                 'This is my text that I want to test myself for subject of typing efficiency. Good luck!\n',
                 'Two people have been confirmed missing after a block of flats was gutted by fire in a suspected\n '
                 'arson attack.'
                 'One person has been confirmed dead following the blaze.',
                 'Voters have begun to cast their ballots in the North Shropshire by-election as they choose \n'
                 'a replacement for former Conservative MP Owen Paterson.From 7am this morning to 10pm tonight,\n'
                 ' voters in the constituency will decide on a new local MP following ex-cabinet minister Mr Paterson\n'
                 'decision to quit the House of Commons last month.']

text = random.choice(list_of_texts)
begin_timing = None


def start():
    global begin_timing
    begin_timing = timer()
    lbl.config(text=f'{text}')


def stop():
    inp = txt_fld.get().split(' ')
    if inp == '':
        quit()
    text_into_list = text.split(' ')

    same = SequenceMatcher(None, inp, text_into_list).ratio()
    lbl3.config(text=f'Percent of effectiveness is: {int(same*100)} %')
    different_words = set(inp).symmetric_difference(set(text_into_list))
    same_words = len(text_into_list) - len(different_words)

    # print(f'You typed: {same_words} words.')
    lbl4.config(text=f'You typed: {same_words} words.')
    finish_timing = timer()
    global begin_timing
    time = finish_timing - begin_timing
    # print(f'It took you: {time} seconds to complete the test.')
    lbl5.config(text=f'It took you: {time} seconds to complete the test.')
    sec_per_word = time/len(inp)
    words_per_minute = 60 / sec_per_word
    # print(f'You typed {int(words_per_minute)} words per minute.')
    lbl6.config(text=f'You typed: {int(words_per_minute)} words per minute!')


window = Tk()
window.title('Typing Speed Test. TST')
window.geometry("1200x600+10+20")

lbl = Label(window, text="Press 'Start' to begin the test", fg='green', font=("Helvetica", 16))
lbl.place(x=60, y=50)

lbl3 = Label(window, text='lbl3', fg='blue', font=('Arial', 16))
lbl3.place(x=30, y=460)

lbl4 = Label(window, text='lbl4', fg='blue', font=('Arial', 16))
lbl4.place(x=30, y=490)

lbl5 = Label(window, text='lbl5', fg='blue', font=('Arial', 16))
lbl5.place(x=30, y=520)

lbl6 = Label(window, text='Test', fg='red', font=('Helvetica', 18))
lbl6.place(x=30, y=550)

txt_fld = Entry(window, text="", bd=5)
txt_fld.place(x=400, y=300, width=300, height=120)

btn_start = Button(window, text="Start", width=20, height=5, fg='blue')
btn_start['command'] = start
btn_start.place(x=1000, y=500)

btn_stop = Button(window, text='Stop', width=20, height=5, fg='red')
btn_stop['command'] = stop
btn_stop.place(x=800, y=500)

window.mainloop()