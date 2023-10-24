import re
import csv
import json

def data_cleansing(content):
    # ex : (...)
    refine_content = re.sub(r'\([^)]*\)', '', content)

    # ex : [...]
    refine_content = re.sub(r'\[[^\]]*\]', '', refine_content)

    # ex : email
    refine_content = re.sub(r'\S+@\S+', '', refine_content)

    # ex : 2023.10.24 or 2023.10.24/...
    refine_content = re.sub(r'\d{4}\.\d{1,2}\.\d{1,2}(?:/[^ ]*)?', '', refine_content)

    # ex : http://... or https://...
    refine_content = re.sub(r'https?://\S+', '', refine_content)

    # ex : ... 기자=
    refine_content = re.sub(r'[\wㄱ-ㅎㅏ-ㅣ가-힣]+ 기자\s?=', '', refine_content)

    refine_content = re.sub(r'ⓒ News1', '', refine_content)

    refine_content = re.sub(r'ⓒ AFP=뉴스1', '', refine_content)

    refine_content = re.sub(r'/연합뉴스', '', refine_content)

    refine_content = re.sub(r'Copyright  뉴스1.', '', refine_content)

    refine_content = re.sub(r'All rights reserved.', '', refine_content)

    # ex : 'Loading... player_likesound_mutesound_mutesound_volume2sound_volume3 Player' ... '복사 레이어 닫기'
    pattern_v1 = r'Loading\.\.\. player_likesound_mutesound_mutesound_volume2sound_volume3 Player.*?복사 레이어 닫기'
    refine_content = re.sub(pattern_v1, '', refine_content, flags=re.DOTALL)

    # ex : 'Loading... player_likesound_mutesound_mutesound_volume2sound_volume3 Player' ... '소요 시간은 달라집니다.'
    pattern_v2 = r'Loading\.\.\. player_likesound_mutesound_mutesound_volume2sound_volume3 Player.*?소요 시간은 달라집니다.'
    refine_content = re.sub(pattern_v2, '', refine_content, flags=re.DOTALL)

    refine_content = re.sub(r'국회사진취재단 =', '', refine_content)

    # ex : <...>
    refine_content = re.sub(r'<[^>]*>', '', refine_content)

    # ex : /사진=...
    refine_content = re.sub(r'/사진=[^ ]+', '', refine_content)

    # 특수문자 제거
    refine_content = re.sub('[^\w\s\.\,]', '', refine_content)

    # 공백 제거
    refine_content = re.sub(r' ', '', refine_content)


    return refine_content


def set_csv_file(raw_file_path, new_file_path):
    with open(new_file_path, 'w', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file)

        csv_writer.writerow(['title', 'content', 'refine_content', 'id'])

        with open(raw_file_path, 'r', encoding='utf-8') as json_file:
            for line in json_file:
                data = json.loads(line)

                for item in data:
                    source = item.get('_source')

                    id = item.get('_id')

                    title = source.get('title')
                    
                    content = source.get('content')

                    refine_content = data_cleansing(content)

                    csv_writer.writerow([title, content, refine_content, id])

if __name__ == '__main__':
    set_csv_file(raw_file_path='', new_file_path='')