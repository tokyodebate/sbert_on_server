nationals = """AoyamaWomensCup.txt
JPDUWinter.txt
AsianBridge.txt
JUDCOnline.txt
RyosoCup.txt
AsianNovice2Days.txt
JapanBP.txt
Seikei_joint.txt
BPNovice.txt
KCup.txt
Silver.txt
DebateNoSusume.txt
KIDAOpen.txt
SophiaMastersCup.txt
ESUJ.txt
KKCup.txt
SubaruCup.txt
ESUJBiz.txt
KUELAutumn.txt
SunSunCup
ElizabethCup.txt
KUELTournament.txt
SupernovaCup.txt
EvergreenCup.txt
Kansai.txt
TITechCup.txt
FeministOpen.txt
KantoDebateOpen.txt
TheBinaryStarCup.txt
GeminiCup.txt
KeioDebateOpen.txt
ToeiCup.txt
HakataRamenCup.txt
MalaysiaABP.txt
TokyoMini.txt
HamaguchiCup.txt
MomijiCup.txt
TsukushiCup.txt
ICUTournament.txt
NagoyaDebateOpen.txt
UmekoCup.txt
IchoCup.txt
NekoChampionship.txt
WPT.txt
OsawaCup.txt
WakabaCup.txt
JPDUAutumn.txt
PhilosophyOpen.txt
JPDUSpring.txt
PreAustrals.txt
JPDUTournament.txt
QDO.txt""".split("\n")

internationals = """ADI.txt
KoreaIntervarsityDANC.txt
AIDAEasters.txt
MacauAPDO.txt
ANUspring.txt
MalaysiaDO.txt
APUPhilosophyChallenge.txt
MelbourneMini.txt
ASDC.txt
MukarjiMemorialDebate.txt
AUDC.txt
NEADC.txt
AllAsianIntervarsityDC.txt
NEAO.txt
AmsterdamOpen.txt
NTUProAm.txt
AsianBP.txt
OxfordIV.txt
AssumptionThailandDO.txt
PIDC.txt
Australs.txt
SIDO.txt
BorneoBP.txt
SMUHammers.txt
CambridgeIV.txt
SydneyMini.txt
ChinaBP.txt
TaiwanDO.txt
ESUKoreaDC.txt
TayDO.txt
EUDC.txt
UADC.txt
EastAsiaIVIV.txt
VictoriaIV.txt
HKDO.txt
WSDC.txt
HWSRoundRobin.txt
WUDC.txt
IIUMOpen.txt
WUPID.txt
KLOC.txt
others.txt""".split("\n")


buffer = ""
for i, file in enumerate(nationals):
	with open(f"./motions/{file}") as f:
		if i > 0:
			buffer += "\n"
		buffer += f.read()
with open("./data/tsv/nationals.tsv", "w") as f:
	f.write(buffer)

buffer = ""
for i, file in enumerate(internationals):
	with open(f"./motions/International/{file}") as f:
		if i > 0:
			buffer += "\n"
		buffer += f.read()
with open("./data/tsv/internationals.tsv", "w") as f:
	f.write(buffer)
