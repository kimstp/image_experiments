import imageio
import zxingcpp
import pathlib
import shutil


inpath = pathlib.Path("/Users/kimstp/Documents/NHMD/data/Entomology/Aslaks_løbebille_kasser/")
output_pathname = "output/"
outpath = pathlib.Path(output_pathname)

list_files = list(inpath.glob("*.jpeg", case_sensitive=False)) + list(inpath.glob("*.jpg", case_sensitive=False))
print(list_files)

for file in list_files:
    print(file)
    if file.match("Studio Session-*"):
        ending = "_top"
    else:
        ending = "_side"

    img = imageio.v2.imread(file)
    barcodes = zxingcpp.read_barcodes(img)
    if len(barcodes) == 0:
        print("Could not find any barcode.")
    else:
        for barcode in barcodes:
            print('Found barcode:'
		        f'\n Text:    "{barcode.text}"'
		        f'\n Format:   {barcode.format}'
		        f'\n Content:  {barcode.content_type}'
		        f'\n Position: {barcode.position}'
                )
            outfile = outpath / pathlib.Path(barcode.text.replace(' ', '_') + ending + ".jpeg")
            print(outfile)
            shutil.copyfile(file, outfile)


