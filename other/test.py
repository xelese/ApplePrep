import re

if __name__ == '__main__':
    s = "(845)-132-2436 lqekjhaf278-643-1231akehdjfg aksjhgb [888-888-8888]" \
        "lajdhf ()893-843-1111)"
    r1 = re.findall("[(]\\d{3}[)][-]\\d{3}[-]\\d{4}|\\d{3}[-]\\d{3}[-]\\d{4}", s)
    print(r1)
