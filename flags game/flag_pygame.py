# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 17:17:21 2022

@author: aldis
"""
#TODO Implement timer and score counter


import pygame
from PIL import Image
import random
import time
import csv

WIDTH, HEIGHT = 900, 500

log_file = "score_log.csv"

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("World Flags")

SCORE = 0
START_TIME, END_TIME = 0, 0

FR = 60

pygame.init()
FONT_SIZE = 40
FONT = pygame.font.SysFont('comicans', FONT_SIZE)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

COUNTRIES = ['Afghanistan (Islamic Emirate)',
 'Afghanistan (Islamic Republic)',
 'Albania',
 'Algeria',
 'Andorra',
 'Angola',
 'Antigua and Barbuda',
 'Argentina',
 'Armenia',
 'Australia',
 'Austria',
 'Azerbaijan',
 'Bahamas',
 'Bahrain',
 'Bangladesh',
 'Barbados',
 'Belarus',
 'Belgium',
 'Belize',
 'Benin',
 'Bhutan',
 'Bolivia',
 'Bosnia and Herzegovina',
 'Botswana',
 'Brazil',
 'Brunei',
 'Bulgaria',
 'Burkina Faso',
 'Burundi',
 'Cambodia',
 'Cameroon',
 'Canada',
 'Cape Verde',
 'Central African Republic',
 'Chad',
 'Chile',
 'China',
 'Colombia',
 'Comoros',
 'Democratic Republic of the Congo',
 'Republic of the Congo',
 'Costa Rica',
 'Croatia',
 'Cuba',
 'Cyprus',
 'Czech Republic',
 'Denmark',
 'Djibouti',
 'Dominica',
 'Dominican Republic',
 'East Timor',
 'Ecuador',
 'Egypt',
 'El Salvador',
 'Equatorial Guinea',
 'Eritrea',
 'Estonia',
 'Eswatini',
 'Ethiopia',
 'Fiji',
 'Finland',
 'France',
 'Gabon',
 'Gambia',
 'Georgia',
 'Germany',
 'Ghana',
 'Greece',
 'Grenada',
 'Guatemala',
 'Guinea',
 'Guinea-Bissau',
 'Guyana',
 'Haiti',
 'Honduras',
 'Hungary',
 'Iceland',
 'India',
 'Indonesia',
 'Iran',
 'Iraq',
 'Ireland',
 'Israel',
 'Italy',
 'Ivory Coast',
 'Jamaica',
 'Japan',
 'Jordan',
 'Kazakhstan',
 'Kenya',
 'Kiribati',
 'North Korea',
 'South Korea',
 'Kuwait',
 'Kyrgyzstan',
 'Laos',
 'Latvia',
 'Lebanon',
 'Lesotho',
 'Liberia',
 'Libya',
 'Liechtenstein',
 'Lithuania',
 'Luxembourg',
 'Madagascar',
 'Malawi',
 'Malaysia',
 'Maldives',
 'Mali',
 'Malta',
 'Marshall Islands',
 'Mauritania',
 'Mauritius',
 'Mexico',
 'Micronesia',
 'Moldova',
 'Monaco',
 'Mongolia',
 'Montenegro',
 'Morocco',
 'Mozambique',
 'Myanmar',
 'Namibia',
 'Nauru',
 'Nepal',
 'Netherlands',
 'New Zealand',
 'Nicaragua',
 'Niger',
 'Nigeria',
 'North Macedonia',
 'Norway',
 'Oman',
 'Pakistan',
 'Palau',
 'Palestine',
 'Panama',
 'Papua New Guinea',
 'Paraguay',
 'Peru',
 'Philippines',
 'Poland',
 'Portugal',
 'Qatar',
 'Romania',
 'Russia',
 'Rwanda',
 'Saint Kitts and Nevis',
 'Saint Lucia',
 'Saint Vincent and the Grenadines',
 'Samoa',
 'San Marino',
 'São Tomé and Príncipe',
 'Saudi Arabia',
 'Senegal',
 'Serbia',
 'Seychelles',
 'Sierra Leone',
 'Singapore',
 'Slovakia',
 'Slovenia',
 'Solomon Islands',
 'Somalia',
 'South Africa',
 'South Sudan',
 'Spain',
 'Sri Lanka',
 'Sudan',
 'Suriname',
 'Sweden',
 'Switzerland',
 'Syria',
 'Tajikistan',
 'Tanzania',
 'Thailand',
 'Togo',
 'Tonga',
 'Trinidad and Tobago',
 'Tunisia',
 'Turkey',
 'Turkmenistan',
 'Tuvalu',
 'Uganda',
 'Ukraine',
 'United Arab Emirates',
 'United Kingdom',
 'United States',
 'Uruguay',
 'Uzbekistan',
 'Vanuatu',
 'Vatican City',
 'Venezuela',
 'Vietnam',
 'Yemen',
 'Zambia',
 'Zimbabwe',
 'Abkhazia',
 'Artsakh',
 "Donetsk People's Republic",
 'Kosovo',
 "Luhansk People's Republic",
 'Northern Cyprus',
 'Sahrawi Arab Democratic Republic',
 'Somaliland',
 'South Ossetia',
 'Taiwan',
 'Transnistria']

current_countries=COUNTRIES[:]
NEW_GAME = False

GAME_MODE = "start"

def draw_window():
    WIN.fill((100, 100, 100))
    
    if GAME_MODE == "options":
        draw_options_buttons(option_buttons)
        draw_flag()
        draw_navigation_buttons()
    
    if GAME_MODE == "start":
        draw_title()
        draw_start_buttons()

    if GAME_MODE == "game_over":
        draw_score()
        draw_navigation_buttons()
        draw_time_score()
    
    pygame.display.update()

def draw_time_score():
    global END_TIME, START_TIME
    WIN.blit(FONT.render(f"{int((END_TIME-START_TIME)*100)/100} seconds", 1,   BLACK), (400, 300))

def draw_score():
    WIN.blit(FONT.render(f"{SCORE}/207", 1, BLACK), (400, 250))

def draw_title():
    WIN.blit(FONT.render("Flags Game", 1, BLACK), (200, 110))

def draw_navigation_buttons():
    for button in navigation_buttons.values():
        button.draw()

def draw_options_buttons(option_buttons):
    
    for button in option_buttons:
        button.draw()
    
    return

def draw_start_buttons():
    
    for button in start_buttons.values():
        button.draw()
        

def draw_flag():
    WIN.blit(flag_image, (flag_rect.x, flag_rect.y))
    return

def set_flag(qn):
    global flag_image, flag_rect
    
    im = Image.open(f"flag_images/{qn}.jpg")
    im_w, im_h = im.size
    flag_image = pygame.image.load(f"flag_images/{qn}.jpg")
    flag_rect = pygame.Rect(WIDTH//2 - im_w//2, 110 - im_h//2, im_w, im_h)
        

class Button():
    def __init__(self, rect, text="", is_ans = False):
        self.text = text
        self.x = rect.x
        self.y = rect.y
        self.width = rect.width
        self.height = rect.height
        self.rect = rect
        self.is_ans = is_ans
        
    
    def draw(self, button_color = BLACK, text_color = WHITE):
        pygame.draw.rect(WIN, button_color, self.rect)
        WIN.blit(FONT.render(self.text, 1, text_color), (self.x, self.y+self.height//2-FONT_SIZE//2)) 
        #+12 to center the text in button
    
    def set_text(self, text):
        self.text = text
    
    def is_clicked(self, pos):
        
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
        return False

class Option_Choice_Button(Button):
    def chosen(self):
        global SCORE
        flash_time = 0.05
        
        if self.is_ans:
            self.draw(GREEN)
            pygame.display.update()
            time.sleep(flash_time)
            SCORE += 1

        else:
            self.draw(RED)
            pygame.display.update()
            time.sleep(flash_time)
        
        generate_question()

class Start_Choice_Button(Button):
    def chosen(self):
        global GAME_MODE, NEW_GAME, SCORE, END_TIME, START_TIME
        GAME_MODE = "options"
        NEW_GAME = True
        SCORE = 0
        END_TIME = 0
        START_TIME = time.time()
        

class Navigation_Button(Button):
    def chosen(self):
        global GAME_MODE
        GAME_MODE = "start"

def generate_question():
    global NEW_GAME, current_countries, GAME_MODE, END_TIME, START_TIME
    if NEW_GAME:
        NEW_GAME = False
        current_countries = COUNTRIES.copy()    
    
    if not current_countries:
        GAME_MODE = "game_over"
        END_TIME = time.time()
        with open(log_file, "a", newline = "") as file:
            writer = csv.writer(file)
            writer.writerow([f"{SCORE}","207",  f"{END_TIME-START_TIME}", time.strftime('%H:%M%p %Z on %b %d, %Y')])
        return
    
    qn= random.choice(current_countries)
    current_countries.remove(qn)
    
    
    
    opts = [qn]
    
    while len(opts) < 4:
        opt = random.choice(COUNTRIES)
        if opt not in opts:
            opts.append(opt)
    
    random.shuffle(opts)
            
    for i in range(4):
        option_buttons[i].set_text(opts[i])
        option_buttons[i].is_ans = False
        if opts[i] == qn:
            option_buttons[i].is_ans = True
    set_flag(qn)
    return qn, opts



def main():
    
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FR)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONUP:
                click_pos = pygame.mouse.get_pos()
                if GAME_MODE == "options":
                    for button in option_buttons:
                        if button.is_clicked(click_pos):
                            button.chosen()
                    for button in navigation_buttons.values():
                        if button.is_clicked(click_pos):
                            button.chosen() 
                if GAME_MODE == "start":
                    for button in start_buttons.values():
                        if button.is_clicked(click_pos):
                            button.chosen()
                if GAME_MODE == "game_over":
                    for button in navigation_buttons.values():
                        if button.is_clicked(click_pos):
                            button.chosen() 
                            
        
        draw_window()
    
    pygame.quit()

Rects = [pygame.Rect(200,210 , 500, 50), pygame.Rect(200,270 , 500, 50), 
           pygame.Rect(200,330 , 500, 50), pygame.Rect(200,390 , 500, 50)]

option_buttons = [
    Option_Choice_Button(Rects[0]), Option_Choice_Button(Rects[1]), 
    Option_Choice_Button(Rects[2]), Option_Choice_Button(Rects[3])
    ]

start_buttons = {
    "options":Start_Choice_Button(pygame.Rect(200,  210, 500, 50), "Options game")
    }

navigation_buttons = {
    "menu": Navigation_Button(pygame.Rect(700, 50, 100, 50), "MENU")
    }

flag_rect = pygame.Rect(0, 0, 0, 0)
flag_image = None
generate_question()
if __name__ == "__main__":
    main()