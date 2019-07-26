#a pyhton gui code to make team and count score during a match
from tkinter import *

score = 0
wic = 0
balls = 0
flag = 1
t = []
t1 = []

t2 = []
toss = 0
overss = 0
update = "0"
team1 = input("enter team 1 name\t")
team2 = input("enter team 2 name\t")
n = int(input("enter the number of players in each team\n"))
print("enter team1 players' names in their batting order\n")
for i in range(n):
    t1.append(input())
print("enter team2 players name in their batting order\n")
for i in range(n):
    t2.append(input())
toss = input("who wins the toss. If team1 press 1 or press 2\t")
if toss == 2:
    team1, team2 = team2, team1
    t1, t2 = t2, t1
print(team1)
print(t1)
print(team2)
print(t2)
tp = team1
t = t1
on = t[0]
off = t[1]
count = 2


def score0():
    global score, wic, balls, qq, flag
    qq = "dot"
    runlbl.configure(text=qq)
    balls += 1
    print(score)
    scorelbl.configure(text=tp + "-   " + str(score))
    overslbl.configure(text=str(int(balls / 6)) + "." + str(balls % 6))
    flag = 1


def score1():
    global score, wic, balls, on, off, qq, flag
    qq = "1"
    runlbl.configure(text=qq)
    score += 1
    balls += 1
    on, off = off, on
    print(score)
    scorelbl.configure(text=tp + "-   " + str(score))
    onstrike.configure(text=on)
    offstrike.configure(text=off)
    overslbl.configure(text=str(int(balls / 6)) + "." + str(balls % 6))
    flag = 1


def score2():
    global score, wic, balls, qq, flag
    qq = "2"
    runlbl.configure(text=qq)
    score += 2
    balls += 1
    print(score)
    scorelbl.configure(text=tp + "-   " + str(score))
    overslbl.configure(text=str(int(balls / 6)) + "." + str(balls % 6))
    flag = 1


def score3():
    global score, wic, balls, on, off, qq, flag
    qq = "3"
    runlbl.configure(text=qq)
    score += 3
    balls += 1
    on, off = off, on
    print(score)
    scorelbl.configure(text=tp + "-   " + str(score))
    onstrike.configure(text=on)
    offstrike.configure(text=off)
    overslbl.configure(text=str(int(balls / 6)) + "." + str(balls % 6))
    flag = 1


def score4():
    global score, wic, balls, qq, flag
    qq = "4"
    runlbl.configure(text=qq)
    score += 4
    balls += 1
    print(score)
    scorelbl.configure(text=tp + "-   " + str(score))
    overslbl.configure(text=str(int(balls / 6)) + "." + str(balls % 6))
    flag = 1


def score6():
    global score, wic, balls, qq, flag
    qq = "6!!!"
    runlbl.configure(text=qq)
    score += 6
    balls += 1
    print(score)
    scorelbl.configure(text=tp + "-   " + str(score))
    overslbl.configure(text=str(int(balls / 6)) + "." + str(balls % 6))
    flag = 1


def noball():
    global score, wic, balls, qq, flag
    qq = "noball"
    runlbl.configure(text=qq)
    score += 1
    print(score)
    scorelbl.configure(text=tp + "-   " + str(score))
    overslbl.configure(text=str(int(balls / 6)) + "." + str(balls % 6))
    flag = 1


def wide():
    global score, wic, balls, qq, flag
    qq = "wide"
    runlbl.configure(text=qq)
    score += 1
    print(score)
    scorelbl.configure(text=tp + "-   " + str(score))
    overslbl.configure(text=str(int(balls / 6)) + "." + str(balls % 6))
    flag = 1


def freehit():
    global score, wic, balls, flag, qq
    qq = "freehit"
    runlbl.configure(text=qq)
    score += 1
    balls -= 1
    flag = 0
    print(score)
    scorelbl.configure(text=tp + "-   " + str(score))
    overslbl.configure(text=str(int(balls / 6)) + "." + str(balls % 6))


def over():
    global score, wic, balls, on, off, qq, flag
    qq = "over up"
    runlbl.configure(text=qq)
    on, off = off, on
    print(score)
    scorelbl.configure(text=tp + "-   " + str(score))
    wiclbl.configure(text=wic)
    onstrike.configure(text=on)
    offstrike.configure(text=off)
    overslbl.configure(text=str(int(balls / 6)) + "." + str(balls % 6))
    flag = 1


