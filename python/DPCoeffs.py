

a = .5

### DP54 ###

b1 = (157015080*a**4 - 13107642775*a**3 + 34969693132*a**2 - 32272833064*a+ 11282082432)/11282082432
b2=0

b3 =-100*a*(15701508*a**3 - 914128567*a**2 + 2074956840*a- 1323431896)/32700410799

b4 =25*a*(94209048*a**3 - 1518414297*a**2 + 2460397220*a - 889289856)/5641041216

b5 = -2187*a*(52338360*a**3 - 451824525*a**2 + 687873124*a - 259006536)/199316789632

b6 =11*a*(106151040*a**3 - 661884105*a**2 + 946554244*a - 361440756)/2467955532

b7 = a*(1 - a)*(8293050*a**2 - 82437520*a + 44764047)/29380423

dp_54bs = [b1,b2,b3,b4,b5,b6,b7]

print("################# DP54 ###########################")

for b in dp_54bs:
    print("{0:.16f}".format(b))
print("SUM ",sum(dp_54bs))

print("################# DP87 ###########################")


b1 = -6.3448349392860401388*a**5 + 22.1396504998094068976*a**4 - 30.0610568289666450593*a**3 + 19.9990069333683970610*a**2- 6.6910181737837595697*a + 1.0
b2 =0
b3 =0
b4 =0
b5 =0
b6 = -39.6107919852202505218*a**5 + 116.4422149550342161651*a**4- 121.4999627731334642623*a**3 + 52.2273532792945524050*a**2- 7.6142658045872677172*a

b7 =20.3761213808791436958*a**5 - 67.1451318825957197185*a**4+ 83.1721004639847717481*a**3 - 46.8919164181093621583*a**2 + 10.72813926304288661240*a

b8 =7.3347098826795362023*a**5 -16.5672243527496524646*a**4+ 9.5724507555993664382*a**3 - 0.1890893225010595467*a**2 +0.5526637063753648783*a

b9 = 32.8801774352459155182*a**5 - 89.9916014847245016028*a**4+ 87.8406057677205645007*a**3 - 35.7075975946222072821*a**2+ 4.2186562625665153803*a

b10 =- 10.1588990526426760954*a**5 + 22.6237489648532849093*a**4- 17.4152107770762969005*a**3+6.2736448083240352160*a**2- 0.6627209125361597559*a

b11 = - 12.5401268098782561200*a**5 + 32.2362340167355370113*a**4- 28.5903289514790976966*a**3 + 10.3160881272450748458*a**2 - 1.2636789001135462218*a

b12 =29.5553001484516038033*a**5 - 82.1020315488359848644*a**4+81.6630950584341412934*a**3 - 34.7650769866611817349*a**2+5.4106037898590422230*a

b13 = - 41.7923486424390588923*a**5 + 116.2662185791119533462*a**4- 114.9375291377009418170*a**3 + 47.7457971078225540396*a**2- 7.0321379067945741781*a

b14 = 20.3006925822100825485*a**5 - 53.9020777466385396792*a**4+ 50.2558364226176017553*a**3 - 19.0082099341608028453*a**2+ 2.3537586759714983486*a

dp_87bs = [b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14]

for b in dp_87bs:
    print("{0:.16f}".format(b))
print("SUM ",sum(dp_87bs))