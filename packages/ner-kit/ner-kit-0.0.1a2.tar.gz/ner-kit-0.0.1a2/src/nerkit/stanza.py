from stanza.server import CoreNLPClient, StartServer
import stanza

def install_corenlp(corenlp_root_path):
    stanza.install_corenlp(
        dir=corenlp_root_path)

def get_entity_list(text,corenlp_root_path="", language="chinese",memory='6G',timeout=300000):
    if corenlp_root_path!="":
        stanza.install_corenlp(
            dir=corenlp_root_path)

    client = CoreNLPClient(
        start_server=StartServer.TRY_START,
        annotators=['tokenize', 'ssplit', 'pos', 'lemma', 'ner', 'parse', 'depparse', 'coref'],
        timeout=timeout,
        memory=memory,
        properties=language,
        # StartServer=StartServer.TRY_START
    )
    list_token = []
    ann = client.annotate(text)
    for sentence in ann.sentence:
        for token in sentence.token:
            print(token.value, token.pos, token.ner)
            token_model = {
                "value": token.value,
                "pos": token.pos,
                "ner": token.ner
            }
            list_token.append(token_model)
    return list_token
