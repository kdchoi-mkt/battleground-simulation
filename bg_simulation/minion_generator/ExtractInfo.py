from bs4 import BeautifulSoup
from .constant import INDEX_CONVERTER, TYPE_CONVERTER


class ExtractInfo(object):
    def __init__(self, file_path):
        self.file = open(file_path, 'r').readline()
        self.crawler = BeautifulSoup(self.file, 'html.parser')
        self.table_tag = 'div > div > div > table'

        self.parser = self.crawler.select(self.table_tag)

    def extract_info(self):
        information = list()
        for tag in self.parser:
            try:
                block = self.extract_block()
                single_info = {
                    key: block[key](tag) for key in block
                }
                information.append(single_info)
            except Exception as ex:
                print(ex)

        return information

    def extract_block(self) -> dict:
        """Build the block
        ================
        Example
        {
            'name': _function(tag)
        }
        """
        basic_info = {
            'KoreanName': lambda tag: self._extract_table_row(tag, 'KoreanName')[1],
            'Name': lambda tag: self._extract_table_row(tag, 'EngName')[1],
            'Tier': lambda tag: self._extract_table_row(tag, 'Tier')[1],
            'Type': lambda tag: TYPE_CONVERTER[self._extract_table_row(tag, 'Type')[1]],
            'Text': lambda tag: self._extract_table_row(tag, 'Text')[1],
            'Attack': lambda tag: self._extract_table_row(tag, 'Ability')[1].split('(')[0],
            'Health': lambda tag: self._extract_table_row(tag, 'Ability')[3].split('(')[0]
        }

        keyword_info = {
            'Taunt': lambda tag: '도발' in basic_info['Text'](tag),
            'DivineShield': lambda tag: '천상의 보호막' in basic_info['Text'](tag),
            'Reborn': lambda tag: '환생' in basic_info['Text'](tag),
            'Windfury': lambda tag: '질풍' in basic_info['Text'](tag),
            'Frenzy': lambda tag: '광분' in basic_info['Text'](tag),
            'BattleCry': lambda tag: '전투의 함성:' in basic_info['Text'](tag),
            'Poison': lambda tag: '독성:' in basic_info['Text'](tag),
            'DeathRattle': lambda tag: '죽음의 메아리:' in basic_info['Text'](tag),
            'Avenge': lambda tag: '복수' in basic_info['Text'](tag),
            'AvengeCount': lambda tag: self._extract_avenge_count(basic_info['Text'](tag)),
            'AvailableInShop': lambda tag: '-' != basic_info['Text'](tag),
        }

        basic_info.update(keyword_info)

        return basic_info

    def _extract_table_row(self, tag, index_key):
        return [elem.text for elem in tag.select('tr')[INDEX_CONVERTER[index_key]]]

    def _indicate_keyword(self, text_ftn, keyword):
        return keyword in text_ftn

    def _extract_avenge_count(self, text):
        if '복수' not in text:
            return 0
        else:
            return int(
                text.split(':')[0].replace('복수 (', '').replace(')', '')
            )