def onrunout():
    global score, wic, balls, on, count, qq, flag
    qq = "run out"
    runlbl.configure(text=qq)
    wic += 1
    if (wic >= n - 1):
        inng()
    on = t[count]
    count += 1
    print(score)
    scorelbl.configure(text=tp + "-   " + str(score))
    wiclbl.configure(text=wic)
    onstrike.configure(text=on)
    offstrike.configure(text=off)
    overslbl.configure(text=str(int(balls / 6)) + "." + str(balls % 6))
    flag = 1


def offrunout():
    global score, wic, balls, on, off, count, qq, flag
    qq = "run out"
    runlbl.configure(text=qq)
    wic += 1
    if (wic >= n - 1):
        inng()
    off = t[count]
    count += 1
    print(score)
    scorelbl.configure(text=tp + "-   " + str(score))
    wiclbl.configure(text=wic)
    onstrike.configure(text=on)
    offstrike.configure(text=off)
    overslbl.configure(text=str(int(balls / 6)) + "." + str(balls % 6))
    flag = 1


def catch():
    global score, wic, balls, on, off, count, flag, qq
    if flag:
        qq = "catch"
        runlbl.configure(text=qq)
        wic += 1
        if (wic >= n - 1):
            inng()
        on = t[count]
        count += 1
        flag = 1
        print(score)
        scorelbl.configure(text=tp + "-  " + str(score))
        wiclbl.configure(text=wic)
        onstrike.configure(text=on)
        offstrike.configure(text=off)
        overslbl.configure(text=str(int(balls / 6)) + "." + str(balls % 6))
        flag = 1


def bold():
    global score, wic, balls, on, off, count, flag, qq
    if flag:
        qq = "bold"
        runlbl.configure(text=qq)
        wic += 1
        if (wic >= n - 1):
            inng()
        on = t[count]
        count += 1
        flag = 1
        scorelbl.configure(text=tp + "-   " + str(score))
        wiclbl.configure(text=wic)
        onstrike.configure(text=on)
        offstrike.configure(text=off)
        overslbl.configure(text=str(int(balls / 6)) + "." + str(balls % 6))
        flag = 1


def lbw():
    global score, wic, balls, on, off, count, flag, qq
    if flag:
        qq = "lbw"
        runlbl.configure(text=qq)
        wic += 1
        if (wic >= n - 1):
            inng()
        on = t[count]
        count += 1
        flag = 1
        print(score)
        scorelbl.configure(text=tp + "-   " + str(score))
        wiclbl.configure(text=wic)
        onstrike.configure(text=on)
        offstrike.configure(text=off)
        overslbl.configure(text=str(int(balls / 6)) + "." + str(balls % 6))
        flag = 1


def inng():
    global score, wic, balls, on, off, t2, team2, t, tp, team1, t1, qq, flag
    qq = "innings complete"
    runlbl.configure(text=qq)
    tp = team2
    t = t2
    count = 2
    on = t[0]
    off = t[1]
    score = 0
    balls = 0
    wic = 0
    scorelbl.configure(text=tp + "-   " + str(score))
    wiclbl.configure(text=wic)
    onstrike.configure(text=on)
    offstrike.configure(text=off)
    overslbl.configure(text=str(int(balls / 6)) + "." + str(balls % 6))
    flag = 1


root = Tk()
root.title("cricscore")
root.configure(bg="White")
heading = Label(root, width=60, text="CRICSCORE", fg="black", bg="LightBlue", font="retro", anchor="center")
heading.pack(side=TOP)

f = Frame(root, height=8, width=20)
f.pack(side=TOP)

runlbl = Label(f, text=update, borderwidth=6, relief="ridge", height=8, width=20, bg="Cyan", fg="Black", font="retro")
runlbl.pack(side=LEFT)

f1 = Frame(f, height=8, width=20)
f1.pack(side=LEFT)

f0 = Frame(f1, height=4, width=20)
f0.pack(side=TOP)
scorelbl = Label(f0, text=tp + "-  " + str(score), borderwidth=4, relief="groove", height=4, width=15, bg="white",
                 fg="Black", font="retro")
