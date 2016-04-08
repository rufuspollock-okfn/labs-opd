import os.path

from browser.models import Brand_owner, Brand_owner_img

def run():

    #list_gtin = Gtin.objects.filter(GTIN_CD__startswith = '083609')
    list_Owner = Brand_owner.objects.all().order_by('OWNER_CD')
    for Ownerobj in list_Owner:
        OWNER_CD = Ownerobj.OWNER_CD
        img_path_base = 'C:/Users/Philippe/media/Owner/';

        img_name = str(OWNER_CD).zfill(6) + '.jpg'

        img_path_full = img_path_base + img_name

        if os.path.isfile(img_path_full):
            #with open(img_path_full, "rb") as image_file:
                #filedata = base64.b64encode(image_file.read())
                #filedata = image_file.encode("base64")

            f = open(img_path_full,'rb')
            filedata = f.read()
            f.close()

            print (img_name  + ' OK')

            if Brand_owner_img.objects.filter(pk=str(OWNER_CD)).exists():
                current_OWNER_CD = Brand_owner_img.objects.get(pk=str(OWNER_CD))
                current_OWNER_CD.Brand_owner_img = filedata
                current_OWNER_CD.save()
            else:
                new_entry = Brand_owner_img(OWNER_CD = str(OWNER_CD), OWNER_IMG= filedata)
                new_entry.save()


            #Gtin_img.objects.create(GTIN_CD = str(gtin) , GTIN_IMG = filedata )
        else:
            print (img_name  + ' :(' + img_path_full)
