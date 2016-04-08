from django.db import models

# Gtin contains products with a GTIN-13
class Gtin(models.Model):
    GTIN_CD = models.CharField(max_length=13, primary_key=True)
    GTIN_LEVEL_CD = models.IntegerField(default=0, null=True, blank=True)
    GCP_CD = models.ForeignKey('Gs1_gcp', null=True, blank=True)
    BSIN = models.ForeignKey('Brand', null=True, blank=True)
    GPC_S_CD = models.ForeignKey('Gs1_gpc', null=True, blank=True, related_name='GPC_S_CD')
    GPC_F_CD = models.ForeignKey('Gs1_gpc', null=True, blank=True, related_name='GPC_F_CD')
    GPC_C_CD = models.ForeignKey('Gs1_gpc', null=True, blank=True, related_name='GPC_C_CD')
    GPC_B_CD = models.ForeignKey('Gs1_gpc', null=True, blank=True, related_name='GPC_B_CD')
    GTIN_NM = models.CharField(max_length=255, null=True, blank=True)
    PRODUCT_LINE = models.CharField(max_length=255, null=True, blank=True)
    M_G = models.FloatField(null=True, blank=True)
    M_OZ = models.FloatField(null=True, blank=True)
    M_ML = models.FloatField(null=True, blank=True)
    M_FLOZ = models.FloatField(null=True, blank=True)
    M_ABV = models.FloatField(null=True, blank=True)
    M_ABW = models.FloatField(null=True, blank=True)
    PKG_UNIT = models.IntegerField(default=0, null=True, blank=True)
    PKG_TYPE_CD = models.IntegerField(null=True, blank=True)
    REF_CD = models.CharField(max_length=255, null=True, blank=True)
    SOURCE = models.CharField(max_length=255, null=True, blank=True)
    IMG = models.IntegerField(default=0, null=True, blank=True)
    def __str__(self):
        return self.GTIN_CD

class Brand(models.Model):
    BSIN = models.CharField(max_length=6, primary_key=True)
    BRAND_NM = models.CharField(max_length=255)
    BRAND_TYPE_CD = models.ForeignKey('Brand_type', null=True, blank=True)
    BRAND_LINK = models.CharField(max_length=255, null=True, blank=True)
    OWNER_CD = models.ForeignKey('Brand_owner', null=True, blank=True)
    def __str__(self):
        return self.BSIN

class Brand_type(models.Model):
    BRAND_TYPE_CD = models.IntegerField(primary_key=True)
    BRAND_TYPE_NM = models.CharField(max_length=255, null=True, blank=True)
    def __str__(self):
        return self.BRAND_TYPE_NM

