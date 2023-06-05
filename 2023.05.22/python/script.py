def tryInt(txtInp,txtErr,min,max,empt):
  while True:
    try:
      uint = int(input(txtInp))
      if uint >= min and uint <= max:
        return uint
      else:
        print(txtErr)
    except:
      if not empt:
        print("Hiba, számértéket adjon meg!")
      else:
        return ""

class munkavallalo():
  def __init__(self,Nev,FizKat,EvesSzabadsag):
    self.Nev = Nev
    self.FizKat = FizKat
    self.EvesSzabadsag = EvesSzabadsag

  def KivehetoSzabi(self):
    evesSzab = self.EvesSzabadsag
    if len(str(evesSzab)) > 0:
      eddigKiv = tryInt("Adja meg az eddig kivett szabadnapok számát: ","Hány nap van egy évben?",0,366,False)
      if evesSzab >= eddigKiv:
        print("A munkavállalónak "+str(evesSzab-eddigKiv)+" kivehető szabadnapja maradt.")
      else:
        print("Az eddig kivett szabadságok száma nagyobb, mint az évente megengedett szabadnapok száma.\nA munkavállaló "+str(abs(evesSzab-eddigKiv))+" nappal több szabadságot vett ki mint engedett.")
    else:
      print("A munkavállaló éves szabadságának száma nem volt megadva")


munkas = munkavallalo(input("Adja meg a munkavállaló nevét: "),tryInt("Adja meg a munkavállaló fizetési kategóriáját: ","A fizetési kategória 1-5 közötti szám lehet (1 és 5 beleértve)",1,5,False),tryInt("adja meg a munkavállaló éves szabadnapjainak számát: ","Az éves szabadnapok száma 0-365 közötti szám lehet",0,365,True))
munkas.KivehetoSzabi()

