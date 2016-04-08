from .models import Gtin, Brand, Brand_type, Gs1_gpc
from rest_framework import serializers
from django.conf import settings


class BrandSerializer(serializers.HyperlinkedModelSerializer):

    code = serializers.SerializerMethodField()
    name = serializers.SerializerMethodField()
    img = serializers.SerializerMethodField()
    link = serializers.SerializerMethodField()

    class Meta:
        model = Brand
        fields = ('code', 'name','link','img')

    def get_code(self, obj):
        return obj.BSIN

    def get_name(self, obj):
        return obj.BRAND_NM

    def get_link(self, obj):
        return obj.BRAND_LINK

    def get_img(self, obj):
        result = ""
        if obj.BSIN:
            result = settings.MEDIA_URL + "brand/" + obj.BSIN + ".jpg"
        else:
            result = ""
        return result

class GPC_S_Serializer(serializers.HyperlinkedModelSerializer):
    code = serializers.SerializerMethodField()
    name = serializers.SerializerMethodField()
    img = serializers.SerializerMethodField()
    class Meta:
        model = Gs1_gpc
        fields = ('code', 'name','img')

    def get_code(self, obj):
        return obj.GPC_CD

    def get_name(self, obj):
        return obj.GPC_NM

    def get_img(self, obj):
        result = ""
        if obj.GPC_CD:
            result = settings.MEDIA_URL + "gpc/" + str(obj.GPC_CD) + ".jpg"
        else:
            result = ""
        return result

class GPC_F_Serializer(serializers.HyperlinkedModelSerializer):
    code = serializers.SerializerMethodField()
    name = serializers.SerializerMethodField()

    class Meta:
        model = Gs1_gpc
        fields = ('code', 'name')

    def get_code(self, obj):
        return obj.GPC_CD

    def get_name(self, obj):
        return obj.GPC_NM

class GPC_C_Serializer(serializers.HyperlinkedModelSerializer):
    code = serializers.SerializerMethodField()
    name = serializers.SerializerMethodField()

    class Meta:
        model = Gs1_gpc
        fields = ('code', 'name')

    def get_code(self, obj):
        return obj.GPC_CD

    def get_name(self, obj):
        return obj.GPC_NM

class GPC_B_Serializer(serializers.HyperlinkedModelSerializer):
    code = serializers.SerializerMethodField()
    name = serializers.SerializerMethodField()

    class Meta:
        model = Gs1_gpc
        fields = ('code', 'name')

    def get_code(self, obj):
        return obj.GPC_CD

    def get_name(self, obj):
        return obj.GPC_NM

class GCP_Serializer(serializers.HyperlinkedModelSerializer):
    code = serializers.SerializerMethodField()
    name = serializers.SerializerMethodField()
    address_1 = serializers.SerializerMethodField()
    address_2 = serializers.SerializerMethodField()
    address_3 = serializers.SerializerMethodField()
    cp = serializers.SerializerMethodField()
    city = serializers.SerializerMethodField()
    country = serializers.SerializerMethodField()

    class Meta:
        model = Gs1_gpc
        fields = ('code', 'name','address_1','address_2','address_3','cp','city','country')

    def get_code(self, obj):
        return obj.GLN_CD

    def get_name(self, obj):
        return obj.GLN_NM

    def get_address_1(self, obj):
        return obj.GLN_ADDR_02

    def get_address_2(self, obj):
        return obj.GLN_ADDR_03

    def get_address_3(self, obj):
        return obj.GLN_ADDR_04

    def get_cp(self, obj):
        return obj.GLN_ADDR_POSTALCODE

    def get_city(self, obj):
        return obj.GLN_ADDR_CITY

    def get_country(self, obj):
        return obj.GLN_COUNTRY_ISO_CD

class GtinSerializer(serializers.HyperlinkedModelSerializer):

    code = serializers.SerializerMethodField()
    name = serializers.SerializerMethodField()
    product_line = serializers.SerializerMethodField()
    weight = serializers.SerializerMethodField()
    volume = serializers.SerializerMethodField()
    alcohol = serializers.SerializerMethodField()
    img = serializers.SerializerMethodField()

    BSIN = BrandSerializer(many=False, read_only=True)
    GPC_S_CD = GPC_S_Serializer(many=False, read_only=True)
    GPC_F_CD = GPC_F_Serializer(many=False, read_only=True)
    GPC_C_CD = GPC_C_Serializer(many=False, read_only=True)
    GPC_B_CD = GPC_B_Serializer(many=False, read_only=True)
    GCP_CD = GCP_Serializer(many=False, read_only=True)

    class Meta:
        model = Gtin
        fields = ('code', 'name','product_line','BSIN','weight','volume','alcohol','img','GPC_S_CD', 'GPC_F_CD','GPC_C_CD','GPC_B_CD','GCP_CD')

    def get_name(self, obj):
        return obj.GTIN_NM

    def get_code(self, obj):
        return obj.GTIN_CD

    def get_product_line(self, obj):
        return obj.PRODUCT_LINE

    def get_weight(self, obj):
        result = ""
        if obj.M_G:
            if obj.M_G >= 1000:
                result = str(obj.PKG_UNIT) + " x " + str(obj.M_G/1000) +  " kg"
            else:
                result = str(obj.PKG_UNIT) + " x " + str(obj.M_G) + " g"
            if obj.M_OZ:
                result += " / "
        elif obj.M_OZ:
            result += str(obj.PKG_UNIT) + " x " + str(obj.M_OZ) + " oz"
        else:
            result += ""
        return result

    def get_volume(self, obj):
        result = ""
        if obj.M_ML:
            if obj.M_ML >= 1000:
                result = str(obj.PKG_UNIT) + " x " + str(obj.M_ML/1000) +  " l"
            else:
                result = str(obj.PKG_UNIT) + " x " + str(obj.M_ML) +  " ml"
            if obj.M_FLOZ:
                result += " / "
        elif obj.M_FLOZ:
            result += str(obj.PKG_UNIT) + " x " + str(obj.M_FLOZ) + " floz"
        else:
            result += ""
        return result

    def get_alcohol(self, obj):
        result = ""
        if obj.M_ABV:
            result = str(obj.M_ABV) + " % vol."
        elif obj.M_ABW:
            result = str(obj.M_ABW) + " % vol."
        else:
            result = ""
        return result

    def get_img(self, obj):
        result = ""
        if obj.GTIN_CD:
            result = settings.MEDIA_URL + "gtin/gtin-" + obj.GTIN_CD[:3] + "/" + obj.GTIN_CD + ".jpg"
        else:
            result = ""
        return result
