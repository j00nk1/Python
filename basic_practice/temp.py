import turtle as t

t.shape("turtle")
t.reset()

angle = 91

t.bgcolor("black")

t.color("blue")

t.speed(0)

for x in range(2000):
    t.forward(x)
    t.left(angle)
    
#t.clear()