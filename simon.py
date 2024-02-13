from tkinter import*

gruut = Tk()
gruut.geometry("100x900")
gruut.title("SI")

lbl_flow = Label(gruut, text="efgtgvtrvg4")
lbl_series = Label(gruut)
lbl_floww = Label(gruut)

lbl_flow.pack()
lbl_series.pack()
lbl_floww.pack()

def NAZI():
    num = 10
    first_no = 0
    second_no = 1
    sum = 0
    count = 1
    while (count <= num):
        lbl_series["text"] += str(sum) + " "
        count = count + 1
        first_no = second_no
        second_no = sum
        sum = first_no + second_no
    lbl_flow['text'] = "La flor está completamente florecida"
    lbl_floww["text"] = "Los espirales en la dirección derecha son " + str(first_no) + " y los espirales en la dirección izquierda son " + str(second_no) + "\n El total de espirales es " + str(sum)

btn = Button(gruut, text="Mostrar la serie Fibonacci", command=NAZI)
btn.pack()
gruut.mainloop()