import pandas as pd


data_frame = pd.read_csv("faktura_do_zad_Python_15.10_21.00.csv",
                         delimiter=";",
                         names=["nazwa_produktu", "cena_netto", "VAT", "narzut"])


def formula(price, tax, markup):
    correct_price = (float(price) * 0.01) * \
                    (1 + (float(tax) * 0.01)) * \
                    (1 + (float(markup) * 0.01))
    return round(correct_price, 2)


def create_receipt(name, price, tax, markup, correct_price):
    print(f'[{name}]')
    print(f'cena_netto = {round(float(price) * 0.01, 2)}')
    print(f'podatek_vat = {tax}%')
    print(f'narzut = {markup}%')
    print(f'CENA_SKLEPOWA = {correct_price}')
    print("-" * (17 + len(str(correct_price))))


def main():
    for i in range(len(data_frame)):
        correct_price = formula(data_frame.cena_netto[i],
                                data_frame.VAT[i],
                                data_frame.narzut[i])
        create_receipt(data_frame.nazwa_produktu[i],
                       data_frame.cena_netto[i],
                       data_frame.VAT[i],
                       data_frame.narzut[i],
                       correct_price)


if __name__ == "__main__":
    main()
