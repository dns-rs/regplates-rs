import random
import string

# List of city tags: https://registracija-vozila.rs/105-uncategorised/453-registarske-oznake-u-srbiji
# Plates wiki: https://en.wikipedia.org/wiki/Vehicle_registration_plates_of_Serbia

hyphen = "-"
cityTag = ["AL", "AR", "AC", "BG", "BO", "BP", "BT", "BĆ", "BU", "BČ", "VA", "VB", "VL", "VP", "VR", "VS", "VŠ", "GL", "GM", "DE", "ĐA", "ZA", "ZR", "IN", "IC", "JA", "KA", "KV", "KG", "KŽ", "KI", "KL", "KM", "KO", "KŠ", "LB", "LE", "LO", "LU", "NV", "NG", "NI", "NP", "NS", "PA", "PB", "PE", "PŽ", "PZ", "PI", "PK", "PN", "PO", "PP", "PR", "PT", "RA", "RU", "SA", "SV", "SD", "SM", "SO", "SP", "ST", "SU", "TO", "TS", "TT", "ĆU", "UB", "UE", "UR", "ČA", "ŠA", "ŠI"]
diplomaticTag = ["A", "M", "P", "CMD", "CD"]
specialTag = ["TX", "П", "AGR", "MOPED", "TRAILER", "MILITARY"]
shield = "🛡️ "

def randomString(stringLength):
    letters = string.ascii_uppercase
    return ''.join(random.choice(letters) for i in range(stringLength))

#Standard Plates

print("-----------Standard Plates-----------")

for x in range(10):
    city = random.choice(cityTag)
    number = str(random.randint(0, 9999))
    if int(number) < 100:
        if int(number) < 10:
            number = "00"+number
        else:
            number = "0"+number
        
    end = randomString(2)
    standardPlate = city + shield + number + hyphen + end
    print(standardPlate)

#Diplomatic Plates

print("-----------Diplomatic Plates-----------")

for x in range(10):
    diplFirstNumber = str(random.randint(0, 999))
    if int(diplFirstNumber) < 100:
        if int(diplFirstNumber) < 10:
            diplFirstNumber = "0"+diplFirstNumber
    diplLetter = random.choice(diplomaticTag)
    diplSecondNumber = str(random.randint(0, 999))
    if int(diplSecondNumber) < 100:
        if int(diplSecondNumber) < 10:
            diplSecondNumber = "00"+diplSecondNumber
        else:
            diplSecondNumber = "0"+diplSecondNumber
    diplomaticPlate = diplFirstNumber + hyphen + diplLetter + hyphen + diplSecondNumber
    print(diplomaticPlate)

#Special Plates

print("-----------Special Plates-----------")
for x in range(10):
    specLetter = random.choice(specialTag)

    #Taxi
    if specLetter == "TX":
        city = random.choice(cityTag)
        number = str(random.randint(0, 9999))
        if int(number) < 100:
            if int(number) < 10:
                number = "00"+number
            else:
                number = "0"+number
            
        end = specLetter
        taxiPlate = city + hyphen + number + hyphen + end
        print(taxiPlate)

    #Police
    elif specLetter == "П":
        policeFirstNumber = str(random.randint(0, 999))
        if int(policeFirstNumber) < 100:
            if int(policeFirstNumber) < 10:
                policeFirstNumber = "00"+policeFirstNumber
            else:
                policeFirstNumber = "0"+policeFirstNumber
        policeSecondNumber = str(random.randint(0, 999))
        if int(policeSecondNumber) < 100:
            if int(policeSecondNumber) < 10:
                policeSecondNumber = "00"+policeSecondNumber
            else:
                policeSecondNumber = "0"+policeSecondNumber
        
        policePlate = specLetter + shield + policeFirstNumber + hyphen + policeSecondNumber
        print(policePlate)

    #Agriculture
    elif specLetter == "AGR":
        city = random.choice(cityTag)
        agroNumber = str(random.randint(0, 99))
        if int(agroNumber) < 10:
            agroNumber = "0"+agroNumber
        agroLetters = randomString(3)
        agroPlate = city + shield + agroNumber + hyphen + agroLetters
        print(agroPlate)

    #Moped
    elif specLetter == "MOPED":
        city = random.choice(cityTag)
        mopedFirstNumber = str(random.randint(0, 999))
        if int(mopedFirstNumber) < 100:
            if int(mopedFirstNumber) < 10:
                mopedFirstNumber = "00"+mopedFirstNumber
            else:
                mopedFirstNumber = "0"+mopedFirstNumber
        mopedSecondNumber = str(random.randint(0, 99))
        if int(mopedFirstNumber) < 10:
            mopedFirstNumber = "0"+mopedFirstNumber
        mopedPlate = city + shield + mopedFirstNumber + hyphen + mopedSecondNumber
        print(mopedPlate)

    #Trailer
    elif specLetter == "TRAILER":
        city = random.choice(cityTag)
        start = randomString(2)
        number = str(random.randint(0, 9999))
        if int(number) < 100:
            if int(number) < 10:
                number = "00"+number
            else:
                number = "0"+number
        trailerPlate = start + hyphen + number + shield + city
        print(trailerPlate)

    #Military
    elif specLetter == "MILITARY":
        start = randomString(1)
        number = str(random.randint(0, 9999))
        if int(number) < 1000:
            if int(number) < 10:
                number = "000"+number
            else:
                number = "00"+number
        militaryPlate = shield + start + hyphen + number
        print(militaryPlate)