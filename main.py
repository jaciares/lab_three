import numpy as np
import pandas as pd
import matplotlib
import openpyxl
import os
from io import StringIO

# States
# Turn off line length for this section
# pylint: disable=C0301
us_states = {'Alabama': {'Capital': 'Montgomery', 'Bird': 'Yellowhammer',
                         'Flower': 'Camellia', 'Population': '4889870',
                         'URL': 'https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/camellia-flower.jpg?itok=K1xKDUI5'},

             'Alaska': {'Capital': 'Juneau', 'Bird': 'Willow Ptarmigan',
                        'Flower': 'Forget Me Not', 'Population': '738432',
                        'URL': 'https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/Alpineforgetmenot.jpg?itok=VxF44TUl'},

             'Arizona': {'Capital': 'Phoenix', 'Bird': 'Cactus Wren',
                         'Flower': 'Saguaro Cactus Blossom',
                         'Population': '6828065',
                         'URL': 'https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/saguaroflowersFlickr.jpg?itok=DxWnZav5'},

             'Arkansas': {'Capital': 'Little Rock', 'Bird': 'Mockingbird',
                          'Flower': 'Apple Blossom', 'Population': '2978204',
                          'URL': 'https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/AppletreeblossomArkansasflower.JPG?itok=HRX6pZyN'},

             'California': {'Capital': 'Sacramento', 'Bird': 'California Valley Quail',
                            'Flower': 'Golden Poppy', 'Population': '39144818',
                            'URL': 'https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/CAflowerCaliforniaPoppy.jpg?itok=62onOuJf'},

             'Colorado': {'Capital': 'Denver', 'Bird': 'Lake Bunting',
                          'Flower': 'Rocky Mountain Columbine', 'Population': '5456574',
                          'URL': 'https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/Colorado_columbine2.jpg?itok=3bfYnk5Y'},

             'Connecticut': {'Capital': 'Hartford', 'Bird': 'Robin',
                             'Flower': 'Mountain Laurel', 'Population': '3590886',
                             'URL': 'https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/Mountain-Laural-flowers2.jpg?itok=b7tlfk4G'},

             'Delaware': {'Capital': 'Dover', 'Bird': 'Blue Hen Chicken',
                          'Flower': 'Peach Blossom', 'Population': '945934',
                          'URL': 'https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/peachblossomspeachflowers.jpg?itok=Lx-fzlgl'},

             'Florida': {'Capital': 'Tallahassee', 'Bird': 'Mockingbird',
                         'Flower': 'Orange Blossom', 'Population': '20271272',
                         'URL': 'https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/OrangeBlossomsFloridaFlower.jpg?itok=SK-Tp-rH'},

             'Georgia': {'Capital': 'Atlanta', 'Bird': 'Brown Thrasher',
                         'Flower': 'Cherokee Rose', 'Population': '10214860',
                         'URL': 'https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/CherokeeRoseFlower.jpg?itok=TKWxpzcw'},

             'Hawaii': {'Capital': 'Honolulu', 'Bird': 'Nene',
                        'Flower': 'Hibiscus', 'Population': '1431603',
                        'URL': 'https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/yellowhibiscusPuaAloalo.jpg?itok=Y2aYqLKY'},

             'Idaho': {'Capital': 'Boise', 'Bird': 'Mountain Blue Bird',
                       'Flower': 'Syringa', 'Population': '1654930',
                       'URL': 'https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/syringaPhiladelphuslewisiiflower.jpg?itok=BKOaOXs0'},

             'Illinois': {'Capital': 'Springfield', 'Bird': 'Cardinal',
                          'Flower': 'Violet', 'Population': '12859995',
                          'URL': 'https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/singlebluevioletflower.jpg?itok=8i1uQHwg'},

             'Indiana': {'Capital': 'Indianapolis', 'Bird': 'Cardinal',
                         'Flower': 'Peony', 'Population': '6619680',
                         'URL': 'https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/PeonyPaeoniaflowers.jpg?itok=IrFIQ9ZF'},

             'Iowa': {'Capital': 'Des Moines', 'Bird': 'Eastern Goldfinch',
                      'Flower': 'Wild Rose', 'Population': '3123899',
                      'URL': 'https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/WildPrairieRose.jpg?itok=zyo0qIMG'},

             'Kansas': {'Capital': 'Topeka', 'Bird': 'Western Meadowlark',
                        'Flower': 'Sunflower', 'Population': '2911641',
                        'URL': 'https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/native-sunflowers.jpg?itok=PB8Qq-IC'},

             'Kentucky': {'Capital': 'Frankfort', 'Bird': 'Cardinal',
                          'Flower': 'Goldenrod', 'Population': '4425092',
                          'URL': 'https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/stateflowergoldenrod-bloom.jpg?itok=CCLZ4eiV'},

             'Louisiana': {'Capital': 'Baton Rouge', 'Bird': 'Eastern Brown Pelican',
                           'Flower': 'Magnolia', 'Population': '4670724',
                           'URL': 'https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/MagnoliagrandifloraMagnoliaflower.jpg?itok=LQ7y9QJk'},

             'Maine': {'Capital': 'Augusta', 'Bird': 'Chickadee',
                       'Flower': 'White Pine Cone and Tassel', 'Population': '1329328',
                       'URL': 'https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/whitepinemalecones.jpg?itok=cscy757F'},

             'Maryland': {'Capital': 'Annapolis', 'Bird': 'Baltimore Oriole',
                         'Flower': 'Black-eyed Susan', 'Population': '6006401',
                         'URL': 'https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/FlowerMDBlack-eyedSusan.jpg?itok=I8jYSvFl'},

             'Massachusetts': {'Capital': 'Boston', 'Bird': 'Chickadee',
                               'Flower': 'Mayflower', 'Population': '6794422',
                               'URL': 'https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/MayflowerTrailingArbutus.jpg?itok=uIQd8O6F'},

             'Michigan': {'Capital': 'Lansing', 'Bird': 'American Robin',
                          'Flower': 'Apple Blossom', 'Population': '9922576',
                          'URL': 'https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/appleblossombeauty.jpg?itok=HxWn6VHl'},

             'Minnesota': {'Capital': 'St.Paul', 'Bird': 'Common Loon',
                           'Flower': 'Lady Slipper', 'Population': '5489594',
                           'URL': 'https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/pinkwhiteladysslipperflower1.jpg?itok=LGYZFl26'},

             'Mississippi': {'Capital': 'Jackson', 'Bird': 'Mockingbird',
                             'Flower': 'Magnolia', 'Population': '2992333',
                             'URL': 'https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/magnoliablossomflower01.jpg?itok=xlIoba-H'},

             'Missouri': {'Capital': 'Jefferson City', 'Bird': 'Bluebird',
                          'Flower': 'Hawthorn', 'Population': '6083672',
                          'URL': 'https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/hawthornflowersblossoms1.jpg?itok=LOrlsJ3L'},

             'Montana': {'Capital': 'Helena', 'Bird': 'Western Meadowlark',
                         'Flower': 'Bitterroot', 'Population': '1032949',
                         'URL': 'https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/bitterrootfloweremblem.jpg?itok=SnCwy78x'},

             'Nebraska': {'Capital': 'Lincoln', 'Bird': 'Western Meadowlark',
                          'Flower': 'Goldenrod', 'Population': '1896190',
                          'URL': 'https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/goldenrodflowersyellow4.jpg?itok=6X5qpm4c'},

             'Nevada': {'Capital': 'Carson City', 'Bird': 'Mountain Bluebird',
                        'Flower': 'Sagebrush', 'Population': '2890845',
                        'URL': 'https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/Nevada-Sagebrush-Artemisia-tridentata.jpg?itok=ij6RMnom'},

             'New Hampshire': {'Capital': 'Concord', 'Bird': 'Purple Finch',
                               'Flower': 'Purple Lilac', 'Population': '1330608',
                               'URL': 'https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/lilacflowerspurplelilac.jpg?itok=GM5URJEO'},

             'New Jersey': {'Capital': 'Trenton', 'Bird': 'Eastern Goldfinch',
                            'Flower': 'Purple Violet', 'Population': '8958013',
                            'URL': 'https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/wood-violet.jpg?itok=IJ0ft_8r'},

             'New Mexico': {'Capital': 'Santa Fe', 'Bird': 'Roadrunner',
                            'Flower': 'Yucca', 'Population': '2085109',
                            'URL': 'https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/YuccaFlowersclose.jpg?itok=jCUN8toc'},

             'New York': {'Capital': 'Albany', 'Bird': 'Bluebird',
                          'Flower': 'Rose', 'Population': '19795791',
                          'URL': 'https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/redrosebeautystateflowerNY.jpg?itok=LDcB_Vc_'},

             'North Carolina': {'Capital': 'Raleigh', 'Bird': 'Cardinal',
                                'Flower': 'Dogwood', 'Population': '10042802',
                                'URL': 'https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/floweringdogwoodflowers2.jpg?itok=p_1PGcNk'},

             'North Dakota': {'Capital': 'Bismarck', 'Bird': 'Western Meadowlark',
                              'Flower': 'Wild Prairie Rose', 'Population': '756927',
                              'URL': 'https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/flowerwildprairierose.jpg?itok=j5Retaxz'},

             'Ohio': {'Capital': 'Columbus', 'Bird': 'Cardinal',
                      'Flower': 'Scarlet Carnation', 'Population': '11613423',
                      'URL': 'https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/WhitetrilliumTrilliumgrandiflorum.jpg?itok=oGiuGS6p'},

             'Oklahoma': {'Capital': 'Oklahoma City', 'Bird': 'Scissor-tailed Flycatcher',
                          'Flower': 'Mistletoe', 'Population': '3911338',
                          'URL': 'https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/mistletoe_phoradendron_serotinum.jpg?itok=7W9kY8YB'},

             'Oregon': {'Capital': 'Salem', 'Bird': 'Western Meadowlark',
                        'Flower': 'Oregon Grape', 'Population': '4028977',
                        'URL': 'https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/Oregongrapeflowers2.jpg?itok=lVSJoqCE'},

             'Pennsylvania': {'Capital': 'Harrisburg', 'Bird': 'Ruffed Grouse',
                              'Flower': 'Mountain Laurel', 'Population': '12802503',
                              'URL': 'https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/Mt_Laurel_Kalmia_Latifolia.jpg?itok=8VhW2Sms'},

             'Rhode Island': {'Capital': 'Providence', 'Bird': 'Rhode Island Red',
                              'Flower': 'Violet', 'Population': '1056298',
                              'URL': 'https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/violetsflowers.jpg?itok=KNMrrLfu'},

             'South Carolina': {'Capital': 'Columbia', 'Bird': 'Great Carolina Wren',
                                'Flower': 'Carolina Yellow Jessamine', 'Population': '4896146',
                                'URL': 'https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/CarolinaYellowJessamine101.jpg?itok=1tgcX6mj'},

             'South Dakota': {'Capital': 'Pierre', 'Bird': 'Ring-necked Pheasant',
                              'Flower': 'American Pasqueflower', 'Population': '858469',
                              'URL': 'https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/Pasqueflower-03.jpg?itok=vMlGt_qW'},

             'Tennessee': {'Capital': 'Nashville', 'Bird': 'Mockingbird',
                           'Flower': 'Iris', 'Population': '6600299',
                           'URL': 'https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/purpleirisflower.jpg?itok=ZJjHu7Lb'},

             'Texas': {'Capital': 'Austin', 'Bird': 'Mockingbird',
                       'Flower': 'Bluebonnet', 'Population': '27469114',
                       'URL': 'https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/EnnisTXbluebonnetfield.jpg?itok=H8r2UOSJ'},

             'Utah': {'Capital': 'Salt Lake City', 'Bird': 'Common American Gull',
                      'Flower': 'Sego Lily', 'Population': '2995919',
                      'URL': 'https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/SegoLily.jpg?itok=Hxt3DOTq'},

             'Vermont': {'Capital': 'Montpelier', 'Bird': 'Hermit Thrush',
                         'Flower': 'Red Clover', 'Population': '626042',
                         'URL': 'https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/redcloverstateflowerWV.jpg?itok=wvnkPA4C'},

             'Virginia': {'Capital': 'Richmond', 'Bird': 'Cardinal',
                          'Flower': 'American Dogwood', 'Population': '8382993',
                          'URL': 'https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/floweringDogwoodSpring.jpg?itok=DFuNFYgS'},

             'Washington': {'Capital': 'Olympia', 'Bird': 'Willow Goldfinch',
                            'Flower': 'Coast Rhododendron', 'Population': '7170351',
                            'URL': 'https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/flower_rhododendronWeb.jpg?itok=0Xl911Zf'},

             'West Virginia': {'Capital': 'Charleston', 'Bird': 'Cardinal',
                               'Flower': 'Rhododendron', 'Population': '1844128',
                               'URL': 'https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/rhododendronWVstateflower.jpg?itok=7lJaeqWT'},

             'Wisconsin': {'Capital': 'Madison', 'Bird': 'Robin',
                           'Flower': 'Wood Violet', 'Population': '5771337',
                           'URL': 'https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/wood-violet.jpg?itok=IJ0ft_8r'},

             'Wyoming': {'Capital': 'Cheyenne', 'Bird': 'Western Meadowlark',
                         'Flower': 'Indian Paintbrush', 'Population': '586107',
                         'URL': 'https://statesymbolsusa.org/sites/statesymbolsusa.org/files/styles/symbol_thumbnail__medium/public/primary-images/indianpaintbrushWYflower.jpg?itok=ClQHPA55'}

            }

