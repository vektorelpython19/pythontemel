<<<<<<< HEAD
import tkinter as tk
pencere = tk.Tk()
pencere.mainloop()
=======
import random as rnd
metin = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec elementum vestibulum volutpat. Nullam cursus placerat purus, quis ultrices lacus pretium at. Nullam interdum auctor arcu, in blandit turpis tristique ac. Vestibulum tristique lacinia cursus. Vivamus aliquet feugiat ante. Suspendisse elementum hendrerit arcu sit amet pulvinar. Cras tempus volutpat dignissim. Donec non libero vitae felis porta ultricies. Cras tincidunt ante et elit egestas viverra. Maecenas nunc ante, ornare vitae ligula ac, malesuada vestibulum massa. Curabitur viverra, risus eu hendrerit vehicula, eros elit maximus velit, et dictum felis felis quis ex. Duis justo nisl, semper eu feugiat vel, suscipit eget purus. Nunc elementum convallis pretium. Suspendisse tincidunt lacus augue, ut vehicula libero blandit eu.
Sed purus lorem, congue eu tempor in, suscipit sit amet lectus. In semper egestas aliquam. Morbi iaculis lorem in lorem tincidunt, in pretium mi tempor. Etiam non mi convallis, maximus nunc sollicitudin, vestibulum elit. Pellentesque semper mi placerat arcu hendrerit molestie. Aenean et nunc nibh. Duis quis libero id ligula tincidunt eleifend id id nibh. Mauris euismod vehicula nibh et vestibulum.
"""
for i in range(50):
    print(metin[rnd.randint(0,len(metin)):rnd.randint(0,len(metin))],rnd.randint(0,5),sep=";",end="\n",file=open("defter.csv","r+"))
>>>>>>> fe9e0b3f730bc18d1cb6949471b7f1ed5de56ef2
