import re



def validateFourDigits(min, max, num):
    try:
        x = int(num)
        if x <= max and x >= min:
            return True
    except:
        return False
    return False

def validateHeight(value):
    unit = value[-2:]
    print(value[0:-2])
    try:
        num = int(value[0:-2])
    except:
        return False

    if unit == "cm":
        if num <= 193 and num >= 150:
            return True
    if unit == "in":
        if num <= 76 and num >= 59:
            return True

    return False

def validateHairColor(value):
    matches = re.match('(#[a-f0-9]{6})', value)
    return bool(matches)

def validateEyeColor(value):
    validColors = {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}

    return value in validColors

def validatePid(value):
    matches = re.match("([0-9]{9})", value)
    return bool(matches)

def validate(key, value):
    if key == "byr":
        return validateFourDigits(1920, 2002, value)
    if key == "iyr":
        return validateFourDigits(2010, 2020, value)
    if key == "eyr":
        return validateFourDigits(2020, 2030, value)
    if key == "hgt":
        return validateHeight(value)
    if key == "hcl":
        return validateHairColor(value)
    if key == "ecl":
        return validateEyeColor(value)
    if key == "pid":
        return validatePid(value)
    print("Invalid key submitted")
    exit()
    return False

file = open('valid.txt', mode = 'r')
lines = file.readlines()
file.close()

rows = []
requiredFields = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
passport = requiredFields.copy()
valid = 0

for line in lines:
    if line == "\n":
        if len(passport) == 0:
            valid += 1
            print("valid passport")
        passport = requiredFields.copy()
        print("new passport")
        print(passport)
    
    fields = line.split()
    for field in fields:
        parsedKv = field.split(":")
        key = parsedKv[0]
        value = parsedKv[1]
        if key == "cid":
            if key in passport:
                passport.remove(key)
        else:
            if validate(key, value):
                passport.remove(key)
        print(key)

if(len(passport) == 0):
    valid += 1

print(valid)