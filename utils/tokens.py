with open('TOKENS.txt', 'r') as f:
    TOKENS_LIST = f.readlines()
    
    ASTRANGER = TOKENS_LIST[0]
    if (len(TOKENS_LIST) > 1):
        BSTRANGER = TOKENS_LIST[1]
        if (len(TOKENS_LIST) > 2):
            CSTRANGER = TOKENS_LIST[2]
