
# entrada
tape_1 = input()

#para marcar o final da entrada, B de branco
tape_1 += 'B'

#fita dos a`s, inicialmente so ha branco(B) na fita
tape_2 = ['B']

#fita dos b`s, inicialmente so ha branco(B) na fita
tape_3 = ['B']

#fita dos c`s, inicialmente so ha branco(B) na fita
tape_4 = ['B']

headstock_1 = 0
headstock_2 = 1
headstock_3 = 1
headstock_4 = 1

result = "REJEITA"

def q0():
    global tape_1
    global tape_2
    global tape_3
    global tape_4
    global headstock_1
    global headstock_2
    global headstock_3
    global headstock_4
    if tape_1[headstock_1] == 'a':
        tape_2.append(tape_1[headstock_1])
        headstock_2 += 1
        headstock_1 += 1
        q0()
    elif tape_1[headstock_1] == 'b':
        tape_3.append(tape_1[headstock_1])
        headstock_3 += 1
        headstock_1 += 1
        q0()
    elif tape_1[headstock_1] == 'c':
        tape_4.append(tape_1[headstock_1])
        headstock_4 += 1
        headstock_1 += 1
        q0()
    elif tape_1[headstock_1] == ' ':
        headstock_1 += 1
        q0()
    elif tape_1[headstock_1] == '#':
        headstock_1 += 1
        tape_2.append('F')
        headstock_2 -= 1
        tape_3.append('F')
        headstock_3 -= 1
        tape_4.append('F')
        headstock_4 -= 1
        q1()

   
def q1():
    global tape_1
    global tape_2
    global tape_3
    global tape_4
    global headstock_1
    global headstock_2
    global headstock_3
    global headstock_4
    if (tape_1[headstock_1] == 'B' and
        tape_2[headstock_2] == 'a' and
        tape_3[headstock_3] == 'b' and
        tape_4[headstock_4] == 'c'):
        headstock_1 -= 1
        q2()    


def q2():
    global tape_2
    global tape_3
    global headstock_2
    global headstock_3
    if (tape_2[headstock_2] == 'a' and
        tape_3[headstock_3] == 'b'):
        headstock_2 -= 1
        headstock_3 -= 1
        q2()
    elif (tape_2[headstock_2] == 'B' and
          tape_3[headstock_3] == 'b'):
        headstock_3 -= 1
        q3()

def q3():
    global tape_2
    global tape_3
    global headstock_2
    global headstock_3
    if (tape_2[headstock_2] == 'B' and
        tape_3[headstock_3] == 'B'):
        headstock_2 += 1
        headstock_3 += 1
        q3()
    elif (tape_2[headstock_2] == 'B' and
          tape_3[headstock_3] == 'b'):
        headstock_2 += 1
        headstock_3 += 1
        q3()
    elif (tape_2[headstock_2] == 'a' and
          tape_3[headstock_3] == 'b'):
        headstock_2 += 1
        headstock_3 += 1
        q3()
    elif (tape_2[headstock_2] == 'F' and
          tape_3[headstock_3] == 'b'):
        headstock_2 -= 1
        q4()


def q4():
    global tape_3
    global tape_4
    global headstock_3
    global headstock_4
    if (tape_3[headstock_3] == 'b'and
        tape_4[headstock_4] == 'c'):
        headstock_3 -= 1
        headstock_4 -= 1
        q4()
    elif (tape_3[headstock_3] == 'B' and
          tape_4[headstock_4] == 'c'):
        headstock_4 -= 1
        q5()


def q5():
    global result
    result = "ACEITA"
   
q0()
print(tape_1.strip('B') + " " + result)
