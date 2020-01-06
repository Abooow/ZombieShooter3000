
import random
import utils


class EnemyWave():
    '''
    '''

    def __init__(self, wave):
        '''
        '''
        
        self.enemies = []

        self.velocity = int(6 + wave * 6  + wave * wave * 0.1)

        self.total_big_zombies = int(self.velocity * (0.12 + wave * 0.02) * 0.5)
        self.total_normal_zombies = 8 + int(self.velocity * 0.15 + wave * 0.65 + wave)

        for i in range(self.total_normal_zombies):
            time = i * 200 + int(i/15) * 3000
            pos = self.get_random_pos()
            self.enemies.append((time, 'normal_zombie', pos[0], pos[1]))

        for i in range(self.total_big_zombies):
            time = i * 300 + int(i/12) * 2000
            pos = self.get_random_pos()
            self.enemies.append((time, 'big_zombie', pos[0], pos[1]))

        self.enemies.sort(key=lambda tup: tup[0])


    def get_random_pos(self):
        posx = 0
        posy = 0

        # top/bottom
        if random.random() < 0.5:
            posx = random.randint(0, utils.world_size[0])
            posy = random.choice([0, utils.world_size[1]])
        else:
            posx = random.choice([0, utils.world_size[0]])
            posy = random.randint(0, utils.world_size[1])

        return (posx, posy)