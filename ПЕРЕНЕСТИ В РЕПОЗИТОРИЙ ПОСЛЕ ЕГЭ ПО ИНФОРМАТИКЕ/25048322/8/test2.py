text = "КАЛЕЙДОСКОП"
text = "".join(sorted(set(text)))[::-1]

def main(text):
    count = 0
    for a in text:
        for b in text:
            for c in text:
                for d in text:
                    for e in text:
                        for f in text:
                            txt = a+b+c+d+e+f
                            if count % 2 == 1 or\
                                a != 'К' or\
                                txt.count('Й') < 2 or\
                                "С" in txt or\
                                "Е" in txt:
                                count += 1
                                continue

                            print(count, txt)
                            return ""

main(text)