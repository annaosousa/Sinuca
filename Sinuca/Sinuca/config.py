import math

import numpy as np
import pygame


def get_default_font(size):
    font_default = pygame.font.get_default_font()
    return pygame.font.Font(font_default,size)


def set_max_resolution():
    infoObject = pygame.display.Info()
    global resolution
    global white_ball_initial_pos
    resolution = np.array([infoObject.current_w, infoObject.current_h])
    white_ball_initial_pos = (resolution + [table_margin + hole_radius, 0]) * [0.25, 0.5]

    fullscreen = False

    if not fullscreen:
        resolution = np.array([1000,500])
    window_caption = "Sinuca :"
    fps_limit = 60

    table_margin = 40
    table_side_color = (200,200,0)
    table_color = (0,100,0)
    saparation_line_color(200,200,200)
    hole_radius = 22
    middle_hole_offset =  np.array([[-hole_radius * 2, hole_radius],[-hole_radius, 0], [hole_radius, 0], [hole_radius * 2, hole_radius]])

    middle_hole_offset =  np.array([
        [-2 * math.cos(math.radians(45))*hole_radius - hole_radius, hole_radius],
        [- math.cos(math.radians(45)) * hole_radius,-
        math.cos(math.radians(45))*hole_radius],
        [math.cos(math.radians(45))*hole_radius,
        math.cos(math.radians(45))*hole_radius],
        [- hole_radius, 2* math.cos(math.radians(45)) * hole_radius + hole_radius]
        ])

    player1_cue_color = (200,100,0)
    player2_cue_color = (0,100,200)
    cue_hit_power = 3
    cue_lenght = 250
    cue_thickness = 4
    cue_max_displacement = 100

    cue_safe_displacement = 1
    aiming_line_lenght =14

    total_ball_num=16
    ball_radius = 14
    ball_mass = 14
    speed_angle_threshold = 0.09
    visible_angle_threshold - 0.05
    ball_colors = [
        (255,255,255),
        (0,200,200),
        (0,0,200),
        (150,0,0),
        (200,0,200),
        (200,0,0),
        (50,0,0),
        (100,0,0),
        (0,0,0),
        (0,200,200),
        (0,0,200),
        (150,0,0),
        (200,0,200),
        (200,0,0),
        (50,0,0),
        (100,0,0)
        ]

    ball_stripe_thickness = 5
    ball_stripe_point_num = 25

    ball_strating_place_ratio = [0.75, 0.5]

    if 'resolution' in locals():
        white_ball_initial_pos = (resolution + [table_margin+hole_radius,0]) * [0.25, 0.5]
    ball_label_text_size = 10

    friction_threshold = 0.06
    friction_coeff = 0.99


    ball_coeff_of_restitution = 0.9
    table_coeff_of_restitution = 0.9

    menu_text_color = (255,255,255)
    menu_text_selected_color = (0,0,255)
    menu_title_text = "Sinuca"
    menu_buttons = ["Jogar Sinuca", "Sair"]
    menu_margin = 20
    menu_spacing = 10
    menu_title_font_size = 40
    menu_option_font_size = 20
    exit_button = 2
    play_game_button = 1

    player1_target_text = 'Bolas jogador 1 -'
    player2_target_text = 'Bolas jogador 2 -'
    target_turn_label = "Jogador 1"
    target_turn_label = "Jogador 2"
    penalty_indication_text = "(Click na bola branca para mover)"
    game_over_label_font_size = 40
