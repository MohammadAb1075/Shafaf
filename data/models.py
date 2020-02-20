from django.db import models


class Cost(models.Model):
    topic                     = models.TextField( null=False, blank=False)#mozou
    contractorName            = models.CharField(max_length=127, null=True, blank=True)#peyman kar
    client                    = models.CharField(max_length=127, null=True, blank=True)#karfarma
    finalAmount               = models.CharField(max_length=127, null=True, blank=True)#mabkagh_nahayi
    cStartDate                = models.DateField(null=True, blank=True)#tarikh_eneghad
    bossName                  = models.CharField(max_length=255, null=True, blank=True)#nam_modiramel
    nonCashAmount             = models.CharField(max_length=255, null=True, blank=True)#mablagh gheyrnaghd
    cashAmount                = models.CharField(max_length=255, null=True, blank=True)#mablagh naghad
    terminationContractDetail = models.CharField(max_length=255, null=True, blank=True)#etelaat faskh gharardad
    additionDetail            = models.CharField(max_length=255, null=True, blank=True)#etelaat elhaghiye
    cDuration                 = models.CharField(max_length=255, null=True, blank=True)#modat gharardad
    cSelect                   = models.CharField(max_length=255, null=True, blank=True)#ravesh entekhab peyman
    cNationalId               = models.CharField(max_length=255, null=True, blank=True)#shenasnameh meli peyman
    cEconomicId               = models.CharField(max_length=255, null=True, blank=True)#code eghtesadi peyman
    cId                       = models.CharField(max_length=255, null=True, blank=True)#code melli
    cBirthday                 = models.CharField(max_length=255, null=True, blank=True)#tarikh tavalod
    reasonLeave               = models.CharField(max_length=255, null=True, blank=True)#ellat tark tashrifat
    hasTax                    = models.BooleanField()#maliyat bar arzesh efzoude?
    startDate                 = models.DateField(null=True, blank=True)#tarikh shoroo
    endDate                   = models.DateField(null=True, blank=True)#tarikh Payan
    moderator                 = models.CharField(max_length=255, null=True, blank=True)#nazer
    winMethod                 = models.CharField(max_length=255, null=True, blank=True)#ravesh taeen barandeh
    memberCommision           = models.TextField(null=True, blank=True)#aazaye kommision
    signClient                = models.CharField(max_length=255, null=True, blank=True)#emzakonande gharardad az tarf karfarma


class Income(models.Model):
    topic                     = models.TextField() #mozo
    beneficiary               = models.CharField(max_length=127) #bahrebardar
    client                    = models.CharField(max_length=127)#karfarma
    finalAmount               = models.CharField(max_length=127)#mabkagh_nahayi
    cStartDate                = models.DateField()#tarikh_eneghad
    bossName                  = models.CharField(max_length=255)#nam_modiramel
    signClient                = models.CharField(max_length=255)#emzakonande gharardad az taraf bahrebardar
    terminationContractDetail = models.CharField(max_length=255, null=True, blank=True)#etelaat faskh gharardad
    additionDetail            = models.CharField(max_length=255, null=True, blank=True)#etelaat elhaghiye
    cDuration                 = models.CharField(max_length=255)#modat gharardad
    cSelectMethod             = models.CharField(max_length=255)#ravesh entekhab taraf gharardad
    kNationalId               = models.CharField(max_length=255)#shenasnameh meli bahrebardar
    kEconomicId               = models.CharField(max_length=255)#code eghtesadi bahrebardar
    kId                       = models.CharField(max_length=255, null=True, blank=True)#code melli
    kBirthday                 = models.CharField(max_length=255, null=True, blank=True)#tarikh tavalod
    hasTax                    = models.BooleanField()#maliyat bar arzesh afzoodeh
    startDate                 = models.DateField(null=True, blank=True)#tarikh shoroo
    endDate                   = models.DateField(null=True, blank=True)#tarikh Payan
    moderator                 = models.CharField(max_length=255)#nazer
    winMethod                 = models.CharField(max_length=255, null=True, blank=True)#ravesh taeen barandeh
    memberCommision           = models.TextField()#aazaye comision
    signClient                = models.CharField(max_length=255)#emzakonande az taraf kar farma

class Participatory(models.Model):
    topic                 = models.TextField() #mozo
    nameInvestor          = models.CharField(max_length=127) #sarmaye gozar
    beneficiary           = models.CharField(max_length=127)#zinaf
    cOveral               = models.CharField(max_length=127, null=True, blank=True)#baravord koli gharardad
    cStartDate            = models.DateField()#tarikh_eneghad
    projectName           = models.CharField(max_length=127, null=True, blank=True)#name proje
    useri                 = models.CharField(max_length=127, null=True, blank=True)#karbari
    brMucipallity         = models.CharField(max_length=127, null=True, blank=True)#avarde shahrdari
    INationalId           = models.CharField(max_length=255)#shenasnameh sarmayegozar
    IEconomicId           = models.CharField(max_length=255)#code eghtesadi sarmayegozar
    IId                   = models.CharField(max_length=255, null=True, blank=True)#code melli sarmayegozar
    brInverstor           = models.CharField(max_length=127, null=True, blank=True)#avarde sarmayegozar
    estimateOperationTime = models.CharField(max_length=127, null=True, blank=True)#baravord zaman barebardari
    partenrshipModel      = models.CharField(max_length=127, null=True, blank=True)#model gharardad mosharekat
    projectAddress        = models.TextField(max_length=127, null=True, blank=True)#address proje
    startDate             = models.DateField(null=True, blank=True)#tarikh shoroo
    endDate               = models.DateField(null=True, blank=True)#tarikh Payan
    signClient            = models.CharField(max_length=255)#emzakonande az taraf kar farma
    bossName              = models.CharField(max_length=255)#nam_modiramel
    cModerator            = models.CharField(max_length=255)#nazer gharardad
    trustee               = models.TextField(max_length=127, null=True, blank=True)#motevalli
