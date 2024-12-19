from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

class Car:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        glColor3f(0.0, 0.5, 1.0)
        self.draw_rectangle(self.x, self.y, 60, 100)

        glColor3f(0.7, 0.9, 1.0)
        self.draw_rectangle(self.x, self.y + 20, 40, 40)
        self.draw_rectangle(self.x, self.y - 20, 40, 40)

        glColor3f(0.3, 0.3, 0.3)
        self.draw_circle(self.x - 25, self.y + 35, 10)
        self.draw_circle(self.x + 25, self.y + 35, 10)
        self.draw_circle(self.x - 25, self.y - 35, 10)
        self.draw_circle(self.x + 25, self.y - 35, 10)

    @staticmethod
    def draw_rectangle(x, y, width, height):
        Car.line_drawing(x - width // 2, y - height // 2, x + width // 2, y - height // 2)
        Car.line_drawing(x + width // 2, y - height // 2, x + width // 2, y + height // 2)
        Car.line_drawing(x + width // 2, y + height // 2, x - width // 2, y + height // 2)
        Car.line_drawing(x - width // 2, y + height // 2, x - width // 2, y - height // 2)

    @staticmethod
    def draw_circle(center_x, center_y, r):
        x, y = 0, r
        d = 1 - r
        while x <= y:
            Car.circle_pixels(x, y, center_x, center_y)
            if d < 0:
                d += 2 * x + 3
            else:
                d += 2 * (x - y) + 5
                y -= 1
            x += 1

    @staticmethod
    def circle_pixels(x, y, cx, cy):
        glBegin(GL_POINTS)
        glVertex2f(cx + x, cy + y)
        glVertex2f(cx - x, cy + y)
        glVertex2f(cx + x, cy - y)
        glVertex2f(cx - x, cy - y)
        glVertex2f(cx + y, cy + x)
        glVertex2f(cx - y, cy + x)
        glVertex2f(cx + y, cy - x)
        glVertex2f(cx - y, cy - x)
        glEnd()

    @staticmethod
    def line_drawing(x0, y0, x1, y1):
        dx = abs(x1 - x0)
        dy = abs(y1 - y0)
        sx = 1 if x0 < x1 else -1
        sy = 1 if y0 < y1 else -1
        err = dx - dy

        while True:
            glBegin(GL_POINTS)
            glVertex2f(x0, y0)
            glEnd()
            if x0 == x1 and y0 == y1:
                break
            e2 = 2 * err
            if e2 > -dy:
                err -= dy
                x0 += sx
            if e2 < dx:
                err += dx
                y0 += sy

class CarGame:
    def __init__(self):
        self.car = Car(250, 300)
        self.lane_speed = 5
        self.lanes = [i for i in range(700, 1400, 100)]
        self.pause = False
        self.over = False
        self.score = 0

    def draw_lanes(self):
        glColor3f(1.0, 1.0, 1.0)
        self.line_drawing(100, 0, 100, 700)
        self.line_drawing(200, 0, 200, 700)
        self.line_drawing(300, 0, 300, 700)
        self.line_drawing(400, 0, 400, 700)

        for lane_y in self.lanes:
            self.line_drawing(150, lane_y, 150, lane_y - 50)
            self.line_drawing(250, lane_y, 250, lane_y - 50)
            self.line_drawing(350, lane_y, 350, lane_y - 50)

    def update(self, value):
        if not self.pause and not self.over:
            for i in range(len(self.lanes)):
                self.lanes[i] -= self.lane_speed
                if self.lanes[i] < -50:
                    self.lanes[i] = 750

        glutPostRedisplay()
        glutTimerFunc(50, self.update, 0)

    @staticmethod
    def line_drawing(x0, y0, x1, y1):
        dx = abs(x1 - x0)
        dy = abs(y1 - y0)
        sx = 1 if x0 < x1 else -1
        sy = 1 if y0 < y1 else -1
        err = dx - dy

        while True:
            glBegin(GL_POINTS)
            glVertex2f(x0, y0)
            glEnd()
            if x0 == x1 and y0 == y1:
                break
            e2 = 2 * err
            if e2 > -dy:
                err -= dy
                x0 += sx
            if e2 < dx:
                err += dx
                y0 += sy

    def draw_buttons(self):
        start_x = 460
        start_y = 620
        spacing = 80
        button_size = 40

        glColor3f(0.0, 1.0, 1.0)
        self.line_drawing(start_x - button_size // 2, start_y, start_x + button_size // 2, start_y)
        self.line_drawing(start_x - button_size // 2, start_y, start_x, start_y - button_size // 2)
        self.line_drawing(start_x - button_size // 2, start_y, start_x, start_y + button_size // 2)

        glColor3f(1.0, 1.0, 0.0)
        pause_y = start_y - spacing
        if self.pause:
            self.line_drawing(start_x - button_size // 2, pause_y - 5, start_x + button_size // 2, pause_y)
            self.line_drawing(start_x + button_size // 2, pause_y, start_x - button_size // 2, pause_y + 5)
        else:
            self.line_drawing(start_x - button_size // 4, pause_y - button_size // 2, start_x - button_size // 4, pause_y + button_size // 2)
            self.line_drawing(start_x + button_size // 4, pause_y - button_size // 2, start_x + button_size // 4, pause_y + button_size // 2)

        glColor3f(1.0, 0.0, 0.0)
        cancel_y = start_y - 2 * spacing
        self.line_drawing(start_x - button_size // 2, cancel_y + button_size // 2, start_x + button_size // 2, cancel_y - button_size // 2)
        self.line_drawing(start_x + button_size // 2, cancel_y + button_size // 2, start_x - button_size // 2, cancel_y - button_size // 2)

    def stop(self):
        self.pause = not self.pause
        print('Paused' if self.pause else 'Resumed')

    def reset(self):
        self.car.x = 250
        self.car.y = 300
        self.lanes = [i for i in range(700, 1400, 100)]
        self.score = 0
        self.pause = False
        self.over = False
        print("Game Reset")

    def cross(self):
        print(f"Game Over! Score: {self.score}")
        glutLeaveMainLoop()

    def mouse_callback(self, button, state, x, y):
        if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
            ogl_x = x
            ogl_y = 700 - y
            button_size = 40
            start_x = 460
            start_y = 620
            spacing = 80

            if start_x - button_size // 2 <= ogl_x <= start_x + button_size // 2:
                if start_y - button_size // 2 <= ogl_y <= start_y + button_size // 2:
                    self.reset()
                elif start_y - spacing - button_size // 2 <= ogl_y <= start_y - spacing + button_size // 2:
                    self.stop()
                elif start_y - 2 * spacing - button_size // 2 <= ogl_y <= start_y - 2 * spacing + button_size // 2:
                    self.cross()

    def keyboard_input(self, key, x, y):
        step = 100
        if key == b'a' and self.car.x > 150:
            self.car.x -= step
        elif key == b'd' and self.car.x < 350:
            self.car.x += step
        glutPostRedisplay()

    def display(self):
        glClear(GL_COLOR_BUFFER_BIT)
        if self.over:
            self.draw_game_over()
        else:
            self.draw_lanes()
            self.car.draw()
        self.draw_buttons()
        glutSwapBuffers()

    def draw_game_over(self):
        glColor3f(1.0, 0.0, 0.0)
        self.line_drawing(150, 450, 200, 450)  # G
        # Add similar lines to render the rest of "GAME OVER"

    def main(self):
        glutInit()
        glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE)
        glutInitWindowSize(500, 700)
        glutCreateWindow(b"Car Game")
        glClearColor(0.0, 0.0, 0.0, 1.0)
        glOrtho(0.0, 500.0, 0.0, 700.0, -1.0, 1.0)

        glutDisplayFunc(self.display)
        glutMouseFunc(self.mouse_callback)
        glutTimerFunc(25, self.update, 0)
        glutKeyboardFunc(self.keyboard_input)
        glutMainLoop()

if __name__ == "__main__":
    game = CarGame()
    game.main()
