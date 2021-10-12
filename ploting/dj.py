def link_gen(link):
    link = link.replace(' ', '-')
    bad_chars = [';', ':', '!', "*", '!', '@', '#', '$', '%', '^', '&', '(', ')']
    for i in bad_chars:
        if bad_chars[-3] in link:
            link = link.replace(i, 'n')
        link = link.replace(i, '')

    if link[-1] == '-':
        link = link[:-1]
        if link[-1] == '-':
            link = link[:-1]

    return link


print(link_gen(link="hai & dasadsd a sdad "))
