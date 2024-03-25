import turtle

t = turtle
t.shape('turtle')

# Архимедова спираль: ro=k*fi
k = 1
fi_degr = 0.1*(180/3.14)

while True:
    fi_rad = 0.1
    for i in range(300):
        ro = k*fi_rad
        t.forward(ro)
        t.left(fi_degr)
        fi_rad += 0.1
    t.reset()
