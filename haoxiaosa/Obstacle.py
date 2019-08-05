import random
import pygame


# 植物
class Plant(pygame.sprite.Sprite):
	def __init__(self, WIDTH=640, HEIGHT=500):
		pygame.sprite.Sprite.__init__(self)
		self.WIDTH = WIDTH
		self.HEIGHT = HEIGHT
		# 统计分数时用的
		self.added_score = False
		self.speed = 5
		# self.imgs = ['./images/obstacles/plant1.png', './images/obstacles/plant2.png', './images/obstacles/plant3.png', './images/obstacles/plant4.png']
		self.imgs = ['./images/obstacles/plant_big.png', './images/obstacles/plant_small.png']
		self.generate_random()
	# 随机生成障碍物
	def generate_random(self):
		idx = random.randint(0, 1)
		temp = pygame.image.load(self.imgs[idx]).convert_alpha()
		if idx == 0:
			self.plant = temp.subsurface((101*random.randint(0, 2), 0), (101, 101))
		else:
			self.plant = temp.subsurface((68*random.randint(0, 2), 0), (68, 70))
		self.rect = self.plant.get_rect()
		self.rect.left, self.rect.top = self.WIDTH+60, int(self.HEIGHT/2)
	# 不停往左移动
	def move(self):
		self.rect.left = self.rect.left-self.speed
	# 把自己画到屏幕上去
	def draw(self, screen):
		screen.blit(self.plant, self.rect)