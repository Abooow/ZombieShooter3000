
from screens.screen import Screen
from scripts.characters.zombie import Zombie
from scripts.characters.big_zombie import BigZombie
from framework.vector2 import Vector2
from framework.gameobject import GameObject


class EnemySpawner(GameObject):
    '''
    '''

    def __init__(self, waves, player):
        super().__init__()

        self.waves = waves[:][:]
        self.player = player
        self.waves.insert(0, [])

        self.current_wave_index = 0
        self.current_wave = 0
        self.timer = 0
        self.spawned_enemies = []

        self.on_new_wave = None


    def update(self, delta_time):
        '''
        '''

        super().update(delta_time)


        self.timer += delta_time

        if len(self.spawned_enemies) < len(self.waves[self.current_wave]):
            # get the current enemy
            enemy = self.waves[self.current_wave][self.current_wave_index]
            # enemy[0] = time, enemy[1] = type, enemy[2] = x, enemy[3] = y
            if enemy[0] <= self.timer:
                self.spawn_enemy(enemy)

        # end of wave
        if self.current_wave_index == len(self.waves[self.current_wave]) and self.all_is_dead():
            self.new_wave()


    def all_is_dead(self):
        '''
        '''

        return (len(self.spawned_enemies) == len(self.waves[self.current_wave]) and
                all(enemy.is_dead==self.spawned_enemies[0].is_dead==True for enemy in self.spawned_enemies))


    def spawn_enemy(self, enemy):
        '''
        '''

        self.current_wave_index += 1

        enemy_type = None
        position = Vector2(enemy[2], enemy[3])

        if enemy[1] == 'normal_zombie':
            enemy_type = Zombie(self.player, position)
        elif enemy[1] == 'big_zombie':
            enemy_type = BigZombie(self.player, position)

        Screen.get_current_screen().instantiate(enemy_type)
        self.spawned_enemies.append(enemy_type)


    def new_wave(self):
        '''
        '''

        self.timer = 0
        self.current_wave += 1
        self.current_wave_index = 0
        self.spawned_enemies = []

        if self.current_wave == len(self.waves):
            self.current_wave -= 1

        if self.on_new_wave is not None:
            self.on_new_wave(self.current_wave)