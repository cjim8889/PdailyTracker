import tika
tika.initVM()
from tika import parser
import pkuseg

seg = pkuseg.pkuseg(model_name='news')



if __name__ == '__main__':

    parsed = parser.from_file("./rmrb2022051701.pdf")
    content = parsed["content"].replace("\n", "").replace(" ", "")

    results = seg.cut(content)
    dictionary = dict()

    for token in results:
        if token not in dictionary:
            dictionary[token] = 1
        else:
            dictionary[token] += 1


    print(dictionary)