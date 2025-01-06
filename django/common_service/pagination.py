
def create_custom_page_range(current_page, total_pages):
    """
    Hàm tạo dải số trang tùy chỉnh
    - Nếu số trang <= 7, hiển thị tất cả các số trang.
    - Nếu số trang > 7, hiển thị số trang đầu, cuối, và một số trang xung quanh trang hiện tại.
    """
    if total_pages <= 7:
        return list(range(1, total_pages + 1))  # Hiển thị toàn bộ các trang

    # neeus lon hon 7, current_page <= 4
    if current_page <= 4:
        # Các trang đầu + '...' + trang cuối
        return list(range(1, 6)) + ['...', total_pages]
    # neeus lon hon 7, current_page o 4 trang cuoi
    if current_page > total_pages - 4:
        # Trang đầu + '...' + các trang cuối
        return [1, '...'] + list(range(total_pages - 4, total_pages + 1))

    # Trang đầu + '...' + xung quanh trang hiện tại + '...' + trang cuối
    return [1, '...'] + list(range(current_page - 2, current_page + 3)) + ['...', total_pages]

