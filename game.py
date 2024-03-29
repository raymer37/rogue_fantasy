import libtcodpy as libtcod

############################
##### GLOBAL CONSTANTS #####
############################

SCREEN_WIDTH = 80
SCREEN_HEIGHT = 50
LIMIT_FPS = 20

#####################
##### FUNCTIONS #####
#####################

def handle_keys():
    global playerx, playery

    # toggle fullscreen
    key = libtcod.console_check_for_keypress()
    if key.vk == libtcod.KEY_ENTER and key.lalt:
        libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())

    # exit game
    elif key.vk == libtcod.KEY_ESCAPE:
        return True

    # movement keys
    if libtcod.console_is_key_pressed(libtcod.KEY_UP):
        playery -= 1

    elif libtcod.console_is_key_pressed(libtcod.KEY_DOWN):
        playery += 1

    elif libtcod.console_is_key_pressed(libtcod.KEY_LEFT):
        playerx -= 1

    elif libtcod.console_is_key_pressed(libtcod.KEY_RIGHT):
        playerx += 1

###########################
##### INITIALIZATION ######
###########################

libtcod.console_set_custom_font('arial10x10.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)
libtcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, 'Rogue Fantasy', False, libtcod.RENDERER_SDL2)
con = libtcod.console_new(SCREEN_WIDTH, SCREEN_HEIGHT)
libtcod.sys_set_fps(LIMIT_FPS)

playerx = SCREEN_WIDTH / 2
playery = SCREEN_HEIGHT / 2

###########################
##### OVERWORLD LOOP ######
###########################

while not libtcod.console_is_window_closed():
    libtcod.console_set_default_foreground(con, libtcod.white)
    libtcod.console_put_char(con, playerx, playery, '@', libtcod.BKGND_NONE)
    libtcod.console_blit(con, 0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, 0, 0, 0)
    libtcod.console_flush()
    libtcod.console_put_char(con, playerx, playery, ' ', libtcod.BKGND_NONE)

    exit = handle_keys()
    if exit:
        break
