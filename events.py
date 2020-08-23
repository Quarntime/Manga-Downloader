import os
import config as cf
import methods as _m

# command for <Return> key on search bar and search button
def search(keyword):
    # reseting the results
    for i in range(len(cf.button)):
        cf.button[i].pack_forget()

    # initializes/resets value
    method = _m.Methods(keyword, domain_path=[], chapters=[], thumbnail=[], type=[], manga_name=[], genre=[])

    # runs for each site in the cf.urls list
    for i in range(len(cf.urls)):
        metod.initialize()

        try:
            method.mangareader()

        # resets loop with a different url on next run
        except AttributeError as error:
            cf.url_index += 1
            print('I failed father', error)

        # ends loop on successful run
        else:
            break