scorelbl.pack(side=LEFT)
wiclbl = Label(f0, text=wic, borderwidth=4, relief="groove", height=4, width=5, bg="white", fg="Black", font="retro")
wiclbl.pack(side=LEFT)
onstrike = Label(f1, text=on, borderwidth=4, relief="groove", height=4, width=21, bg="white", font="retro")
onstrike.pack(side=TOP)

f2 = Frame(f, height=8, width=20)
f2.pack(side=LEFT)
overslbl = Label(f2, text=str(int(balls / 6)) + "." + str(balls % 6), borderwidth=4, relief="groove", height=4,
                 width=20, bg="white", fg="Black", font="retro")
overslbl.pack(side=TOP)
offstrike = Label(f2, text=off, borderwidth=4, relief="groove", height=4, width=20, bg="white", font="retro")
offstrike.pack(side=TOP)

f3 = Frame(root, height=8, width=20)
f3.pack(side=TOP)

b0 = Button(f3, text="DOT", borderwidth=1, relief="groove", height=4, width=9, bg="LightBlue", font="retro",
            command=score0)
b0.pack(side=LEFT)
b1 = Button(f3, text="1", borderwidth=1, relief="groove", height=4, width=10, bg="LightBlue", font="retro",
            command=score1)
b1.pack(side=LEFT)
b2 = Button(f3, text="2", borderwidth=1, relief="groove", height=4, width=10, bg="LightBlue", font="retro",
            command=score2)
b2.pack(side=LEFT)
b3 = Button(f3, text="3", borderwidth=1, relief="groove", height=4, width=10, bg="LightBlue", font="retro",
            command=score3)
b3.pack(side=LEFT)
b4 = Button(f3, text="4", borderwidth=1, relief="groove", height=4, width=10, bg="LightBlue", font="retro",
            command=score4)
b4.pack(side=LEFT)
b6 = Button(f3, text="6", borderwidth=1, relief="groove", height=4, width=10, bg="LightBlue", font="retro",
            command=score6)
b6.pack(side=LEFT)

f4 = Frame(height=8, width=20)
f4.pack(side=TOP)

bnb = Button(f4, text="no ball", borderwidth=1, relief="groove", height=4, width=12, bg="LightBlue", font="retro",
             command=noball)
bnb.pack(side=LEFT)
bwide = Button(f4, text="wide", borderwidth=1, relief="groove", height=4, width=12, bg="LightBlue", font="retro",
               command=wide)
bwide.pack(side=LEFT)
bfreehit = Button(f4, text="free hit", borderwidth=1, relief="groove", height=4, width=12, bg="LightBlue", font="retro",
                  command=freehit)
bfreehit.pack(side=LEFT)
bover = Button(f4, text="over up", borderwidth=1, relief="groove", height=4, width=12, bg="LightBlue", font="retro",
               command=over)
bover.pack(side=LEFT)
binng = Button(f4, text="innings up", borderwidth=1, relief="groove", height=4, width=12, bg="LightBlue", font="retro",
               command=inng)
binng.pack(side=LEFT)

f5 = Frame(height=8, width=20)
f5.pack(side=TOP)

bonrunout = Button(f5, text="on-runout", borderwidth=1, relief="groove", height=4, width=12, bg="LightBlue",
                   font="retro", command=onrunout)
bonrunout.pack(side=LEFT)
boffrunout = Button(f5, text="off-runout", borderwidth=1, relief="groove", height=4, width=12, bg="LightBlue",
                    font="retro", command=offrunout)
boffrunout.pack(side=LEFT)
bhitwic = Button(f5, text="bold", borderwidth=1, relief="groove", height=4, width=12, bg="LightBlue", font="retro",
                 command=bold)
bhitwic.pack(side=LEFT)
bcatch = Button(f5, text="catch", borderwidth=1, relief="groove", height=4, width=12, bg="LightBlue", font="retro",
                command=catch)
bcatch.pack(side=LEFT)
blbw = Button(f5, text="lbw", borderwidth=1, relief="groove", height=4, width=12, bg="LightBlue", font="retro",
              command=lbw)
blbw.pack(side=LEFT)

root.mainloop()