# Turn on line length for rest of code
# pylint: enable=C0301

def alphabetical_states():
    pass


def search_state():
    pass


def top_five_states():
    pass


def update_state_pop():
    pass


def exit_program():
    pass


def app_banner():
    print('*' * 90)
    title = "Python State Capital and Flower List Application"
    centered_title = title.center(90, " ")
    print(centered_title)
    print('*' * 90)


def menu():
    app_banner()

    print('1. Display all U.S States in Alphabetical order along with\n\tthe '
          'Capital, State Population, and Flower\n')

    print('2. Search for a specific state and display the appropriate '
          'Capital name,\n\tState population, and an image of the associated '
          'State Flower.\n')

    print('3. Provide a Bar graph of the top 5 populated States showing '
          'their overall population.\n')

    print('4. Update the overall state population for a specific date.\n')

    print('5. Exit the program\n')

    try:
        user_selection = int(input('Please make a selection from 1-5: '))
        if user_selection == 1:
            alphabetical_states()
        if user_selection == 2:
            search_state()
        if user_selection == 3:
            top_five_states()
        if user_selection == 4:
            update_state_pop()
        if user_selection == 5:
            exit_program()

    except ValueError:
        print('Please enter a number 1 - 5!')
        menu()


def main():
    menu()


if __name__ == '__main__':
    main()
