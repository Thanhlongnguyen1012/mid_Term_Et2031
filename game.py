import pygame
import sys
import level1
import level2
import level3

# Khởi tạo Pygame
pygame.init()

# Tạo kích thước màn hình
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Đặt tiêu đề cho cửa sổ
pygame.display.set_caption("Smart Start ")

# Tải hình ảnh background từ thư viện có sẵn
background = pygame.image.load('img/backgroud/00.jpg')

# Thiết lập màu sắc
black = (0, 0, 0)
light_blue = (173, 216, 230)  # Xanh dương nhạt

# Khởi tạo font chữ
font = pygame.font.SysFont(None, 40)

# Hàm để tạo nút
def create_button(text, x, y, width, height, color):
    rect = pygame.Rect(x, y, width, height)
    pygame.draw.rect(screen, color, rect, border_radius=15)  # Tạo hình chữ nhật góc cong
    label = font.render(text, True, black)
    screen.blit(label, (x + (width - label.get_width()) // 2, y + (height - label.get_height()) // 2))
    return rect

# Hàm để xử lý sự kiện khi nhấp chuột
def button_click_check(button_rects, pos):
    for idx, rect in enumerate(button_rects):
        if rect.collidepoint(pos):  # Kiểm tra nếu vị trí nhấp chuột nằm trong nút
            return idx + 1  # Trả về số level (1, 2, hoặc 3)
    return None

# Vòng lặp menu chính
def main_menu():
    while True:
        # Xử lý sự kiện
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                clicked_button = button_click_check(button_rects, mouse_pos)
                if clicked_button == 1:
                    level1.run_level1()  # Chạy level 1
                elif clicked_button == 2:
                    level2.run_level2()  # Chạy level 2
                elif clicked_button == 3:
                    level3.run_level3()  # Chạy level 3

        # Vẽ background lên màn hình
        screen.blit(background, (0, 0))

        # Tạo 3 nút Level ở giữa
        button_width = 150
        button_height = 50
        gap = 20  # Khoảng cách giữa các nút
        total_width = 3 * button_width + 2 * gap  # Tổng chiều rộng của 3 nút và khoảng cách
        start_x = (screen_width - total_width) // 2
        y_position = screen_height // 2

        button_rects = []  # Lưu vị trí các nút
        button_rects.append(create_button("Level 1", start_x, y_position, button_width, button_height, light_blue))
        button_rects.append(create_button("Level 2", start_x + button_width + gap, y_position, button_width, button_height, light_blue))
        button_rects.append(create_button("Level 3", start_x + 2 * (button_width + gap), y_position, button_width, button_height, light_blue))

        # Cập nhật màn hình
        pygame.display.update()

# Chạy menu chính
main_menu()
