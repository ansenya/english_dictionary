import math

from app.schemas import PageModel


def get_page(query, page, limit):
    total_items = query.count()
    skip = (page - 1) * limit
    items = query.offset(skip).limit(limit).all()
    total_pages = math.ceil(total_items / limit)

    return PageModel(
        limit=limit,
        total_pages=total_pages,
        current_page=page,
        items=items
    )

def get_page_for_topics(query, page, limit):
    page = get_page(query, page, limit)
    page.items = [i[0] for i in page.items]
    return page
