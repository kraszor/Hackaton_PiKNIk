def plone_jak_pochodnia():
    days = ["poniedzialek", "wtorek", "sroda", "czwartek", "piatek", "sobota", "niedziela"]
    after = {
        "poniedzialek": ["wtorek", "sroda", "czwartek", "piatek", "sobota", "niedziela", "poniedzialek"],
        "wtorek": ["sroda", "czwartek", "piatek", "sobota", "niedziela", "poniedzialek", "wtorek"],
        "sroda": ["czwartek", "piatek", "sobota", "niedziela", "poniedzialek", "wtorek", "sroda"],
        "czwartek": ["piatek", "sobota", "niedziela", "poniedzialek", "wtorek", "sroda", "czwartek"],
        "piatek": ["sobota", "niedziela", "poniedzialek", "wtorek", "sroda", "czwartek", "piatek"],
        "sobota": ["niedziela", "poniedzialek", "wtorek", "sroda", "czwartek", "piatek", "sobota"],
        "niedziela": ["poniedzialek", "wtorek", "sroda", "czwartek", "piatek", "sobota", "niedziela"]
    }

    vals = input("Input:")
    vals = vals.split()
    if len(vals) != 2 or vals[0] not in days or not vals[1].isalnum():
        print("Incorrect input.")
        return 0

    day = vals[0]
    num = int(vals[1]) - 7 * (int(vals[1]) // 7)
    if num == 0:
        num = 7

    print(after[day][num - 1])


if __name__ == "__main__":
    plone_jak_pochodnia()
