import xlwt
from collections.abc import Iterable
from .errors import *


def create(**kw):
    workbook = xlwt.Workbook()  # 注意Workbook的开头W要大写
    sheets = []
    try:
        x1 = kw['sheets']['x']
    except KeyError:
        raise nameNotFoundError('sheets[x]')
    try:
        y1 = kw['sheets']['y']
    except KeyError:
        raise nameNotFoundError('sheets[y]')
    try:
        lt = kw['sheets']['t']
    except KeyError:
        raise nameNotFoundError('sheets[t]')

    try:
        path = kw['path']
    except KeyError:
        raise nameNotFoundError('path')

    try:
        names = kw['sheets']['names']
    except KeyError:
        raise nameNotFoundError('sheets[names]')

    try:
        if isinstance(kw['sheets']['numList'], Iterable):
            for x in kw['sheets']['numList']:
                try:
                    sheets.append(workbook.add_sheet(
                        names[x], cell_overwrite_ok=True))
                except IndexError:
                    raise IndexError()
        else:
            raise NotIterableError()
    except KeyError:
        raise nameNotFoundError('sheets[numList]')
    for y in sheets:
        try:
            for z in range(len(x1)-1):
                y.write(x1[z], y1[z], lt['time'][z])
            for i in range(len(lt['text'])):
                print(type(lt['text'][i][1][0]), type(lt['text']
                      [i][1][1]), lt['text'][i][0])
                y.write(int(lt['text'][i][1][0]), int(lt['text']
                        [i][1][1]), str(lt['text'][i][0]))
        except IndexError:
            raise IndexError()
    workbook.save(path)


create(
    path='./index.xls',
    sheets={
        'x': [1-1, 2-1, 3-1, 4-1, 5-1, 6-1, 6],
        'y': [1-1, 1-1, 1-1, 1-1, 1-1, 1-1, 0],
        'numList': range(2),
        'names': ['a', 'b'],
        't': {
            'time':
            [
                '7:00~9:00',
                '9:00~12:00',
                '12:00~2:00',
                '2:00~4:00',
                '4:00~6:00',
                '6:00~9:00'
            ],
            'text': [
                ['你好', [1, 1]],
                ['你好', [2, 1]],
                ['你好', [3, 1]],
                ['你好', [4, 1]],
                ['你好', [5, 1]],
                ['你好', [6, 1]]
            ]
        }
    }
)
