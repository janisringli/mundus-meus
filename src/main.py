from turtle import *
color('red', 'yellow')
begin_fill()
while True:
    forward(250)
    left(200)
    if abs(pos()) < 1:
        break
end_fill()
done()
