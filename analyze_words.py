#unfinished feature

def get_entities(client, text):
    entities_list = []
    document = types.Document(
        content=text,
        type = enums.Document.Type.PLAIN_TEXT
    )

    entities = client.analyze_entities(document=document).entities

    for entity in entities:
        entity_type = enums.Entity.Type(entity.type)
#        print('=' * 20)
#        print(u'{:<16}: {}'.format('name', entity.name))
#        print(u'{:<16}: {}'.format('type', entity_type.name))
#        print(u'{:<16}: {}'.format('salience', entity.salience))
#        print(u'{:<16}: {}'.format('wikipedia_url',
#              entity.metadata.get('wikipedia_url', '-')))
#        print(u'{:<16}: {}'.format('mid', entity.metadata.get('mid', '-')))
        entities_list.append(entity)
    return entities

def get_adjs(client, text):
    adjs = []
    document = types.Document(
        content=text,
        type=enums.Document.Type.PLAIN_TEXT)

    tokens = client.analyze_syntax(document).tokens

    # part-of-speech tags from enums.PartOfSpeech.Tag
    pos_tag = ('UNKNOWN', 'ADJ', 'ADP', 'ADV', 'CONJ', 'DET', 'NOUN', 'NUM',
               'PRON', 'PRT', 'PUNCT', 'VERB', 'X', 'AFFIX')

    for token in tokens:
        print(u'{}: {}'.format(pos_tag[token.part_of_speech.tag],
                               token.text.content))

        if token.part_of_speech.tag == 1:
            adjs.append(token.text.content)
    return adjs

#print(get_entities(text))
#print(get_adjs(text))
