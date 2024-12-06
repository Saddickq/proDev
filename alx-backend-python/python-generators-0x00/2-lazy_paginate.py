from paginate_users import paginate_users

def lazy_paginate(page_size):
    offset = 0
    while True:
        batch = paginate_users(page_size=page_size, offset=offset)
        if not batch:
            break
        yield batch
        offset += page_size