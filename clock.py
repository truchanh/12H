"""
a simple program to display the clock of current time
"""
import time,math
import pygame as pg

pg.init()
pg.display.set_caption('analog clock:3')

WINW = 640
WINH = 480
HALF_W = WINW/2
HALF_H = WINH/2

win = pg.display.set_mode((WINW,WINH))
clk = pg.time.Clock()


def draw_text(info,color,pos):
	font = pg.font.SysFont('comicsansms',18)
	text_surf = font.render(info,1,color)
	text_rect = text_surf.get_rect(topleft=pos)
	win.blit(text_surf,text_rect)


def main():
	r = 200
	done:bool = 0
	# main game loop (infinite loop until a condition is met)
	while not done:

		# main event loop
		for e in pg.event.get():
			if e.type in (pg.QUIT,pg.WINDOWCLOSE):
				done = 1  # exit main while.. loop when the user click the close button


		# to get the current time you MUST keep it within the main loop
		current_time: str = time.strftime('%I:%M:%S')  # format hour:minutes:second
		# convert str to list[str] of hour,minutes,second 
		current_time_list_str = current_time.split(':') 
		# convert every element in the list from str to int using list comprehension
		current_time_list_int = [int(i) for i in current_time_list_str]
		# extract/unpacking three elements in the list[int] to variables
		hour,mins,sec = current_time_list_int


		# calculate the angle(deg)
		hour_angle = 360/12
		# because 1hour=60mins and 1mins=60sec so they have the same angle
		mins_angle = sec_angle = hour_angle/5


		# convert angle(deg) to theta(rad)
		# and theta of 0deg will be at the 3 hour o'clock
		# so we must subtract 90deg
		sec_theta = math.radians((sec*sec_angle)-90)
		min_theta = math.radians((mins*mins_angle)-90)
		hour_theta = math.radians((hour*hour_angle)-90) 


		# first of all, clear the entire screen to a plain color
		win.fill('black')
		
		# blitzing the current hour text at the bottomright corner of the screen
		draw_text(current_time_list_str[0],'red',(WINW-105,WINH-25))
		draw_text(':','white',(WINW-105+25,WINH-25))
		draw_text(current_time_list_str[1],'green',(WINW-105+40,WINH-25))
		draw_text(':','white',(WINW-105+65,WINH-25))
		draw_text(current_time_list_str[2],'blue',(WINW-105+80,WINH-25))
		
		pg.draw.circle(win,(30,30,30),(HALF_W,HALF_H),r+5,5)

		for i in range(60):
			if (mins_angle*i)%5 != 0:
				# draw every minutes&second separator to divide our 
				# circle into sixty equal parts
				x0 = HALF_W+(r-10)*math.cos(math.radians(mins_angle*i))
				y0 = HALF_H+(r-10)*math.sin(math.radians(mins_angle*i))
				x1 = HALF_W+r*math.cos(math.radians(mins_angle*i))
				y1 = HALF_H+r*math.sin(math.radians(mins_angle*i))
				pg.draw.line(win,(190,190,190),(x0,y0),(x1,y1),1)
			else:
				# draw every hour separator to divide our 
				# circle into twelve equal parts
				cx = HALF_W+(r-5)*math.cos(math.radians(hour_angle*i))
				cy = HALF_H+(r-5)*math.sin(math.radians(hour_angle*i))
				pg.draw.circle(win,(190,190,190),(cx,cy),5,0)

		# draw the hour clock hand
		pg.draw.line(win,'red',(HALF_W,HALF_H),
			(HALF_W+(r-100)*math.cos(hour_theta),
			 HALF_H+(r-100)*math.sin(hour_theta)),5)
		
		# draw the minute clock hand
		pg.draw.line(win,'green',(HALF_W,HALF_H),
			(HALF_W+(r-40)*math.cos(min_theta),
			 HALF_H+(r-40)*math.sin(min_theta)),5)

		# draw the second clock hand
		pg.draw.line(win,'blue',
			(HALF_W-40*math.cos(sec_theta),
			 HALF_H-40*math.sin(sec_theta)), 
			(HALF_W+(r-5)*math.cos(sec_theta),
			 HALF_H+(r-5)*math.sin(sec_theta)),3) 
		
		# draw a small circle on top of the second clock hand
		pg.draw.circle(win,'blue',(HALF_W,HALF_H),6,0)


		# update everything you've drawn
		pg.display.flip()
	pg.quit()

if __name__ == '__main__':
	main()
