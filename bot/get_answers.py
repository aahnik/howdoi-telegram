from json import JSONDecoder
from howdoi import howdoi
jd = JSONDecoder()


def get_answers(question: str, pos=1):

    try:
        raw_answer = howdoi.howdoi(f'{question} -j -p {pos}')
        answer = jd.decode(raw_answer)[0]
    except Exception as err:
        return {'warning': 'Something went wrong.'}
    else:
        return answer
