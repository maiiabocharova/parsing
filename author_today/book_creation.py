from ebooklib import epub
book = epub.EpubBook()

def create_book_from_chapters(chapters_texts,
                           chapters_names,
                           book_name = 'Красавица, чудовище и волшебник без лицензии'):
    # set metadata

    book.set_title(book_name)
    book.set_language('ru')
    book.add_author('Мария Заболотская')
    book.set_identifier("NA12345")

    # add default NCX and Nav file
    book.add_item(epub.EpubNcx())
    book.add_item(epub.EpubNav())

    style = 'BODY {color: white;}'
    nav_css = epub.EpubItem(uid="style_nav",
                            file_name="style/nav.css",
                            media_type="text/css",
                            content=style)

    # add CSS file
    book.add_item(nav_css)

    # cycle through chapters:
    spine = ['nav']
    toc = []

    for content,chapter_name in zip(chapters_texts, chapters_names):

        # create chapter objects:
        chapter = epub.EpubHtml(
                           title=chapter_name,
                           file_name=chapter_name +'.xhtml',
                           lang='ru')

        chapter.set_content(f"<h1>{chapter_name}</h1>{content}")

        book.add_item(chapter)

        spine.append(chapter)
        toc.append(chapter)

    # Everything you put in spine and toc must exists inside of the book. EPUB will bot be valid if
    # they don't exist.
    book.spine = spine
    book.toc = toc

    # write file:
    epub.write_epub(book_name + '.epub', book)
