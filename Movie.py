



######################################################################################################################################
######################################################################################################################################
## # CODE LANGUAGE IS PYHTON!                                                        ##      ##                                     ##
## # DATE: 19-JULY-2021                                                              ##      ##   ########   ##          ##     ##  ##
## # CODE BY HANU!                                                                   ##########         ##   #########   ##     ##  ##
## # ONLY FOR EDUCATIONAL PURPOSE!                                                   ##########    #######   ##     ##   ##     ##  ##
## # Movie Discriptor MAIN!                                                          ##      ##    ##   ##   ##     ##   ##     ##  ##
## # ITS ONLY DEMO!                                                                  ##      ##    #######   ##     ##   #########  ##
######################################################################################################################################
######################################################################################################################################

import tkinter
from tkinter import *
import imdb
import tkinter.messagebox as tmsg
    #Functions


    # define function for View Help
def Help():
    tmsg.showerror("Help", "Please Insure Your Network Connection\nMust Be Stable.")


    # define function for about!
def about():
    tmsg.showerror("About", "Movie Info By Hanu.. \nVersion 1.1"
                            "\nYou Can Get All Basic Inforamation About All Movies."
                            "\nCopy Right 2021 Hanu Corporation. "
                            "All Right Reserved!"
                            " For All OS {Windows}, {Linux}, {MacOS}"
                            " User Interface Are Protected By Trademark"
                            " And Other Pendings"
                            " Or Existing Intellecutal Property Right In "
                            " United State And Other Countries.")

def Exit():
        root.destroy()

    # define function for Next version
def Next_version():
    tmsg.showwarning("Info", " Go To ->Github.com/HorridHanu<- \n For More Update And Versions....")




    # define function for search
def Search():

    if Movie_Entry.get() == "":
        tmsg.showerror("Error", "Please enter a movie name.")

    else:
        root1 = Toplevel()
        root1.geometry("800x500+100+160")
        root1.title("Movie Info..")
        root1.config(bg="orange")
        root1.resizable(0, 0)

        Title = Label(root1, text='* Title :', font=('cooper black', 30, 'bold'), fg="white", bg="orange")
        Title.place(x=60, y=20)

        Title_Name = Label(root1, font=('algerian', 25, 'bold'), fg="white", bg="orange")
        Title_Name.place(x=350, y=20)



        Director = Label(root1, text='* Director :', font=('cooper black', 30, 'bold'), fg="white", bg="orange")
        Director.place(x=60, y=90)

        Director_Name = Label(root1, font=('algerian', 25, 'bold'), fg="white", bg="orange")
        Director_Name.place(x=350, y=90)



        Year = Label(root1, text='* Year :', font=('cooper black', 30, 'bold'), fg="white", bg="orange")
        Year.place(x=60, y=160)

        Year_Name = Label(root1, text='', font=('algerian', 20, 'bold'), fg="white", bg="orange")
        Year_Name.place(x=350, y=160)



        Runtime = Label(root1, text='* Runtime :', font=('cooper black', 30, 'bold'), fg="white", bg="orange")
        Runtime.place(x=60, y=220)

        Runtime_Name = Label(root1, text='', font=('algerian', 20, 'bold'), fg="white", bg="orange")
        Runtime_Name.place(x=350, y=220)



        Genres= Label(root1, text='* Genres :', font=('cooper black', 30, 'bold'), fg="white", bg="orange")
        Genres.place(x=60, y=280)

        Genres_Name = Label(root1, text='', font=('algerian', 20, 'bold'), fg="white", bg="orange")
        Genres_Name.place(x=350, y=280)



        Rating = Label(root1, text='* Rating :', font=('cooper black', 30, 'bold'), fg="white", bg="orange")
        Rating.place(x=60, y=340)

        Rating_Name = Label(root1, text='', font=('algerian', 20, 'bold'), fg="white", bg="orange")
        Rating_Name.place(x=350, y=340)



        Cast = Label(root1, text='* Cast :', font=('cooper black', 30, 'bold'), fg="white", bg="orange")
        Cast.place(x=60, y=400)

        Cast_Name = Label(root1, text='', font=('algerian', 20, 'bold'), fg="white", bg="orange", wraplength=612, justify=LEFT)
        Cast_Name.place(x=350, y=400)


        imdbObject = imdb.IMDb()
        Movie_name = Movie_Entry.get()
        Movies = imdbObject.search_movie(Movie_name)
        Index = Movies[0].getID()
        Movie = imdbObject.get_movie(Index)



        title = Movie['title']
        Title_Name.config(text=title)




        for director in Movie['director']:
            Director_Name.config(text=director)



        year = Movie['year']
        Year_Name.config(text=year)



        for runtime in Movie['runtime']:
            Hours = int(runtime)//60
            Minutes = int(runtime) % 60
            Runtime_Name.config(text=f"{Hours} hour {Minutes} minutes")



        genres = Movie['genre']
        Genres_Name.config(text=genres)



        rate = Movie['rating']
        Rating_Name.config(text=rate)



        cast = Movie['cast']
        castlist = list(map(str, cast))
        Slicelist = castlist[:10]
        strr = ''
        for i in Slicelist():
            if i==Slicelist[9]:
                strr = strr+i+'.'
            else:
                strr = strr+i+", "
        Cast_Name.config(text=strr)


        root1.mainloop()


