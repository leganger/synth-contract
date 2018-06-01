import os, glob
import img2pdf

img_list = glob.glob("output/*.png")

with open("synth_contracts.pdf", "wb") as f:
	f.write(img2pdf.convert(img_list))
