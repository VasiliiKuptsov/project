import requests
import os
from run import get_company

"""  ПО ЗАЯВКЕ РАБОТАЕМ С ВАКАНСИЯМИ НН  """

def main():
    #keyword = input(' ВВЕДИТЕ КЛЮЧЕВОЕ СЛОВО   ')
    print(get_company(1740))
    breake

    page = 0
    hh_pages = 1
    hh_close = False


    while not hh_close:
        if page < hh_pages:
            hh_run.params['page'] = page
            page += 1
            hh_emplouers = hh_run.get_request().json()
            print(hh_emplouers)
            #hh_pages = hh_emplouers['page']
            #hh_items = hh_vacancies['items']

        else:
            hh_close = True


main()