root = Tk()
root.geometry("930x1000+40+10")
root.title("Movie Info")
root.resizable(0, 0)
root.bell()
image = PhotoImage(file='Source/search.png')
root.iconphoto(False, image)

bgpic = PhotoImage(file="Source/pic.png")
bglabel = Label(root, image=bgpic)
bglabel.place(x=0, y=0)

Movie_label = Label(root, text="Movie Name:", font=('algerian 30 bold'), bg="#E5E3E4")
Movie_label.place(x=70, y=570)

Movie_Entry = Entry(root, font=('FELIX TITLING', 20, 'bold'), bd=5, relief=GROOVE, justify=CENTER)
Movie_Entry.place(x=370, y=577)
Movie_Entry.focus_set()

SearchButton_icon = PhotoImage(file='Source/search.png')
SearchButton = Button(root, image=SearchButton_icon, bd=3, relief=GROOVE, command=Search)
SearchButton.place(x=800, y=580)



    #Main Menu!

    # Icons
about_icon = PhotoImage(file='Source/about.png')
Version_icon = PhotoImage(file='Source/ver.png')
Help_icon = PhotoImage(file='Source/help.png')
Exit_icon = PhotoImage(file='Source/exit.png')


    # Submenu View Help
mainmenu = Menu(root)
m5 = Menu(mainmenu, tearoff=0)


    # Veiw Help
m5.add_command(label="View Help", command=Help, image=Help_icon, compound=tkinter.LEFT)

    # next version
m5.add_command(label="Next Version..", command=Next_version, image=Version_icon, compound=tkinter.LEFT)
# m5.add_separator()

    # about
m5.add_command(label="About", command=about, image=about_icon, compound=tkinter.LEFT)
m5.add_separator()
    # Exit
m5.add_command(label='Exit', command=Exit, image=Exit_icon, compound=tkinter.LEFT)

mainmenu.add_cascade(label="Help", menu=m5)


    # View help menu END

root.config(menu=mainmenu)    #configure the mainmenu as menu

root.mainloop()



######################################################################################################################################
######################################################################################################################################
                                                                                                                                    ##
###########                                                                                                                         ##
##                                                                                                                                  ##
##               ##                     ##                                                                                          ##
#########        ##########             ##                                                                                          ##
#########        ##########      #########                                                                                          ##
##               ##      ##      ##     ##                                                                                          ##
##               ##      ##      ##     ##                                                                                          ##
###########      ##      ##      #########  ## ## ##                                                                                ##
                                                                                                                                    ##
######################################################################################################################################
######################################################################################################################################