class Nutrition(models.Model):
    GTIN_CD  = models.OneToOneField(
        Gtin,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    INGREDIENTS = models.TextField(null=True, blank=True)
    SERV_SIZE_G = models.FloatField(null=True, blank=True)
    SERV_SIZE_ML = models.FloatField(null=True, blank=True)
    SERV_CT = models.FloatField(null=True, blank=True)
    CAL = models.FloatField(null=True, blank=True)
    CAL_FROM_FAT = models.FloatField(null=True, blank=True)
    TOT_FAT_G = models.FloatField(null=True, blank=True)
    TOT_FAT_DV = models.FloatField(null=True, blank=True)
    SAT_FAT_G = models.FloatField(null=True, blank=True)
    SAT_FAT_DV = models.FloatField(null=True, blank=True)
    TRANS_FAT_G = models.FloatField(null=True, blank=True)
    CHOL_MG = models.FloatField(null=True, blank=True)
    CHOL_DV = models.FloatField(null=True, blank=True)
    SOD_MG = models.FloatField(null=True, blank=True)
    SOD_DV = models.FloatField(null=True, blank=True)
    POT_MG = models.FloatField(null=True, blank=True)
    POT_DV = models.FloatField(null=True, blank=True)
    TOT_CARB_G = models.FloatField(null=True, blank=True)
    TOT_CARB_DV = models.FloatField(null=True, blank=True)
    DIET_FIBER_G = models.FloatField(null=True, blank=True)
    DIET_FIBER_DV = models.FloatField(null=True, blank=True)
    SUGARS_G = models.FloatField(null=True, blank=True)
    PROTEIN_G = models.FloatField(null=True, blank=True)
    VITAMIN_A = models.FloatField(null=True, blank=True)
    VITAMIN_C = models.FloatField(null=True, blank=True)
    CALCIUM = models.FloatField(null=True, blank=True)
    IRON = models.FloatField(null=True, blank=True)
    SOURCE = models.TextField(null=True, blank=True)
    SYNC_DT = models.DateField(null=True, blank=True)

class Gs1_gpc(models.Model):
    GPC_LANG = models.CharField(max_length=3)
    GPC_CD = models.CharField(max_length=20, primary_key=True)
    GPC_NM = models.TextField()
    GPC_LEVEL = models.CharField(max_length=1)
    SOURCE = models.CharField(max_length=255)

class Gs1_gpc_hier(models.Model):
    GPC_S_CD = models.CharField(max_length=8)
    GPC_F_CD = models.CharField(max_length=8)
    GPC_C_CD = models.CharField(max_length=8)
    GPC_B_CD = models.CharField(max_length=8, primary_key=True)

class Brand_owner(models.Model):
    OWNER_CD = models.IntegerField(primary_key=True)
    OWNER_NM = models.CharField(max_length=255, null=True, blank=True)
    OWNER_LINK = models.CharField(max_length=255, null=True, blank=True)
    OWNER_WIKI_EN = models.CharField(max_length=255, null=True, blank=True)

class Gs1_gcp(models.Model):
    GCP_CD = models.CharField(max_length=13, primary_key=True)
    GLN_CD = models.CharField(max_length=13)
    GLN_NM = models.CharField(max_length=255)
    GLN_ADDR_02 = models.CharField(max_length=38)
    GLN_ADDR_03 = models.CharField(max_length=38)
    GLN_ADDR_04 = models.CharField(max_length=38)
    GLN_ADDR_POSTALCODE = models.CharField(max_length=38)
    GLN_ADDR_CITY = models.CharField(max_length=38)
    GLN_COUNTRY_ISO_CD = models.CharField(max_length=38)
    CONTACT_NAME = models.CharField(max_length=38)
    CONTACT_TEL = models.CharField(max_length=255)
    CONTACT_HOTLINE = models.CharField(max_length=255, null=True, blank=True)
    CONTACT_FAX = models.CharField(max_length=255)
    CONTACT_MAIL = models.CharField(max_length=255)
    CONTACT_WEB = models.CharField(max_length=255)
    GLN_LAST_CHANGE = models.CharField(max_length=10)
    GLN_PROVIDER = models.CharField(max_length=13)
    SEARCH_GTIN_CD = models.CharField(max_length=13)
    GEPIR_GCP_CD = models.CharField(max_length=13)
    ADD_PARTY_ID = models.CharField(max_length=13)
    RETURN_CODE = models.ForeignKey('Gs1_gcp_rc', null=True, blank=True)
    SOURCE = models.CharField(max_length=100)
    SYNC_DT = models.DateField(null=True, blank=True)
    def __str__(self):
        return self.GCP_CD

class Gs1_gcp_rc(models.Model):
    RETURN_CODE = models.CharField(max_length=3, primary_key=True)
    RETURN_NAME = models.CharField(max_length=255)
    ORIGIN = models.CharField(max_length=255)

# Search is used to store gtin that people are searching and the number of times it has been searched
class Search(models.Model):
    GTIN_CD = models.CharField(max_length=13, primary_key=True)
    SEARCH_NB =  models.IntegerField(default=1)

# same but for the API
class Search_api(models.Model):
    GTIN_CD = models.CharField(max_length=13, primary_key=True)
    SEARCH_NB =  models.IntegerField(default=1)
