from json import JSONDecoder
from howdoi import howdoi
jd = JSONDecoder()


def get_answers(question: str, pos=1):
    answer = jd.decode(howdoi.howdoi(f'{question} -j -p {pos}'))[0]
    return answer
