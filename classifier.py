import content


def classifier(contents):
    contents.insert(0, content.Content())
    contents.append(content.Content())
    contents_len = len(contents)
    for idx, cur in enumerate(contents):
        if idx == 0 or idx == (contents_len - 1):
            continue
        prev = contents[idx - 1]
        next = contents[idx + 1]
        cur.is_content = words_classify(prev, cur, next)


def dens_classify(prev, cur, next):
    if cur.link_density() <= 0.333333:
        if prev.link_density() <= 0.555556:
            if cur.text_density() <= 9:
                if next.text_density() <= 10:
                    is_content = not (prev.text_density() <= 4)
                else:
                    is_content = True
            else:
                is_content = not (next.text_density() == 0)
        else:
            is_content = not (next.text_density() <= 11)
    else:
        is_content = False

    return is_content


def words_classify(prev, cur, next):
    if cur.link_density() <= 0.333333:
        if prev.link_density() <= 0.555556:
            if cur.words <= 16:
                if next.words <= 15:
                    is_content = not (prev.words <= 4)
                else:
                    is_content = True
            else:
                is_content = True
        else:
            if cur.words <= 40:
                is_content = not (next.words <= 17)
            else:
                is_content = True
    else:
        is_content = False
    return is_content
